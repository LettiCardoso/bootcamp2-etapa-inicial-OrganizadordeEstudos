# FocusFlow - Foco de Estudos 🎓
[![Python CI](https://github.com/LettiCardoso/bootcamp2-etapa-inicial-OrganizadordeEstudos/actions/workflows/ci.yml/badge.svg)](https://github.com/LettiCardoso/bootcamp2-etapa-inicial-OrganizadordeEstudos/actions/workflows/ci.yml)
## 🧠 Problema Real
Muitos estudantes enfrentam a chamada "paralisia por análise" ou dificuldade severa em manter uma rotina. A falta de um ponto de partida claro e o sentimento de sobrecarga levam à procrastinação crônica, afetando o desempenho acadêmico e a saúde mental.

## 💡 Proposta da Solução
O **FocusFlow** é uma ferramenta de gestão de foco baseada na técnica de micro-metas. A aplicação permite que o estudante defina uma tarefa específica e um tempo determinado, forçando o cérebro a sair da inércia inicial através de um cronômetro visual simples e direto, sem distrações.

## 👥 Público-alvo
- Estudantes universitários e secundaristas.
- Candidatos a concursos e exames (OAB, ENEM).
- Pessoas com dificuldade de organização ou TDAH.

## ✨ Funcionalidades Principais
- **Definição de Meta:** Espaço para digitar a disciplina ou tarefa atual.
- **Cronômetro Customizável:** Definição de tempo em minutos.
- **Notificações:** Alerta visual ao concluir um ciclo de estudos.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Interface Gráfica:** Tkinter
- **Testes:** Pytest
- **Qualidade de Código:** Flake8 (Linting)
- **CI/CD:** GitHub Actions (Automação de testes e linting)


## 🧪 Como testar
🧪 Instruções para Rodar os Testes
Para validar a lógica do sistema e garantir que tudo está funcionando:
### Execute: `py -m pytest` 
<img width="1819" height="901" alt="image" src="https://github.com/user-attachments/assets/cba81463-93ac-4102-ac7a-f5ff5135125a" /> <br>
### **Caso não funcione,** 
### Execute`py -m pip install pytest`

### 🧹 Instruções para Rodar o Lint
Para verificar a padronização e qualidade do código (análise estática):
###  Execute:`flake8 src/`
<img width="1096" height="727" alt="image" src="https://github.com/user-attachments/assets/806d5bc1-b3b6-427c-8f08-fac90e431277" /> <br>
### **Caso não funcione,** 
### Execute`py -m pip install flake8`
## ⚙️ Como executar
### 1. Clone o repositório, Abra o terminal ou prompt de comando e digite: ` git clone https://github.com/LettiCardoso/bootcamp2-etapa-inicial-OrganizadordeEstudos.git`
### 1. Instale as dependências: `py -m pip install -r requirements.txt`
### 2. Execute o app utilizando o terminal: `py src/main.py`
<img width="1901" height="934" alt="image" src="https://github.com/user-attachments/assets/edd604fa-c3cd-4052-b5ae-4e851e9421cf" /> <br>
### 📖 Como utilizar o FocusFlow (v1.0.0 - Versão Inicial)
Nesta versão de lançamento, o foco foi a simplicidade extrema. O sistema foi projetado para seguir o fluxo "uma vez iniciado, foco total até o fim".

1. Definindo a Tarefa
No campo de entrada superior, escreva o nome da atividade que você vai realizar. Isso serve como um lembrete visual do seu compromisso atual.

2. Ajuste de Tempo
No campo de minutos, insira o tempo desejado para o seu bloco de concentração. O padrão sugerido pelo sistema é de 25 minutos.

3. Início do Ciclo
Clique no botão "Iniciar Foco".

Importante: Nesta versão inicial, o cronômetro rodará ininterruptamente até chegar ao zero. É o modo "foco profundo", sem distrações e sem pausas intermediárias.

4. Conclusão
Ao final do tempo definido, o sistema emitirá um alerta visual informando que seu ciclo de estudos foi concluído com sucesso. Para iniciar uma nova sessão, basta fechar o alerta e configurar um novo tempo.


### 🚀 Versão Atual: 1.0.0 (Semantic Versioning)
### 👤 Autora: Letícia Cardoso
 
 🔗 Link do Repositório Público `https://github.com/LettiCardoso/bootcamp2-etapa-inicial-OrganizadordeEstudos.git`
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
│   └── test_logic.py&ensp; &ensp;&ensp; # Testes automatizados<br><br>├── .flake8 &ensp; &ensp;&ensp;# Configuração do Linter<br>
├── CHANGELOG.md &ensp; &ensp;&ensp;#Alterações<br>
├── CONTRIBUITING.md &ensp; &ensp;&ensp;#Contribuição<br><br>
── **Imagens**/<br>
└── Exemplo de usos &ensp; &ensp;&ensp;<br><br>
├── LICENSE &ensp; &ensp;&ensp;#Licensa<br>
├── README.md &ensp; &ensp;&ensp;# Documentação<br>
└── VERSION &ensp; &ensp;&ensp;# Versão semântica (1.0.0)<br>
├── requirements.txt &ensp; &ensp;&ensp;# Dependências<br>


>
