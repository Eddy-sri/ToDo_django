from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/delete/',views.delete, name = 'delete'),
    path('create/', views.create, name = "create")

]