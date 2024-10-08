import email
from email import policy
from email.parser import BytesParser

def analisar_cabecalho_email(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
    
    print("Remetente:", msg['From'])
    print("Destinatário:", msg['To'])
    print("Assunto:", msg['Subject'])
    print("Data de Envio:", msg['Date'])
    
    for header in msg.items():
        print(header)

# Exemplo de uso
analisar_cabecalho_email('email.eml')
