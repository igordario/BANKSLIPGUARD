import extract_msg

def analisar_cabecalho_email(caminho_arquivo):
    # Substitua 'caminho_arquivo' pelo caminho do seu arquivo .msg
    msg = extract_msg.Message(caminho_arquivo)
    header = msg.header
    # Define os campos que serão extraídos do cabeçalho
    header_keys = ["Remetente","Destinatário","Assunto","Data de envio",'Message-ID', \
                    "Received-SPF","Return-Path","DKIM-Signature","DMARC"]
    # Extrai os valores que serão associados a cada campo
    header_values = [msg.sender,msg.to,msg.subject,msg.date,header.get('Message-ID'), \
                     header.get('Received-SPF'),header.get('Return-Path'),header.get('DKIM-Signature'),header.get('DMARC')]
    
    header_data = {}

    # Cria o dicionário Campo:valor
    for i in range(len(header_keys)):
        header_data[header_keys[i]] = header_values[i]
        print(f"{header_keys[i]}: {header_values[i]}")

    # Localiza e extrai o domínio do remetente no cabeçalho
    sender_domain = header_data['Remetente'][header_data['Remetente'].find('@')+1:len(header_data['Remetente'])-1]
    
    # Valores necessários para que cada campo seja válido (== 1)
    states = [sender_domain,'pass',sender_domain,sender_domain,'pass']

    # Checa se cada um dos valores é o esperado e cria um dicionário para armazenar os resultados
    check = {}
    for i in range(4,len(header_keys)):
        if header_data[header_keys[i]] == None:
            check[header_keys[i]] = None
        elif states[i-4] in header_data[header_keys[i]].lower():
            check[header_keys[i]] = 1
        else:
            check[header_keys[i]] = 0
          
    print("\n")
    print(check)

# Exemplo de uso
analisar_cabecalho_email(r'C:\Users\J4VR\Downloads\fortinet_email.msg')
