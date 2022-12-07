from rest_framework import serializers
from app.models import File

class FileUploadSerialzer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'desc', 'timestamp')
