from rest_framework import serializers
from .models import Project  # coincide con la clase

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'f_creacion')
        read_only_fields = ('f_creacion',)