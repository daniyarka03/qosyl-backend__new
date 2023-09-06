from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.tokens import RefreshToken

from main.models import UserAccount
from main.serializers import MyUserCreateSerializer, User, UserSerializerWithToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data

    try:
        user = UserAccount.objects.create(
            avatar=data['avatar'],
            name=data['name'],
            email=data['email'],
            password=make_password(data['password']),
            hobbies=data['hobbies'],
            speciality=data['speciality'],
            study_place=data['study_place'],
        )

        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)

        serializer = MyUserCreateSerializer(user, many=False)
        response_data = serializer.data
        response_data['token'] = token  # Include the token in the response

        return Response(response_data, status=status.HTTP_201_CREATED)
    except Exception as e:
        message = e
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    if request.user.is_authenticated:
        serializer = MyUserCreateSerializer(request.user, many=False)
        return Response(serializer.data)
    else:
        return Response({'message': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def getUsers(request):
    users = UserAccount.objects.all()
    serializer = MyUserCreateSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def updateUser(request):
    user = request.user
    serializer = MyUserCreateSerializer(user, many=False)

    data = request.data
    user.avatar = data['avatar']
    user.name = data['name']
    user.email = data['email']
    user.password = make_password(data['password'])
    user.hobbies = data['hobbies']
    user.speciality = data['speciality']
    user.study_place = data['study_place']
    user.save()

    return Response(serializer.data)


@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
def deleteUser(request):
    user = request.user
    user.delete()
    return Response('User was deleted')

@api_view(['GET'])
def getUser(request, pk):
    user = UserAccount.objects.get(user_id=pk)
    serializer = MyUserCreateSerializer(user, many=False)
    return Response(serializer.data)