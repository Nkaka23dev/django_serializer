from .views import fn_based_view,cl_based_view
from django.urls import path


urlpatterns = [
     path('',fn_based_view.blog_view),
      path('api/view/',cl_based_view.BlogAPIView.as_view()),
]

