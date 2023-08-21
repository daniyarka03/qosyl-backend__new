from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
import requests
from main.models import Post
from main.serializers import PostSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status


@api_view(['GET'])
def getPosts(request):
    # return HttpResponse('Hello')
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def addPost(request):
    data = request.data
    project = Post.objects.create(
        content=data['content'],
        author_name=data['author_name'],
        author_id=data['author_id']
    )
    serializer = PostSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['DELETE', 'GET'])
def deletePost(request, pk):
    post = Post.objects.get(post_id=pk)
    post.delete()
    return Response('Post was deleted')


@api_view(['PUT'])
def updatePost(request, pk):
    data = request.data
    try:
        post = Post.objects.get(post_id=pk)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

    post.content = data['content']
    post.author_name = data['author_name']
    post.author_id = data['author_id']
    post.save()

    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getPost(request, pk):
    post = Post.objects.get(project_id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)
