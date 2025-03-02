from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('uan', views.uan, name='uan'),
    path('uan2', views.uan2, name='uan2'),
    path('uan3', views.uan3, name='uan3'),
    path('uan4', views.uan4, name='uan4'),

]
