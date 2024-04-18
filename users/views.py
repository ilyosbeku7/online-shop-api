from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from.serializers import LoginSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.response import Response

from .serializers import UserSerializer
# Create your views here.

class LodinApiView(APIView):
    def post(self, request):
        data=request.data
        serializer=LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user=authenticate(username=serializer.data['username'], password=serializer.data['password'])

        if user is None:
            data={
                'status': False,
                'message': "User not found"
            }
            return Response (data)
        refresh=RefreshToken.for_user(user)

        data={
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
        return Response (data)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'},
                            status=HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=HTTP_400_BAD_REQUEST)