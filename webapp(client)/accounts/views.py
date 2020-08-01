from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm, UserDetailsForm,UserImagesForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserImages
from django.forms import modelformset_factory
import requests 

import urllib.request
import urllib.parse

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
					print('*************User Created************')
					return redirect('accounts:userdetails')

			else:
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
				return redirect('/')

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
			address=userDetails_form.cleaned_data['address']
			city=userDetails_form.cleaned_data['city']
			country=userDetails_form.cleaned_data['country']
			zipcode=userDetails_form.cleaned_data['zipcode']
			email=userDetails_form.cleaned_data['email']
			aadhar=userDetails_form.cleaned_data['aadhar']
			pancard=userDetails_form.cleaned_data['pancard']
			passport=userDetails_form.cleaned_data['passport']
			dlicense =userDetails_form.cleaned_data['dlicense']
			height =userDetails_form.cleaned_data['height']
			unique_feature =userDetails_form.cleaned_data['unique_feature']
			prev_records  =userDetails_form.cleaned_data['prev_records']

		#convert to json
			userDetailsDict={
				'firstname':firstname,
				'lastname':lastname,
				'dob':dob,
				'placeOfBirth':placeOfBirth,
				'gender':gender,
				'address':address,
				'city':city,
				'country':country,
				'zipcode':zipcode,
				'email':email,
				'aadhar':aadhar,
				'pancard':pancard,
				'passport':passport,
				'dlicense':dlicense,
				'height':height,
				'unique_feature':unique_feature,
				'prev_records':prev_records,
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
	userdetails=request.session.get('userdetails')
	print('classifier',userdetails)
	resp =  sendSMS('MdOytkxZLts-jWl88wbMv3Ch0Og7HiP65DJooZWwye', '9324775077',
    'TXTLCL',"%s %s found at Airoli recently" %(userdetails['firstname'],userdetails['lastname']))
	print (resp)
	return render(request,'app.html',{})

 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
