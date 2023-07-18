from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('/',views.index,name='index'),
    
    path("<slug:s>",views.details,name='std-msg'),
]
