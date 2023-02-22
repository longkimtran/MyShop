from django.urls import path
from . import views

urlpatterns =[

    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('term_of_service', views.term_of_service, name='term_of_service'),
    path('register', views.register, name='register'),
    path('manage_admin', views.manage_admin, name='mange_admin'),
    path('manage_product', views.manage_product, name='mange_product'),

]