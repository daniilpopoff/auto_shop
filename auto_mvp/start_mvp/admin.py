from django.contrib import admin
from . import models
# Register your models here.\
admin.site.register(models.CarAnnouncement)
admin.site.register(models.Category)




# пока еще не решил зачем этот код но он был в на stackoverflow
# для того чтобы выводить цвет машины через html
# class CarAdmin(admin.ModelAdmin):
#     list_display = ('name_car', 'color', 'colored_name')