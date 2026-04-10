# Documentação | bootcamp2-etapa-inicial-OrganizadordeEstudos
Aplicação parar organizar rotina de estudos para estudantes com dificuldade como atividade inicial de Bootcamp II

# FocusFlow - Foco de Estudos 🎓
O **FocusFlow** é uma aplicação GUI simples projetada para estudantes que enfrentam dificuldades em manter uma rotina de estudos ou que sofrem com a procrastinação.

### 🚀 Versão Atual: 1.0.0 (Semantic Versioning)
## 🧠 O Problema Real
Muitos estudantes falham não por falta de capacidade, mas por dificuldade em **quebrar a inércia**. O FocusFlow utiliza a lógica de micro-metas para reduzir a ansiedade e facilitar o foco.
## 🛠️ Tecnologias
- Python 3.x
- Tkinter (Interface Gráfica)
- Pytest (Testes Unitários)
- Flake8 (Linting)
- GitHub Actions (CI)

## ⚙️ Como executar
1. Clone o repositório, Abra o terminal ou prompt de comando e digite: ` git clone https://github.com/LettiCardoso/bootcamp-etapa-inicial-OrganizadordeEstudos.git`
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute o app: `python src/main.py`

## 🧪 Como testar
Execute: `py -m pytest`
## 🛠️ Estrutura do Projeto 

### bootcamp2-etapa-inicial-OrganizadordeEstudos/<br>
├── **.github**/<br>
│   └── **workflows**/<br>
│      └── ci.yml &ensp; &ensp;&ensp;#Pipeline de CI (GitHub Actions)<br><br>
├── **src**/<br>
│   ├── _ _init_ _.py<br>
│   ├── main.py  &ensp; &ensp;&ensp;# Interface GUI (Tkinter)<br>
│   └── logic.py  &ensp; &ensp;&ensp;# Lógica de negócio<br><br>
├── **tests**/<br>
│   └── test_logic.py&ensp; &ensp;&ensp; # Testes automatizados<br><br>
├── requirements.txt &ensp; &ensp;&ensp;# Dependências<br>
├── .flake8 &ensp; &ensp;&ensp;# Configuração do Linter<br>
├── README.md &ensp; &ensp;&ensp;# Documentação<br>
└── VERSION &ensp; &ensp;&ensp;# Versão semântica (1.0.0)<br>