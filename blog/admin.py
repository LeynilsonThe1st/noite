from django.contrib import admin
from .models import Publicacao, Comentario, Categoria, Tag, ViwerEmail


# Register your models here.

admin.sites.AdminSite.site_header = "Painel Administrativo"

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo', 'autor', 'categoria', 'condicao',
        'criado_em', '_comentarios', 'get_tags'
    )

    list_filter = ('condicao', 'autor', 'categoria', 'criado_em')
    search_fields = ['titulo', 'conteudo']
    prepopulated_fields = {'slug': ('titulo',)}

    fieldsets = [
        [None, {"fields": [ ('autor', 'categoria', 'condicao'),
                            ('imagem', 'tag'),
                            ('titulo', 'slug')]}],
        ['Editor de texto do conteudo', { 'fields': [ 'conteudo']}]
    ]

    class Media:
        css = {
            'all': ('blog.css', )
        }

        js = ('tinymce/tinymce.min.js', 'blog.js',)

class PublicacaoInline(admin.TabularInline):
    fieldsets = (
        (None, {
            "fields": ('titulo',),
        }),
    )

    model = Publicacao
    extra = 0


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pequena_descricao')
    fieldsets = (
        (None, {
            "fields": ( 'nome', 'descricao'),
        }),
    )

    inlines = [PublicacaoInline]


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'conteudo', 'publicacao', 'criado_em', 'activo')
    list_filter = ('activo', 'criado_em')
    search_fields = ('nome', 'email', 'conteudo')
    actions = ['aprovar_comentario']

    def aprovar_comentario(self, request, queryset):
        queryset.update(activo=True)


@admin.register(ViwerEmail)
class ViwerEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'criado_em', 'notificado',)
