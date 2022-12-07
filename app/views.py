from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response 
from rest_framework import status

from .serializers import FileUploadSerialzer


class FileUploadView(APIView):
    parser_class = (FileUploadParser, )


    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerialzer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
