from django.shortcuts import render
from rest_framework import views
from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework.response import Response

# Create your views here.
class RegisterView(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Success"})
        else:
            print(serializer.errors)
            return Response(serializer.errors, status = 400)