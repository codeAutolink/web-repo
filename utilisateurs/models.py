from django.db import models
from django.contrib.auth.models import User

class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.TextField()  # ceci stockera le token chiffré
    url = models.URLField(max_length=500)  # Ceci est le champ URL ajouté
    def __str__(self):
        return self.name
    
class Scenario(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

 

class SSHKey(models.Model):
    key = models.TextField(help_text="Clé SSH")
    username = models.CharField(max_length=255, help_text="Nom d'utilisateur SSH")
    ip = models.GenericIPAddressField(help_text="Adresse IP de la machine distante")
    port = models.PositiveIntegerField(default=22, help_text="Port SSH (par défaut à 22)")
    
    def __str__(self):
        return f"{self.username}@{self.ip}:{self.port}"
    
 