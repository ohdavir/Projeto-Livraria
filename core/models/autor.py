from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"