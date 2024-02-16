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

def struktur(request):
 return render(request,'view/about/struktur.html')

def datasiswa(request):
 return render(request,'view/about/datasiswa.html')





# Prestasi
def kec(request):
 return render(request,'view/prestasi/kec.html')
def kab(request):
 return render(request,'view/prestasi/kab.html')
def prov(request):
 return render(request,'view/prestasi/prov.html')
def nas(request):
 return render(request,'view/prestasi/nas.html')





# performa
def penampilan(request):
 return render(request,'view/performa/penampilan.html')
def drumband(request):
 return render(request,'view/performa/drumband.html')
def keagamaan(request):
 return render(request,'view/performa/keagamaan.html')
def classmeating(request):
 return render(request,'view/performa/classmeating.html')
def studytour(request):
 return render(request,'view/performa/studytour.html')






# alumni
def alumni(request):
 return render(request,'view/testimonial.html')

# informasi
def berita(request):
 return render(request, 'view/informasi/berita.html')
def pengumuman(request):
 return render(request, 'view/informasi/pengumuman.html')
def extrakulikuler(request):
 return render(request, 'view/informasi/extra.html')


# contact
def contact(request):
 return render(request,'view/contact.html')