import requests
from twilio.rest import Client
from bs4 import BeautifulSoup
import datetime


url = 'http://aplicaciones.americana.edu.co:93/carnets/Consulta.aspx/search'
payload = {'usuario': 1027521897}

now = datetime.datetime.now()
now = now.strftime('%d/%m%Y %H:%M:%S')


page = requests.post(url, json = payload)
soup = BeautifulSoup(page.text, 'html.parser')


account_sid = 'ACbe980398e59ffafa2f5b47a39aa70d24'
password = '905621a578a910f34c2d946cc4d4c8e4'

client = Client(account_sid, password)


seguimiento = True

while seguimiento:

    try:
        if 'SU CARNÉ NO SE ENCUENTRA LISTO, POR FAVOR CONSULTE NUEVAMENTE LA OTRA SEMANA.'.encode('utf-8') in page.content:
            pass

        else:
            message = client.messages.create(to= 'whatsapp:+573026068319', from_= 'whatsapp:+14155238886', body= f'Cristian, su carnet de identificación de la Universidad Americana está listo\nfecha y hora de aviso: {now}')


    except:
        message = client.messages.create(to= 'whatsapp:+573026068319', from_= 'whatsapp:+14155238886', body= f'Cristian,ha ocurrido un error, revisa streamlit\nfecha y hora de aviso: {now}')

        seguimiento = False


