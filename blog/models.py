from django.db import models
from django.contrib.auth.models import User
from random import randint as rdi


# Create your models here.

CONDICAO = (
    (0, "Rascunho"),
    (1, "Publicar")
)


class Categoria(models.Model):
    publicacoes = models.ForeignKey(
        "blog.publicacao",
        on_delete=models.CASCADE,
        related_name='publicacoes'
    )
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()

    def pequena_descricao(self):
        return " ".join(self.descricao.split()[:5])

    def __str__(self):
        return self.nome


class Publicacao(models.Model):
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='publicacoes'
    )

    tag = models.ManyToManyField(
        'blog.Tag',
        related_name='publicacoes'
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=200, unique=True)
    titulo = models.CharField(max_length=200, unique=True)
    conteudo = models.TextField()
    condicao = models.IntegerField('Condição', choices=CONDICAO, default=0)
    criado_em = models.DateTimeField('Data de criação', auto_now_add=True)
    modificado_em = models.DateTimeField('Ultima alteração', auto_now=True)

    def _comentarios(self):
        return self.comentarios.count()

    def get_tags(self):
        return list(self.tag.all())

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo


class Tag(models.Model):
    # Publicacao = models.ManyToManyField("blog.publicacao", related_name="publicacao")
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


class Comentario(models.Model):
    publicacao = models.ForeignKey(
        "blog.publicacao",
        on_delete=models.CASCADE,
        related_name='comentarios'
    )

    nome = models.CharField(max_length=80)
    email = models.EmailField()
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=False)

    class Meta:
        ordering = ['criado_em']

    def __str__(self):
        return f'Comentário de {self.nome}: {self.conteudo}'


class ViwerEmail(models.Model):
    email = models.EmailField()
    criado_em = models.DateTimeField('Data de criação', auto_now_add=True)
    notificado = models.BooleanField(default=False)
