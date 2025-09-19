import sqlite3
conn = sqlite3.connect("To-do_list.db")
conn.row_factory = sqlite3.Row
crs = conn.cursor()

crs.execute('''
    CREATE TABLE IF NOT EXISTS Tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data TEXT NOT NULL,
        situacao INTEGER DEFAULT 0)''')

conn.commit()

def criar_tarefa_db(nome, data_str):
    crs.execute("INSERT INTO Tarefas (nome, data) VALUES (?, ?)", (nome, data_str))
    conn.commit()

def listar_tarefas_db():
    tab = crs.execute('SELECT * FROM Tarefas')
    return tab.fetchall()

def des_marcar_db(id):
    crs.execute("SELECT situacao FROM Tarefas WHERE id = ?", (id,))
    sit = crs.fetchone()
    if sit is None: 
        print('Tarefa não encontrada')
        return
    new_sit = 1 if sit[0] == 0 else 0

    crs.execute("UPDATE Tarefas SET situacao = ? WHERE id = ?", (new_sit, id))
    conn.commit()

def remover_tarefas_db(id):
    crs.execute("DELETE FROM Tarefas WHERE id = ?", (id,))
    conn.commit()

def editar_tarefas_db(id, nome, data):
    crs.execute("UPDATE Tarefas SET nome = ?, data = ? WHERE id = ?", (nome, data, id))
    conn.commit()