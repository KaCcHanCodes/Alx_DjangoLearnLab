from .models import CustomUser
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserRegisterSerializer, CustomUserLoginSerializer

class UserLoginView(APIView):
    def post(self, request):
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
                    'token': token.key,
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserRegisterView(APIView):
    pass