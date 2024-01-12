from django.urls import path
from . import views

urlpatterns = [
 path('', views.beranda, name='home'),
 path('profile/', views.profil, name='profile'),
 path('vm/', views.visimisi, name='visimisi'),
 path('performance/', views.performa, name='performance'),
#  path('testimonial/', views.alumni, name='testimonial'),
]