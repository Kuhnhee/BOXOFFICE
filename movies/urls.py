from django.urls import path
from . import views

app_name = 'articles' # app name 설정

urlpatterns = [
    path('', views.index, name='index'),
]

