import tarefas
import utils 
import database as db
from datetime import datetime as dt

class Ui:
    t = tarefas.Tarefas()

    def print_marcar(self):       
        p = int(input('Qual tarefa quer marcar? '))
        id = utils.validar_id(p, db.listar_tarefas_db())
        if id is None:
            print('Id inválido')
        else: 
            db.des_marcar_db(id)
        return

    def print_criar(self):
        nome = input("Qual o nome da tarefa? ")
        data_str = input("Qual a data? (dd/mm/yyyy ou hoje): ")
        print(self.t.criar_tarefa(nome= nome, data_str = data_str))
        return
    
    def print_editar(self):
        p = int(input('Qual tarefa quer editar? '))
        try:
            id = utils.validar_id(p, db.listar_tarefas_db())
            if id is not None:
                nome = db.listar_tarefas_db()[id-1]['nome']
                data = db.listar_tarefas_db()[id-1]['data']

                print('\nNome: ', nome, '\nData: ', data)
                o = int(input("\n1\tNome\n2\tData\nO que você quer mudar? "))
                if 0 < o < 3:
                    if o == 1: nome = input("Novo nome: ")
                    else: 
                        nova_data = input("Nova data: ")
                        data = utils.validar_data(nova_data)
                        print(data)
                        if data == None:
                            print('Formato de data inválido')
                            return
            else: 
                print("Opção inválida")
                return

            print(self.t.editar_tarefa(id= id, nome= nome, data= data))
            return
        except(ValueError):
            print("Tarefa não encontrada")
    
    def print_deletar(self):
        o = int(input('Qual tarefa quer remover? '))
        id = utils.validar_id(o, db.listar_tarefas_db())
        if id is not None: print(self.t.remover_tarefa(id= id))
        else: print("Tarefa não encontrada")
        return



    def print_menu(self):
        while True:
            print('\n1\tMarcar tarefa')
            print('2\tCriar tarefa')
            print('3\tEditar tarefa')
            print('4\tDeletar tarefa')
            print('5\tMostrar tarefas')
            print('6\tFiltrar tarefas por dia')
            print('0\tSair')
            op = int(input('Opção: '))

            match op:
                case 1: self.print_marcar()
                case 2: self.print_criar()
                case 3: self.print_editar()
                case 4: self.print_deletar()
                case 5: self.t.mostrar_tarefas()
                case 6: self.print_por_dia()
                case 0: break
                case _: print('Opção inválida')
        return

    def print_por_dia(self):
        while True:
            data = input("Qual dia quer filtrar? (dd/mm/yyyy) ")
            dataf = utils.validar_data(data_str= data)
            if dataf is None: print("Data inválida")
            else: break

        print('\n')
        print("="*23)
        formato= '%d/%m/%Y'
        print('🗓️  Tarefas de ', dataf if dt.strptime(dataf, formato).date() != dt.today().date() else 'Hoje')
        print("="*23)

        tarefas_dia = [t for t in db.listar_tarefas_db() if t['data'] == dataf]
        print(dataf)

        if not tarefas_dia: 
                print("Nenhuma tarefa para este dia")
                return
        
        for i, t in enumerate(tarefas_dia):
            sts = '[x]' if t['situacao'] else '[ ]'
            print(i+1, sts, t['nome'])
            
            
        total = len(tarefas_dia)
        concluidas = sum(t['situacao'] for t in tarefas_dia)
        print("\nTotal de tarefas para hoje: ", total)
        print("Total de tarefas concluídas: ", concluidas)
        print("Total de tarefas pendentes: ", total-concluidas)
        print('='*23)
        return

    
