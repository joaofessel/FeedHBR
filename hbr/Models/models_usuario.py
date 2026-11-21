from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=120,blank=False, null = False)
    email = models.CharField(max_length=120, blank=False, null = False)
    celular = models.CharField(max_length=120, blank=False, null= False)
    login = models.CharField(max_length=120, blank=False, null= False)
    senha = models.CharField(max_length=120, blank=False, null= False)
    criado_em = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True, blank= False)
    id = models.BigAutoField(primary_key = True)