import locale
import UI
from datetime import datetime

ui = UI.Ui()
t = ui.t
locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
dia_semana = datetime.today().strftime("%a").upper()

print('='* 5, ' TODO LIST ', '='*5)
print(datetime.today().strftime('%d/%m/%Y'), "\t", dia_semana)

while True:
    t.mostrar_tarefas()
    op = int(input("\n1\tMarcar\n2\tMenu\n0\tSair\n"))
    if op == 1: ui.print_marcar()
    elif op== 2: ui.print_menu()
    elif op == 0: break
    else: print('Opção Inválida')
