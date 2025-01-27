from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="user/", blank=True, null=True)
    bio = models.TextField(null=True, blank=True)

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classes = [
        ("Comunidade", "Comunidade"),
  ("Bug", "Bug"),
        ("Dark", "Dark"),
        ("Dragon", "Dragon"),
        ("Electric", "Electric"),
        ("Fairy", "Fairy"),
        ("Fighting", "Fighting"),
        ("Fire", "Fire"),
        ("Flying", "Flying"),
        ("Ghost", "Ghost"),
        ("Grass", "Grass"),
        ("Ground", "Ground"),
        ("Ice", "Ice"),
        ("Normal", "Normal"),
        ("Poison", "Poison"),
        ("Psychic", "Psychic"),
        ("Rock", "Rock"),
        ("Steel", "Steel"),
        ("Water", "Water"),
]
    foto = models.ImageField(upload_to='', blank=True, null=True)

    nome = models.CharField(max_length=50)
    defesa = models.IntegerField()
    ataque = models.IntegerField()
    hp = models.IntegerField()
    descricao = models.TextField()
    classe = models.CharField(choices=classes, max_length=50)
    
    def __str__(self):
        return self.nome
