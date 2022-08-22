from django.db import models

class  Marca(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')

    class Meta:
        db_table = 'marca'

    def __str__(self):
        return self.nombre

class  Auto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    color = models.CharField(max_length=100, verbose_name='Color')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca')

    class Meta:
        db_table = 'auto'

    def __str__(self):
        return self.nombre
