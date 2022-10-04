import urllib.request
import time
import smtplib

precoAlvo = 4.70 #preço máximo para que a mensagem seja enviada


def criarMensagem():  # cria o corpo e assunto do email a ser enviado
    body = f"""Subject: Compre Cafe

Os precos estao abaixo de $4.70, compre.
Preco obtido em {dia}/{mes} as {hora}:{minuto}:{segundo}
Mensagem automatica"""
    return body


def obterLogin():  # obtém login e senha do arquivo enderecoEmail.txt
    with open("enderecoEmail.txt", "r") as file:
        return file.read().split(" ")


def obterDestinos():  # obtém destinos do arquivo destinos.txt
    destinos = []
    with open("destinos.txt", "r") as f:
        for line in f:
            destinos.append(line.strip())
    return destinos


def mensagem():  # conexão smtp
    mail, senha = obterLogin()
    destinos = obterDestinos()
    corpo = criarMensagem()
    print("Enviando mensagem")

    smtpObj = smtplib.SMTP("smtp-mail.outlook.com", 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(mail, senha)
    smtpObj.sendmail(mail, destinos, corpo)
    smtpObj.quit()


def receberPreco(site):  # retorna float com o preço
    pagina = urllib.request.urlopen(site)
    texto = pagina.read().decode("utf8")
    indexacao = (texto.find("$")) + 1
    return float((texto[indexacao : indexacao + 4]))


print("Pressione Control+C para abortar")

while True:
    precoNormal = receberPreco("http://beans.itcarlow.ie/prices.html")
    precoEspecial = receberPreco("http://beans.itcarlow.ie/prices-loyalty.html")

    mes, dia, hora, minuto, segundo = time.localtime()[
        1:6
    ]  # obtém a hora em que a consulta foi feita

    print(f"Preço normal: {precoNormal}  Preço Especial: {precoEspecial} ")
    print(f"Preço obtido em {dia}/{mes}  {hora}:{minuto}:{segundo}")
    print("------")

    if (precoNormal < precoAlvo) or (precoEspecial < precoAlvo):
        mensagem()
        break

    time.sleep(10)
