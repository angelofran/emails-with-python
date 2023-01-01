# Fazer as importações
import requests as rq
import smtplib as smt
import email.message

# Fazer a requisição
requisição = rq.get('https://economia.awesomeapi.com.br/last/USD-AOA')
requisição_dict = requisição.json()
cotação = int(requisição_dict['USDAOA']['bid'])

# Mandar o e-mail
def enviar_email():
    body = f"""
    <p>A cotação do dolár, está abaixo de 500</p>
    <p>Agora a cotação é de {cotação}</p>
    """
    msg = email.message.Message()
    msg['subject'] = "Cotação do Dolár"
    msg['From'] = "angelofrancisco2008@gmail.com"
    msg['To'] = "nerdoriginal999@gmail.com"
    password = 'jibpznlnerryfwrp'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    s = smt.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
if  cotação < 500:
    enviar_email()
else:
    print(f'A cotação está acima, agora são {cotação} kwz')
