from django.db import models


class Obrazek(models.Model):
    licznik = models.IntegerField(default = 0)
    nazwa = models.CharField(max_length = 200)
    source = models.CharField(max_length = 200, default='')
    #zdjecie = models.ImageField()

    def glosuj(self):
        self.licznik += 1
        self.save()

    def __str__(self):
        return self.nazwa
