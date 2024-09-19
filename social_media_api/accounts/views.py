from .models import CustomUser
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserRegisterSerializer, CustomUserLoginSerializer, CustomUserSerializer

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                'username': {
                    'detail': 'User does not exist!',
                },
            }
            userdata = CustomUser.objects.filter(username=request.data['username'])
            if userdata.exists():
                user = CustomUser.objects.get(username=request.data['username'])
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'username': user.username,
                    'email': user.email,
                    'token': token.key
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'user': serializer.data,
                'token': Token.objects.get(user=CustomUser.objects.get(username=serializer.data['username'])).key
            }
            return Response(response, status=status.HTTP_200_OK)
        raise ValidationError(serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)
    
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(
            {
                'success': True,
                'detail': "Logged out!"
            }, status=status.HTTP_200_OK
        )
    
class ProfileUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_update(self, serializer):
        serializer.save()