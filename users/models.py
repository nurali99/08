from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls.base import reverse, reverse_lazy
# Create your models here.
class CustomUser(AbstractUser):
  age=models.PositiveIntegerField(null=True, blank=True)
  address=models.CharField(max_length=100)
  job=models.CharField(max_length=50)

class Post(models.Model):
  title=models.CharField(max_length=200)
  rasm=models.ImageField(upload_to='images/', blank=True)
  body=models.TextField()
  time=models.DateTimeField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post_detail', args=[str(self.id)])