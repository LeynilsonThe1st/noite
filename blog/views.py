from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Publicacao, Categoria
from .forms import ComentarioForm, SubscreverForm


# Create your views here.
class TodasPublicacoes(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'publicacoes'
    queryset = Publicacao.objects.filter(condicao=1).order_by('-criado_em')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['subscrever_form'] = SubscreverForm()
        return context

    def post(self, request, *args, **kwargs):
        form = SubscreverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')


class Categorias(ListView):
    template_name = 'blog/categorias.html'
    context_object_name = 'categorias'
    model = Categoria

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publicacoes'] = Publicacao.objects.filter(condicao=1).order_by('-criado_em')
        context['subscrever_form'] = SubscreverForm()
        return context

    def post(self, request, *args, **kwargs):
        form = SubscreverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/categorias')


class ArtigosCategoria(FormMixin, DetailView):
    template_name = 'blog/artigos_por_categoria.html'
    context_object_name = 'categoria'
    model = Categoria
    form_class = SubscreverForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publicacoes'] = get_list_or_404(Publicacao, categoria=context['categoria'])
        context['categorias'] = Categoria.objects.all()
        context['subscrever_form'] = SubscreverForm()
        return context

    def get_success_url(self):
        return reverse('artigos-por-categoria', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        self.form_valid(form) if form.is_valid() else self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def Ver_publicacao(request, slug):
    template_name = 'blog/ver_publicacao.html'
    publicacao = get_object_or_404(Publicacao, slug=slug)

    publicacoes = Publicacao.objects.filter(
        condicao=1,
        categoria=publicacao.categoria
    ).order_by('-criado_em')[:5]

    categorias = Categoria.objects.all()

    comentarios = publicacao.comentarios.filter(activo=True)
    novo_comentario = None

    # Comentario postado
    if request.method == 'POST':
        comentario_form = ComentarioForm(data=request.POST)
        form = SubscreverForm(request.POST)
        if form.is_valid():
            form.save()

        if comentario_form.is_valid():

            novo_comentario = comentario_form.save(commit=False)
            novo_comentario.publicacao = publicacao
            novo_comentario.save()
    else:
        comentario_form = ComentarioForm()

    return render(request, template_name, {
        'publicacoes': publicacoes,
        'categorias': categorias,
        'publicacao': publicacao,
        'comentarios': comentarios,
        'novo_comentario': novo_comentario,
        'comentario_form': comentario_form,
        'subscrever_form': SubscreverForm(),
    })
