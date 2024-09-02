import re

# Dicionário de simulação para os principais bancos e seus códigos de identificação (BIN - Bank Identification Number)
bancos = {
    "001": "Banco do Brasil",
    "033": "Santander",
    "104": "Caixa Econômica Federal",
    "237": "Bradesco",
    "341": "Itaú",
    "399": "HSBC",
    "745": "Citibank",
    "756": "Bancoob"
}

def extrair_codigo_banco(linha_digitavel):
    # A linha digitável tem 47 caracteres no formato 00000.00000 00000.000000 00000.000000 0 00000000000000
    # O código do banco é formado pelos três primeiros dígitos da linha digitável
    match = re.match(r"^\d{3}", linha_digitavel)
    if match:
        return match.group(0)
    else:
        return None

def validar_boleto():
    # Entrada do usuário - linha digitável do boleto
    linha_digitavel = input("Informe a linha digitável do boleto (apenas números): ").strip()
    
    if not re.match(r"^\d{47}$", linha_digitavel):
        print("A linha digitável deve conter 47 dígitos. Verifique e tente novamente.")
        return

    # Extrai o código do banco da linha digitável
    codigo_banco = extrair_codigo_banco(linha_digitavel)
    
    if codigo_banco not in bancos:
        print("Código de banco desconhecido ou não suportado.")
        return
    
    banco_identificado = bancos[codigo_banco]
    print(f"O boleto pertence ao banco: {banco_identificado}")

    # Confirmação da origem fornecida pelo usuário
    origem_usuario = input("Informe o banco que você acredita ser o emissor do boleto: ").strip()
    
    # Validação da origem
    if origem_usuario.lower() == banco_identificado.lower():
        print("O boleto é autêntico de acordo com as informações fornecidas.")
    else:
        print("A origem fornecida não coincide com o banco emissor. Verifique o boleto.")

# Executa a função de validação de boleto
if __name__ == "__main__":
    validar_boleto()
