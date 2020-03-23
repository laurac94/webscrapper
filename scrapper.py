import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.es/Apple-iPhone-64GB-Reacondicionado-Certificado/dp/B0798FPYHQ/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1AEDSIGH5XQHW&keywords=iphone%2Breacondicionados&qid=1584795338&refinements=p_72%3A831280031%2Cp_89%3AApple&rnid=1692911031&sprefix=iphone%2Bre%2Caps%2C175&sr=8-3&th=1s"

headers = {
"User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36'}


def check_price():
  page = requests.get(URL, headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  title = soup.find(id = "productTitle").get_text()


  price = soup.find(id="priceblock_ourprice").get_text()
  converted_price = float(price[0:3])


  if(converted_price < 200):
    send_mail()

  print(title.strip())
  print(converted_price)


  if(converted_price < 200):
    send_mail()


def send_mail():
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('magic@gmail.com','ujdpfruqxkbsttdo')

  subject = 'Price fell down'
  body = 'Check the amazon link https://www.amazon.es/Apple-iPhone-64GB-Reacondicionado-Certificado/dp/B0798FPYHQ/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1AEDSIGH5XQHW&keywords=iphone%2Breacondicionados&qid=1584795338&refinements=p_72%3A831280031%2Cp_89%3AApple&rnid=1692911031&sprefix=

  msg = f"Subject: {subject}\n\n{body}"
  server.sendmail(
    'magic@gmail.com'
    'syrenia93@gmail.com'
    msg

    )

  print('HEY, EMAIL HAS BEEN SENT!')

  server.quit()



check_price()
