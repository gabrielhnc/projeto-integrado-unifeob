from datetime import datetime
import time

# DATA ----------------------------------------------------------------------

def obter_data(mensagem="\nDigite a data (DD/MM/YYYY) [0 para cancelar]: "):
    while True:
        data = input(mensagem)
        if data == '0':
            print("[!] Operação cancelada.")
            return None
        if validar_data(data):
            return data
        print("[!] Data inválida. Use o formato DD/MM/YYYY.")

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
def conversao_data(data):
    data_formatada = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
    return data_formatada

# HORA ----------------------------------------------------------------------

def obter_hora(mensagem="Digite a hora (HH:MM:SS) [0 para cancelar]: "):
    while True:
        hora = input(mensagem)
        if hora == '0':
            print("[!] Operação cancelada.")
            return None
        if validar_hora(hora):
            return hora
        print("[!] Hora inválida. Use o formato HH:MM:SS.")


def validar_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M:%S")
        return True
    except ValueError:
        return False

# STATUS ----------------------------------------------------------------------

def obter_status(mensagem="Digite o status (Pendente, Confirmado, Cancelado) [0 para cancelar]: "):
    while True:
        status = input(mensagem)
        if status == '0':
            print("[!] Operação cancelada.")
            return None
        if validar_status(status):
            return status
        print("[!] Status inválido. Escolha entre Pendente, Confirmado, Cancelado.")


def validar_status(status):
    return status in ["Pendente", "Confirmado", "Cancelado"]

# QUANTIDADE ----------------------------------------------------------------------

def obter_quantidade(mensagem="Digite a quantidade (g) [0 para cancelar]: "):
    while True:
        quantidade = input(mensagem)
        if quantidade == '0':
            print("[!] Operação cancelada.")
            return None
        if validar_quantidade(quantidade):
            return float(quantidade)

def validar_quantidade(quantidade):
    try:
        if float(quantidade) > 0:
            return True
        else:
            print("[!] A quantidade deve ser maior que zero.")
            return False
    except ValueError:
        print("[!] Quantidade inválida. Digite um número válido.")
        return False

# CONSULTA/VALIDAR ID ----------------------------------------------------------------------

def consultar_e_validar_id(consulta_func, consulta_por_id_func, entidade):
    while True:
        print(f"\nConsultando {entidade}(s)...")
        time.sleep(2)
        consulta_func()
        try:
            id_escolhido = input(f"\nDigite o ID do(a) {entidade} escolhido(a) para continuar [0 para cancelar]: ")
            if id_escolhido == '0':
                print(f"\n[!] Operação cancelada.")
                return None
            print("\nVerificando Escolha...")
            time.sleep(2)
            if consulta_por_id_func(id_escolhido):
                return id_escolhido
            else:
                print(f"[!] Tente novamente.")
        except ValueError:
            print("[!] ID inválido. Digite um número válido.")
