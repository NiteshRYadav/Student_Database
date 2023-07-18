from django.db import models

from django.utils.text import slugify

# Create your models here.

class Studentdata(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=30)
    Phone=models.CharField(max_length=20)
    
    slug=models.SlugField(default='',null=False)
    
    
    
    
    def __str__(self):
        return f"{self.Name},{self.Email},{self.Phone},{self.slug}"
    
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.Name)
        
        return super().save(*args,**kwargs)
