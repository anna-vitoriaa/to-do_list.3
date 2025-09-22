import locale
import UI
from datetime import datetime

ui = UI.Ui()
t = ui.t

print('='* 5, ' TODO LIST ', '='*5)

while True:
    t.mostrar_tarefas()
    op = int(input("\n1\tMarcar\n2\tMenu\n0\tSair\n"))
    if op == 1: ui.print_marcar()
    elif op== 2: ui.print_menu()
    elif op == 0: break
    else: print('Opção Inválida')
