from django.shortcuts import render

# Create your views here.
def beranda(request):
 return render(request,'view/utama.html')

#  ABOUT 
def profil(request):
 return render(request,'view/about/video.html')

def visimisi(request):
 return render(request,'view/about/visimisi.html')

def performa(request):
 return render(request,'view/performance.html')

def alumni(request):
 return render(request,'view/testimonial.html')