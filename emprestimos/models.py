from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
    nome = models.CharField("Nome",max_length=150)
    email = models.EmailField("Email")
    data_cadastro = models.DateField("Data de cadastro")

class Livros(models.Model):
    titulo = models.CharField("Titulo",max_length=150)
    descricao = models.CharField("Descrição",max_length=200)
    editora = models.CharField("Editora",max_length=150)
    status = models.
    imagem =  models.ImageField("Imagem", upload_to='imagens', null=True, blank=True)
    data_cadastro = models.DateField("Data de cadastro")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = 'Livros'

class Emprestimo(models.Model):
    codigo = models.AutoField("Codigo", primary_key=True, unique=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_emprestimo = models.DateField("Data de emprestimo")
    data_devolucao = models.DateField("Data de devolução")
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE, verbose_name="Autor")

class Perfil(models.Model):
    nome = models.CharField("Nome",max_length=150)
    email = models.EmailField("Email")
    avatar = models.
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)


