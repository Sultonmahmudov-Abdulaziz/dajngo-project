from django.db import models

# Create your models here.


class Shaharlar(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='shaharlar/')
    text=models.TextField(max_length=900)
    category=models.ForeignKey('Category' ,on_delete=models.CASCADE)
    airveys=models.ManyToManyField('Airveys', blank=True ,null=True)



    class Meta:
        verbose_name = 'shahar'
        verbose_name_plural ='shaharlar'


    def __str__(self):
        return  self.name
    


class Category(models.Model):
    name=models.CharField(max_length=255)


    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'



    def __str__(self):
        return  self.name
    

class Airveys(models.Model):
    name=models.CharField(max_length=255)


    class Meta:
        verbose_name = 'Samalyot'
        verbose_name_plural = 'Samalyotlar'



    def __str__(self):
        return  self.name