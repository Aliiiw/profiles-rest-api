from django.urls import URLPattern, path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    
]