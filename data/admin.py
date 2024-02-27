from django.contrib import admin
from .models import *

# Register your models here.
class DataGuruAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'nama', 'jabatan')

    def get_image(self, obj):
        return '<img src="%s" width="100" height="100" />' % obj.image.url
    get_image.short_description = 'Image'
    get_image.allow_tags = True

admin.site.register(DataGuru,DataGuruAdmin)

class AlumniAdminLK(admin.ModelAdmin):
    list_display = ('get_image', 'deskripsi' ,'nama', 'sekolah')

    def get_image(self, obj):
        return '<img src="%s" width="100" height="100" />' % obj.image.url
    get_image.short_description = 'Image'
    get_image.allow_tags = True

admin.site.register(AlumniLK,AlumniAdminLK)

class AlumniAdminPR(admin.ModelAdmin):
    list_display = ('get_image', 'deskripsi' ,'nama', 'sekolah')

    def get_image(self, obj):
        return '<img src="%s" width="100" height="100" />' % obj.image.url
    get_image.short_description = 'Image'
    get_image.allow_tags = True

admin.site.register(AlumniPR,AlumniAdminPR)