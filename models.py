from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)    
    description = models.TextField()
    phone = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True, blank=True)
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='usuario')
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #quem foi que criou,tem na tabela do django, é só importar

 
def __str__(self):
        return str(self.id)

#nome da tabela do banco

class Meta:
        db_table = 'usuario'
