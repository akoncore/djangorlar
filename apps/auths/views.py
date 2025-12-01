from rest_framework import viewsets,status,permissions
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import  RefreshToken
from rest_framework.response import Response

from django.contrib.auth import login

from .models import CustomUser
from .serializers import (
   RegisterSerializer,
   LoginSerializer,
   UserProfileSerializer
)

class RegisterView(viewsets.ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self,request,*args,**kwargs):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user =  serializer.save()
    
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
            'message':'Register OK'
        },status=status.HTTP_200_OK)
        

class LoginView(viewsets.ViewSet):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self,request,*args,**kwargs):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        login(request,user)
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
            'message':'Login OK'
        },status=status.HTTP_200_OK)
        
        
