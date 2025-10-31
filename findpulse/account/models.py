from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Perfil(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="perifl")
    nome = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    email = models.EmailField(null=True, blank=True)
    contacto = models.CharField(max_length=9)
    creado_em = models.DateTimeField(auto_now_add=True)
    cidade = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='perfl/', blank=True)

    def __str__(self):
        return f"{self.nome} de {self.owner.username}"

@receiver(post_save, sender=User)
def criar_atualizar_perfil(sender, instance, created, **kwargs):
    if created:
            Perfil.objects.create(owner=instance)
    else:
        instance.perfil.save()
        
class Status(models.Model):
    cliente = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name="status")
    ultimo_pulso = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    logintude = models.FloatField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
         return f"{self.cliente} de {self.activo}"