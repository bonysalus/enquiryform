from django.contrib import admin
from django.urls import path
from . import views
app_name ='enquiryapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),

]
