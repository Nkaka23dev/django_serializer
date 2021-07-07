from django.urls import path,include  
from .views.fn_based_view import BlogView 
from .views.cl_based_view import BlogView2


urlpatterns = [
    path('blog/',BlogView),
    path('clb/',BlogView2.as_view())
]