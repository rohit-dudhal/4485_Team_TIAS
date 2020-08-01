from django.conf.urls import include
from rest_framework import routers
from django.urls import path
from . import views


router=routers.DefaultRouter()
router.register('verify',views.VerifyUserDetails,basename='books')

app_name='operations'
urlpatterns=[
			path('search', views.searchRecords, name='search'),
			path('user/<uuid:userID>',views.recordDetails,name='details'),
			path('api/', include(router.urls))

]
