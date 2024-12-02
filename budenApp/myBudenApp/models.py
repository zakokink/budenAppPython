from datetime import datetime
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Uebungen(models.Model):
    uebung = models.CharField(max_length=100)
    comment = models.CharField(max_length=200, default='', blank=True)
    minWiederholungen = models.IntegerField(null=True, blank=True)
    maxWiederholungen = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.uebung

class Training(models.Model):
    date = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="users")
    uebung = models.ForeignKey(Uebungen, on_delete=models.PROTECT)
    gewicht = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    wiederholungen = models.CharField(max_length=200)
    comment = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return str(self.date)  + ' ' + self.user.name + ' ' + str(self.uebung) + ' ' + str(self.gewicht) + ' ' + str(self.wiederholungen) + ' ' + str(self.comment)

