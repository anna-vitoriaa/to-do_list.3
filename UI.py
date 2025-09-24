import tarefas
import utils 
import database as db
from datetime import datetime as dt
import customtkinter as ctk
import locale
from tkcalendar import DateEntry

class Ui:
    def __init__(self):
        self.t = tarefas.Tarefas()
        locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

        # Aparência
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')

        # Janela principal
        self.app = ctk.CTk()
        self.app.title("TO-DO List")
        self.app.geometry("900x600")

        frame_titulo = ctk.CTkFrame(self.app, fg_color='transparent')
        frame_titulo.pack(pady= 10)

        label_titulo = ctk.CTkLabel(frame_titulo, text= '📝 TO-DO List', font=("Arial", 26, 'bold'))
        label_titulo.pack()

        label_subtitulo = ctk.CTkLabel(frame_titulo, text="Gerenciador de texto inteligente", font=("Arial", 14))
        label_subtitulo.pack()

            # Adicionar tarefas
        frame_add = ctk.CTkFrame(self.app, corner_radius= 15)
        frame_add.pack(pady = 20, padx = 20, fill = 'x')

        label_add = ctk.CTkLabel(frame_add, text= "+ Adicionar tarefa", font=('Arial',20, 'bold'))
        label_add.grid(row=0, column=0, columnspan=3, sticky='w', pady=10, padx=10)

        self.entry_nome = ctk.CTkEntry(frame_add, placeholder_text="Nome da tarefa...", font=("Arial", 18))
        self.entry_nome.grid(row=1, column=0, columnspan=3, sticky='ew', padx=10, pady=10)

        self.entry_data = DateEntry(frame_add, date_pattern= 'dd/MM/yyyy', width=14, font=('Arial', 13))
        self.entry_data.grid(row=1, column=4, pady=10, padx=10)

        btt_add = ctk.CTkButton(frame_add, text='Adicionar', command=self.print_criar)
        btt_add.grid(row=1, column= 5, padx=10, pady=10)

        self.label_return_add = ctk.CTkLabel(frame_add, text=' ', font=("Arial", 20), justify= 'center')

        frame_add.grid_columnconfigure(0, weight=1)

        # Filtrar Tarefas
        frame_filtro = ctk.CTkFrame(self.app, corner_radius= 15)
        frame_filtro.pack(pady=20, padx=20, fill='x')

        label_filtro = ctk.CTkLabel(frame_filtro, text="🔍 Filtrar Tarefas", font=("Arial", 20, 'bold'))
        label_filtro.grid(row=0, column=0, columnspan=3, sticky='w', padx=10, pady=10)

        btt_todas = ctk.CTkButton(frame_filtro, text="Todas", corner_radius=15, fg_color="#012E40")
        btt_todas.grid(row=1, column=0, padx=10, pady=10)
        btt_pendentes = ctk.CTkButton(frame_filtro, text="Pendentes", corner_radius=15, fg_color="#D1B40D")
        btt_pendentes.grid(row=1, column=1, padx=7, pady=7)
        btt_concluidas = ctk.CTkButton(frame_filtro, text="Concluídas", corner_radius=15, fg_color="#024E0C")
        btt_concluidas.grid(row=1, column=2, padx=7, pady=7)

        entry_data = DateEntry(frame_filtro, date_pattern= 'dd/MM/yyyy', width=14, font=('Arial', 13))
        entry_data.grid(row=1, column=3, pady=7, padx=7)
        btt_limpar = ctk.CTkButton(frame_filtro, text="🧹 Limpar", corner_radius=15, fg_color="#661212")
        btt_limpar.grid(row=1, column=4, padx=7, pady=7) 

        frame_tarefa = ctk.CTkFrame(self.app, corner_radius=15)
        frame_tarefa.pack(pady=20, padx=20, fill='both', expand=True)

        label_vazio = ctk.CTkLabel(frame_tarefa, text="Nenhuma tarefa encontrada!", font=("Arial", 20, 'bold'), justify= 'center')
        label_vazio_sub = ctk.CTkLabel(frame_tarefa, text="Adicione uma tarefa ou mude o filtro", font=("Arial", 16), justify= 'center')
        label_vazio.pack(pady= (30, 3))
        label_vazio_sub.pack(pady= (0, 30))

    def rodar(self):
        self.app.mainloop()

    def print_marcar(self):       
        p = int(input('Qual tarefa quer marcar? '))
        id = utils.validar_id(p, db.listar_tarefas_db())
        if id is None:
            print('Id inválido')
        else: 
            db.des_marcar_db(id)
        return
    def print_criar(self):
        nome = self.entry_nome.get().strip()
        data_str = self.entry_data.get()
        if data_str == None or nome == '': text = "Os campos não podem estar vazios"
        else: text = self.t.criar_tarefa(nome= nome, data_str = data_str)
        self.label_return_add.grid(pady=10, padx=10, row=2, column=0, columnspan = 10)
        self.label_return_add.configure(text= text)
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

    
