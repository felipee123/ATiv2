from django.contrib import admin # type: ignore
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Produto)
class ProtudoAdmin(admin.ModelAdmin):
    list_display = ('nome' , 'preco' , 'categoria')
    list_filter = ('categoria',)
    list_editable = ('preco', )
    list_display_links = ('nome', )
    search_fields= ('nome', 'descricao')