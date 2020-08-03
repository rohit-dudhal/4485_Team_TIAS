from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm, UserDetailsForm,UserImagesForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserImages
from django.forms import modelformset_factory
import requests 

import urllib.request
import urllib.parse
import logging
import datetime

logger = logging.getLogger('details.log')
#USER_DETAILS={}
def register(request):
	template_name='register.html'
	if request.method =='POST':
		register_form=RegisterForm(request.POST)
		if register_form.is_valid():
			username=register_form.cleaned_data['username']
			email=register_form.cleaned_data['email']
			password=register_form.cleaned_data['password']
			confirm_password=register_form.cleaned_data['confirm_password']

			if password==confirm_password:
				if User.objects.filter(username=username).exists():
					messages.info(request,'Username Taken!!')
					return redirect('accounts:register')

				elif User.objects.filter(email=email).exists():
					messages.info(request,'Email exists!! Try Logging In')
					return redirect('accounts:register')

				else:
					user = User.objects.create_user(username=username,email=email,
													password=password)
					user.save()
					logger.info(datetime.datetime.now(),': *************User Created************')
					
					return redirect('accounts:userdetails')

			else:
				logger.error(datetime.datetime.now(),": Password not matching!!")
				messages.info(request,"Password not matching!!")
				return redirect('accounts:register')



	else: 
		register_form=RegisterForm()


	context={
				'register_form':register_form,
	}
	return render(request,template_name,context)

def login(request):
	template_name='login.html'

	if request.method=="POST":
		login_form =LoginForm(request.POST)

		if  login_form.is_valid():
			username=login_form.cleaned_data['username']
			password=login_form.cleaned_data['password']

			user=auth.authenticate(username=username,password=password)

			if user is not None:
				auth.login(request,user)
				print('*************User Logged IN************')
				logger.info(datetime.datetime.now(),': *************User Created************')
				return redirect('accounts:userdetails')

			else:
				messages.info(request,"Given Credentials not matching!!")
				return redirect('accounts:login')


	else:
		login_form =LoginForm()


	context={
				'login_form':login_form,
	}
	return render(request,template_name,context)


def logout(request):
	auth.logout(request)
	return redirect('/')


#@login_required
def userDetailsView(request):
	template_name='userDetails.html'
	#ImageFormSet = modelformset_factory(UserImages, form=UserImagesForm, extra=3)
	if request.method=="POST":
		userDetails_form =UserDetailsForm(request.POST)
		#userImage_form =ImageFormSet(request.POST, request.FILES,queryset=UserImages.objects.none())
		if userDetails_form.is_valid():
			firstname=userDetails_form.cleaned_data['firstname']
			lastname=userDetails_form.cleaned_data['lastname']
			dob=userDetails_form.cleaned_data['dob']
			placeOfBirth=userDetails_form.cleaned_data['placeOfBirth']
			gender=userDetails_form.cleaned_data['gender']
			

		#convert to json
			userDetailsDict={
				'firstname':firstname,
				'lastname':lastname,
				'dob':dob,
				'placeOfBirth':placeOfBirth,
				'gender':gender,
				
				}

		URL='http://tiasauthority.pythonanywhere.com/records/api/verify/'
		#userDetails_form.save()
		r = requests.get(url = URL, params = userDetailsDict) 
		if len(r.json())!=0:
			print(r.json(),'********************')
			request.session['userdetails']=(r.json()[0])
			print('USER FOUND')
			return redirect('accounts:classifier')
		else:
			print("NO USER")
		print(userDetailsDict)

		return redirect('/')


		#userImage_form = ImageFormSet(queryset=UserImages.objects.none())
	else:
		userDetails_form=UserDetailsForm()


	context={
				'userDetails_form':userDetails_form,
				
	}
	return render(request,template_name,context)


def classifier(request):

	return render(request,'app.html',{})

def success(request):
	userdetails=request.session.get('userdetails')
	print('classifier',userdetails)
	details= detail(userdetails['firstname'],21,userdetails['gender'],'Bank Fraud',"Airoli")
	m="Team Tias Security Alert \n\n Criminal Found! \n\n"
	for label, value in details.items():
		m=m + label + ": " + value + "\n"
	resp =sendSMS('MdOytkxZLts-jWl88wbMv3Ch0Og7HiP65DJooZWwye', '9769542490',
	'TXTLCL',m)
	print (resp)
	#details= detail(userdetails['firstname'],21,userdetails['gender'],'Bank Fraud',"Airoli")

	email_alert('Criminal Details by Team Tias',details,'rparab190@gmail.com' )

	URL='http://tiasauthority.pythonanywhere.com/records/api/addalert?criminalID=%s&criminalName=%s&lastLocation=airoli&status=spotted' %(userdetails['userID'],userdetails['firstname'])
	print(URL)
	r = requests.get(url = URL)
	return render(request,'success.html',{})

 
import urllib.request
import urllib.parse
 



def sendSMS(apikey, numbers, sender, message):
	data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
	    'message' : message, 'sender': sender})
	data = data.encode('utf-8')
	request = urllib.request.Request("https://api.textlocal.in/send/?")
	f = urllib.request.urlopen(request, data)
	fr = f.read()
	return(fr)



import smtplib
import imghdr
import os
from email.message import EmailMessage

def detail(name1,age,gender,crime,location):
	d=dict()
	d["Name"]=str(name1)
	d["Age"]=str(age)
	d["Gender"]=str(gender)
	d["Crime"]=str(crime)
	d["Location"]="Recently found at " + str(location)
	return d

def email_alert(subject , body, to):
	m="Team Tias Security Alert \n\nCriminal Found\n\n"
	msg = EmailMessage()
	for i,j in body.items():
	    m = m + i + ": " + j +"\n"
	msg.set_content(str(m))
	msg['subject'] = subject
	msg['to'] = to


	user = "tiasbvcoe@gmail.com"
	msg['from'] = user
	password = "jcmdvbjplgpflwoe"


	server = smtplib.SMTP("smtp.gmail.com" , 587)
	server.starttls()
	server.login(user, password)
	server.send_message(msg)
	server.sendmail(user, to, m)

	server.quit()


    