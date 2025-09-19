from datetime import datetime

def validar_data(data_str):
    formato = "%d/%m/%Y"
    if data_str.strip().upper() == 'HOJE':
        return datetime.today().strftime(format= formato)
    
    try:
        return datetime.strptime(data_str, formato).strftime(formato)
    except(ValueError):
        return None
    
def validar_id(id, lista):
    if 0 < id <= len(lista):
        return id
    else: return None