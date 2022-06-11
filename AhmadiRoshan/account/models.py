from django.db import models

# Create your models here.
class material(models.Model):
    name=models.CharField(max_length=100)
class Product(models.Model):
    materials=models.ManyToManyField(material,null=True,verbose_name='products',related_name='materials',null=True,blank=True)
class PasteurizationMachine(models.Model):
    MachineName=models.CharField(max_length=100,null=True,blank=True)
    CleaningTime=models.FloatField(null=True,blank=True)
    PerformanceRate=models.FloatField(null=True,blank=True)
    
    
