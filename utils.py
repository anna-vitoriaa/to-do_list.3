from datetime import datetime

def validar_data(data_str):
    formato = "%d/%m/%Y"
    data = datetime.strptime(data_str, formato).date()
    if data >= datetime.today().date():
        return data.strftime(formato)
    else:
        return None
    
def validar_id(id, lista):
    if 0 < id <= len(lista):
        return id
    else: return None