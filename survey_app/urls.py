from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('result/<str:yourName>/<str:yourLocation>/<str:yourLanguage>/<str:yourComments>', views.result)
]