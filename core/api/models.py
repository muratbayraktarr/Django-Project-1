from django.db import models

class Not(models.Model):
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
