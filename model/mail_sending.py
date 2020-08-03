# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 21:15:51 2020

@author: tejas
"""
import os
import smtplib
import imghdr
from email.message import EmailMessage
import urllib.request
import urllib.parse
global x
x=[]

class Mail_sending(object):
    def send_mail(self,name=None):
        print(name)
        EMAIL_ADDRESS = 'teamtias6@gmail.com'
        EMAIL_PASSWORD = 'acerswift6'
        link='https://www.google.co.in/maps/place/Mahindra+Towers/@19.0040909,72.8157536,15.81z/data=!4m13!1m7!3m6!1s0x3be7ce9734348cc5:0x1f77abaae06400ec!2sWorli,+Mumbai,+Maharashtra!3b1!8m2!3d18.9986406!4d72.8173599!3m4!1s0x3be7ce941d496ee5:0xfce04fdca10381aa!8m2!3d19.0060136!4d72.8216127'

        msg = EmailMessage()
        msg['Subject'] = 'TIAS Security Alert'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'tejasghadshi60@gmail.com'
        msg.set_content('Criminal Activity Detected. \nSending captured image...\nName of Criminal:'+name+'\nLocation:\n'+link+'\n')
        with open(name+'.jpg', 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
    
        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print('Mail Send')
            # resp =  Mail_sending().sendSMS('4R0EHR8oczk-gSxm8CRZ0kwplAMXkBMSoPnh4KcRVr', '9152245356',
            #                 'TXTLCL','CRIMINAL FOUND')
            # print (resp)
            return "Yes"
            
            
    # def sendSMS(apikey, numbers, sender, message):
    #     data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
    #                                     'message' : message, 'sender': sender})
    #     data = data.encode('utf-8')
    #     request = urllib.request.Request("https://api.textlocal.in/send/?")
    #     f = urllib.request.urlopen(request, data)
    #     fr = f.read()
    #     return(fr)
 

        
    