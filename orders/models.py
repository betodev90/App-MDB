from django.db import models

from core.models import Movie

class Client(models.Model):
    dni = models.CharField(max_length=10, verbose_name='Cédula')
    first_name = models.CharField(max_length=150, verbose_name='Nombre')
    last_name = models.CharField(max_length=150, verbose_name='Apellido')

    def __str__(self):
        return "({}) - {}".format(self.dni, self.last_name)

class Status(models.Model):
    name = models.CharField(verbose_name='Estado', max_length=120)
    description = models.CharField(verbose_name='Descripción', max_length=220, default='', blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    code = models.CharField(max_length=10, verbose_name='Código', unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    date_created = models.DateTimeField(auto_now=True)
    date_updated_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class DetailOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    price = models.FloatField(verbose_name='Precio', default=0.0)
    info = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.order.code, self.movie)

    
