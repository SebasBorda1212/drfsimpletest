from django.db import models

class Project(models.Model):  # ✅ nombre con mayúscula
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=50)
    f_creacion = models.DateTimeField(auto_now_add=True)