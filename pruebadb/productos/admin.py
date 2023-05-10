from django.contrib import admin
from common.models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('idproducto', 'nombreproducto', 'rubroproducto',)
    search_fields = ('nombreProducto',)


admin.site.register(Producto, ProductoAdmin)