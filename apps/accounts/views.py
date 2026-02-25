from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer, RegisterSerializer, ResetPasswordSerializer
from .permissions import IsOwnerOrAdmin
from django.contrib.auth import update_session_auth_hash

from rest_framework.views import APIView



class RegisterAPI(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[permissions.AllowAny]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user).data,
            'message': 'User muvaffaqiyatli royhatdan otdi'
        }, status=status.HTTP_201_CREATED
        )


class LoginThrottle(UserRateThrottle):
     rate = '10/min'

class LoginView(ObtainAuthToken):
     throttle_classes = [LoginThrottle]

     def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({'token': response.data['token']})


class LogoutView(generics.GenericAPIView):
    def get_serializer_class(self):
        return None
    
    
class ResetPasswordAPI(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResetPasswordSerializer

    def get_object(self):
        return self.request.user


    def update(self, request, *args, **kwargs):
        user=self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        update_session_auth_hash(request, user) 
        return Response({'message': 'Password updated'}, status=status.HTTP_200_OK)
        