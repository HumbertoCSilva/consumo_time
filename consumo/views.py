from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from .models import Funcionario, Item, Lancamento

# 1. Tela de Identificação (Login por CPF)
def login_funcionario(request):
    if request.method == "POST":
        cpf_digitado = request.POST.get('cpf')
        try:
            # Busca o funcionário pelo CPF
            funcionario = Funcionario.objects.get(cpf=cpf_digitado)
            request.session['funcionario_id'] = funcionario.id
            return redirect('lancar_consumo')
        except Funcionario.DoesNotExist:
            messages.error(request, "CPF não encontrado.")
    return render(request, 'login.html')

# 2. Tela de Lançamento de Consumo
def lancar_consumo(request):
    # Recupera o ID do funcionário que "logou" via CPF
    func_id = request.session.get('funcionario_id')
    if not func_id:
        return redirect('login_funcionario')
    
    funcionario = get_object_or_404(Funcionario, id=func_id)
    itens_disponiveis = Item.objects.all()

    if request.method == "POST":
        # Captura a lista de IDs (ex: ['1', '1', '2'] se clicou 2x no item 1 e 1x no item 2)
        itens_ids = request.POST.getlist('itens')
        
        if itens_ids:
            # 1. Cria a instância do lançamento vinculada ao funcionário
            novo_lancamento = Lancamento.objects.create(funcionario=funcionario)
            
            # 2. Busca os objetos únicos no banco para associar ao ManyToMany
            objetos_itens = Item.objects.filter(id__in=itens_ids)
            
            # 3. Mapeia os preços em um dicionário para cálculo rápido {str(id): valor}
            tabela_precos = {str(item.id): item.valor for item in objetos_itens}
            
            # 4. Calcula o total real percorrendo a lista original vinda do POST (com duplicatas)
            total_calculado = sum(tabela_precos.get(id_str, 0) for id_str in itens_ids)
            
            # 5. Salva os dados finais
            novo_lancamento.itens.set(objetos_itens) # Salva a relação (única por item)
            novo_lancamento.total = total_calculado  # Salva o valor acumulado real
            novo_lancamento.save()
            
            messages.success(request, f"Consumo de R$ {total_calculado:.2f} lançado para {funcionario.nome}!")
            
            # Limpa a sessão para que o próximo colaborador precise digitar o CPF
            del request.session['funcionario_id'] 
            return redirect('login_funcionario')
        else:
            messages.warning(request, "Seu carrinho está vazio. Adicione itens antes de finalizar.")

    return render(request, 'consumo.html', {
        'funcionario': funcionario, 
        'itens': itens_disponiveis
    })

# 3. Tela de Relatório e Fechamento (Filtro por Datas)
def relatorio_consumo(request):
    # Captura os filtros de data da URL para filtragem local
    data_inicio = request.GET.get('inicio')
    data_fim = request.GET.get('fim')
    
    lancamentos = Lancamento.objects.all().order_by('-data_hora')
    
    # Filtra os lançamentos salvos localmente por período
    if data_inicio and data_fim:
        lancamentos = lancamentos.filter(data_hora__date__range=[data_inicio, data_fim])
    
    # Agrega a soma de tudo que foi consumido no período
    total_geral = lancamentos.aggregate(Sum('total'))['total__sum'] or 0
    
    # Agrupamento para ver quanto cada um dos 7 funcionários consumiu
    resumo_funcionarios = lancamentos.values('funcionario__nome').annotate(
        total_gasto=Sum('total')
    ).order_by('-total_gasto')

    return render(request, 'relatorio.html', {
        'lancamentos': lancamentos,
        'total_geral': total_geral,
        'resumo_funcionarios': resumo_funcionarios,
        'data_inicio': data_inicio,
        'data_fim': data_fim
    })