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