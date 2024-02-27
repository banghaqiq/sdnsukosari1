from django.db import models

# Create your models here.
class DataGuru(models.Model):
    image = models.ImageField(upload_to='images/')
    nama = models.CharField(max_length=100,null=True, blank=True)
    jabatan = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural="Data Guru"