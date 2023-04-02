from django.urls import path, re_path

from .views import TodasPublicacoes, Ver_publicacao, Categorias, ArtigosCategoria

urlpatterns = [
    path('', TodasPublicacoes.as_view(), name='index'),
    path('categorias/', Categorias.as_view(), name='categorias'),
    path('categorias/<int:pk>/', ArtigosCategoria.as_view(), name='artigos-por-categoria'),
    path('<slug:slug>/', Ver_publicacao, name='ver-publicacao' ),
]

# path('<slug:pagina>/', Subscrever.as_view(), name='subscrever')
# re_path(r"^subscrever/(?P<pagina>[./a-zA-Z]+)/$", Subscrever.as_view(), name='subscrever')
# r"^(subscrever?P<pagina>[-a-zA-Z]+)/$"