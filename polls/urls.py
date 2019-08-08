from django.urls import path
from . import views,api

urlpatterns = [
    path('index',views.index,name='index'),
    path('index1', views.index1, name='index1'),
    path('Api', views.Api, name='Api'),
    path('login', views.index2, name='login2'),
    # path('login', views.index2, name='login2'),
    path('login11', api.question_list, name='login2'),

]