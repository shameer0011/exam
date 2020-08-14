from . import views

from django.urls import path,include

urlpatterns = [
   
    path('',views.main_page,name='newapp-home'),
    # path('home', views.home1, name='newapp-home1'),
    # path('offer',views.offer),
    # path('product',views.prod),
    # path('cat',views.cat),
    # path('home',views.edit_profile)


]
