from datetime import datetime
import utils as ut
import database as db

class Tarefas:
    def __init__(self):
        self.d = datetime.today()
        self.hoje_str = datetime.strftime(self.d, "%d/%m/%Y")
        self.situacao = False
        self.tarefas = []
    
    def criar_tarefa(self, nome, data_str):
        try:
            data_str = ut.validar_data(data_str= data_str)
            if data_str is not None:
                db.criar_tarefa_db(nome, data_str)
                return 'Tarefa criada'
            else: return ("Data inválida")
        except(ValueError):
            print("Inválido")
    
    def mostrar_tarefas(self):
        print('='*23)
        for i, v in enumerate(db.listar_tarefas_db()):
            sts = '[x]' if v['situacao'] else '[ ]'
            print(i+1, sts, v['nome'])
        print('='*23)

    def remover_tarefa(self, id):
        try:
            db.remover_tarefas_db(id)
            return 'Tarefa removida'
        except(ValueError):
            print("Inválido")
    
    def editar_tarefa(self, id, nome, data):
        try:
            db.editar_tarefas_db(id, nome, data)
            return "Tarefa editada"
        except(ValueError):
            print("Inválido")
