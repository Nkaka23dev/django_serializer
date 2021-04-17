from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import ObtainAuthToken


router=routers.DefaultRouter()
router.register('users',views.UserView)

urlpatterns=[
    path('',include(router.urls)),
    path('auth/',ObtainAuthToken.as_view())
]

