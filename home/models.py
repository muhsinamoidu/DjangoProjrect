from django.db import models

# Create your models here.
class SignUp(models.Model):
	Name = models.CharField(max_length=20,default='')
	Age=models.IntegerField(default='')
	Email=models.EmailField(default='')
	Password=models.CharField(max_length=12,default='')
	Photo=models.ImageField(upload_to='media/',default='')
