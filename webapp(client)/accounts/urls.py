from django.urls import path
from . import views


app_name='accounts'
urlpatterns=[
			path('register', views.register, name='register'),
			path('',views.login,name='login'),
			path('login', views.login, name='login'),
			path('logout', views.logout, name='logout'),
			path('userdetails', views.userDetailsView, name='userdetails'),
			path('classifier', views.classifier, name='classifier'),
			path('success', views.success, name='success'),

]
