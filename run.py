from firebase import firebase
from email import header
from email.quoprimime import body_check
from math import prod
from bs4 import BeautifulSoup
import requests
import smtplib
import os

#headers is used to identify the version of browser i am using
headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'}
#FBconn is used to establish a connection between firebase and my program 
FBconn=firebase.FirebaseApplication('https://my-web-scrapper-3dff1-default-rtdb.firebaseio.com/',None)

#this function is used to check the price of the product all the webscrapping happens in this function
def check_price(data):
      page =requests.get(data[1],headers=headers)
      soup=BeautifulSoup(page.content,'html.parser')
      details =soup.find("h1",{"class":"yhB1nd"}).get_text();
      price =soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text();
      convertedPrice=0

      for i in range (1,len(price)):
        if(price[i]!=','):
          convertedPrice=convertedPrice*10 + (ord(price[i])-48)

      desiredPrice=0
      for i in range (0,len(data[2])):
        desiredPrice=desiredPrice*10 + (ord(data[2][i])-48) 
      print(data[3])
      if(convertedPrice<=desiredPrice):
          send_mail(data[0],data[1])
          satisfied=FBconn.post('/satisfiedCustomrers/',data[0])
          FBconn.delete('/customerList/'+data[3],None)
      
        

#this function will run whenever i want to run and take whole database an input
def runApplication():
    mydata=FBconn.get('/customerList/',None)
    for x in mydata:
        data=[mydata[x]['customerEmaiil'],
        mydata[x]['product'],mydata[x]['desiredPrice'],x] 
        check_price(data)

#this function is used to send mail when the product is less than the desired price of the customer
def send_mail(data,URL):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('abhisheksha952@gmail.com','konrvplwrxrlpynv')
    subject ='price fell down!'
    body = 'check the flipkart link '+ URL
    msg =f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'abhisheksha952@gmail.com',
        data,
         msg
     )
    print('Hey email has been sent!')
    print('to '+data)
    server.quit()
    
print("runApplication")
runApplication()

