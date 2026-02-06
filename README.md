# 📊 Consumo_Time

Sistema web prático desenvolvido em **Python** e **Django** para gestão de consumo interno de equipes. O projeto foi desenhado para ser rápido, escalável e de fácil manutenção, permitindo o controle de gastos de colaboradores de forma intuitiva.

## 🚀 Funcionalidades

- **Identificação por CPF:** Acesso direto ao perfil do funcionário sem necessidade de senhas.
- **Interface PDV com Cliques:** Botões de itens que permitem adicionar múltiplas unidades ao carrinho através de cliques sucessivos.
- **Busca em Tempo Real:** Barra de pesquisa para localização rápida de itens no catálogo.
- **Relatório Administrativo:** Página dedicada para fechamento mensal com filtros de data e soma total por funcionário.
- **Gestão via Admin:** Interface completa para cadastro de funcionários e itens (CRUD) nativa do Django.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.12 / Django.
- **Frontend:** HTML5, CSS3 e JavaScript (Vanilla).
- **Banco de Dados:** SQLite (Armazenamento local em arquivo `db.sqlite3`).

---

## 💻 Como Executar o Projeto

Escolha a modalidade que melhor se adapta à sua necessidade:

### Opção A: Execução via Git (Desenvolvimento/Sincronização)
Ideal para quando você deseja manter o código atualizado em diferentes máquinas.

1. **Clonar o Repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/consumo_time.git](https://github.com/seu-usuario/consumo_time.git)
   cd consumo_time
Criar e Ativar Ambiente Virtual:

Bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
Instalar Dependências:

Bash
pip install django
Rodar o Servidor:

Bash
python manage.py runserver 0.0.0.0:8000
Opção B: Execução Manual (Sem Git / Pen Drive)
Ideal para transferir o sistema pronto para um computador de produção ou uso offline.

Copiar Arquivos:

Copie a pasta consumo_time para o novo PC (não copie a pasta venv).

Certifique-se de que o arquivo db.sqlite3 está na raiz para manter os dados já cadastrados.

Criar Novo Ambiente Virtual: No terminal da pasta do projeto:

Bash
python -m venv venv
.\venv\Scripts\activate
Instalar Django:

Bash
pip install django
Iniciar Sistema:

Bash
python manage.py runserver 0.0.0.0:8000
📁 Estrutura do Projeto
Plaintext
consumo_time/
├── consumo/              # App principal (Lógica de consumo)
│   ├── templates/        # Telas (login.html, consumo.html, relatorio.html)
│   ├── models.py         # Tabelas de Funcionário, Item e Lançamento
│   └── views.py          # Lógica de cálculo e filtros
├── core/                 # Configurações do Django
├── db.sqlite3            # Banco de dados local com seus registros
└── manage.py             # Script de execução
🔐 Acessos
Interface de Lançamento: http://localhost:8000

Relatório de Fechamento: http://localhost:8000/relatorio

Painel Administrativo: http://localhost:8000/admin (Requer superuser)
