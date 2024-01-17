from django.shortcuts import render

# Create your views here.
def beranda(request):
 return render(request,'view/utama.html')

#  ABOUT 
def profil(request):
 return render(request,'view/about/video.html')

def visimisi(request):
 return render(request,'view/about/visimisi.html')

def developer(request):
 return render(request,'view/about/developer.html')



# Prestasi
def kab(request):
 return render(request,'view/prestasi/kab.html')



# performa
def classmeating(request):
 return render(request,'view/performa/classmeating.html')

def studytour(request):
 return render(request,'view/performa/studytour.html')



# alumni
def alumni(request):
 return render(request,'view/testimonial.html')


# contact
def contact(request):
 return render(request,'view/contact.html')