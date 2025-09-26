# Projeto TO-DO List - Gerenciador de tarefas inteligente

É um projeto de lista de tarefas desenvolvido em **Python**, com interface gráfica utilizando **CustomTkinter** e banco de dados **SQLite** para persistência.  
Permite adicionar, editar, marcar/desmarcar como concluída, visualizar e excluir tarefas.

## Funcionalidades
✔ Criar novas tarefas  
✔ Editar tarefas existentes  
✔ Marcar / desmarcar tarefas como concluídas  
✔ Excluir tarefas  
✔ Visualizar lista de tarefas em interface gráfica  
✔ Persistência dos dados em **SQLite**

## Tecnologias utilizadas
- **Python 3**  
- **CustomTkinter** — interface gráfica moderna  
- **SQLite** — banco de dados local e leve

## Estrutura do projeto

```text
/
├── UI.py              # Interface gráfica (CustomTkinter)
├── todo_list.py       # Inicialização da aplicação
├── tarefas.py         # Classe/métodos de manipulação das tarefas
├── database.py        # Operações com SQLite
├── utils.py           # Funções auxiliares
├── To-do_list.db      # Banco de dados SQLite
└── __pycache__/       # Cache do Python
