from django.db import models

# Create your models here.

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie= models.CharField(max_length=10)
    date = models.DateField()
    def __str__(self):
        return str(self.movie)

class Geust(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return str(self.name)


class Reservation(models.Model):
    geust= models.ForeignKey(Geust,on_delete=models.CASCADE,related_name='reservation')
    
    movie= models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reservation')


    def __str__(self):
        return str(self.movie)