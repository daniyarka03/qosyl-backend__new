from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
import requests
from .models import Post
from .models import Project
from .models import UserAccount
from .serializers import ProjectSerializer, PostSerializer, MyUserCreateSerializer, User, UserSerializerWithToken

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
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
    #
    #     # Add custom claims
    #     token['email'] = user.email
    #     token['message'] = 'Hello world'
    #     # ...
    #
    #     return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data

    try:
        user = UserAccount.objects.create(
            name=data['name'],
            email=data['email'],
            password=make_password(data['password']),
            token=data['token']
        )


        serializer = MyUserCreateSerializer(user, many=False)
        return Response(serializer.data)  # Return the serialized data using .data
    except:
        message = {'detail': 'User with this email already exists'}
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

@api_view(['GET'])
def getPosts(request):
    # return HttpResponse('Hello')
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def addPost(request):
    post = PostSerializer(data=request.data)

    # if Post.objects.filter(user_id=request.data['post_id']).exists():
    #     return Response({'message': 'User already exists'})

    if post.is_valid():
        post.save()
        return Response(post.data)
    else:
        return Response(post.errors)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)




#

#
#
# @api_view(['DELETE', 'GET'])
# def deletePost(request, pk):
#     post = Post.objects.get(post_id=pk)
#     post.delete()
#     return Response('Post was deleted')
#
# @api_view(['PUT', 'GET'])
# def updatePost(request, pk):
#     post = Post.objects.get(post_id=pk)
#     serializer = PostSerializer(instance=post, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
# # @api_view(['GET'])
# # def getProjects(request):
# #     return Response(projects)
# #
# # @api_view(['GET'])
# # def getProducts(request):
# #     return Response(products)
#
#
# # @api_view(['GET'])
# # def getProduct(request, pk):
# #     product = None
# #     for i in products:
# #         if i['_id'] == pk:
# #             product = i
# #             break
# #     return Response(product)
#
