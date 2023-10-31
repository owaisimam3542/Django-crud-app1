from django.urls import path
from a1 import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('insert',views.insertData,name="insertData"),
    path('update/<uid>',views.updateData,name="updateData"),
    path('delete/<uid>',views.deleteData,name="deleteData"),
]