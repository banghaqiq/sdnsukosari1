from django.urls import path
from . import views

urlpatterns = [
 path('', views.beranda, name='home'),

#  ABOUT
 path('profile/', views.profil, name='profile'),
 path('vm/', views.visimisi, name='visimisi'),
 path('developer/', views.developer, name='developer'),

#  Performa
 path('classmeating/', views.classmeating, name='classmeating'),
 path('studytour/', views.studytour, name='studytour'),


#  path('testimonial/', views.alumni, name='testimonial'),
 path('contact/', views.contact, name='contact'),
]