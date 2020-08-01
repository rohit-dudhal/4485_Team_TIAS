from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm, UserDetailsForm,UserImagesForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserImages
from django.forms import modelformset_factory


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
					return redirect('accounts:login')

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
	ImageFormSet = modelformset_factory(UserImages, form=UserImagesForm, extra=3)
	if request.method=="POST":
		userDetails_form =UserDetailsForm(request.POST)
		userImage_form =ImageFormSet(request.POST, request.FILES,queryset=UserImages.objects.none())
		if  userDetails_form.is_valid():
			fname=userDetails_form.cleaned_data['fname']
			lname=userDetails_form.cleaned_data['lname']
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
			dlicense =userDetails_form.cleaned_data['dlicense ']
			height =userDetails_form.cleaned_data['height']
			unique_feature =userDetails_form.cleaned_data['unique_feature']
			prev_records  =userDetails_form.cleaned_data['prev_records']
			userDetails_form.save()
			for form in userImage_form.cleaned_data:
				image = form['image']
				photo = Images(post=post_form, image=image)
				photo.save()
			return redirect('/')


	else:
		userDetails_form =UserDetailsForm()
		userImage_form = ImageFormSet(queryset=UserImages.objects.none())
    

	context={
				'userDetails_form':userDetails_form,
				'userImage_form':userImage_form
	}
	return render(request,template_name,context)
