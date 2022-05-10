from django.contrib import admin
from .models import Categoria

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoria_nombre',)
    prepopulated_fields = {'slug':('categoria_nombre',)} #Forma de rellenar un campo automaticamente, en este caso el slug

# Register your models here.
admin.site.register(Categoria, CategoryAdmin)
