from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests
from .models import Post
from .models import Project
from .serializers import ProjectSerializer, PostSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['email'] = self.user.email
        data['name'] = self.user.name

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

def get_user_data(request):
    jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyMjkwNDIwLCJpYXQiOjE2OTIyOTAxMjAsImp0aSI6ImMzMTI4M2ZjOTViYzRiMDlhOGU1ZTVmOTUyOTkxNjY2IiwidXNlcl9pZCI6OH0.V-ydE8l3jRYtnqaDa1dY9W8MnLShG9BhVUmVD7HL4vc"
    headers = {
        'Authorization': f'JWT {jwt_token}',
    }

    response = requests.get('http://localhost:8000/auth/users/me/', headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        return JsonResponse(user_data)
    else:
        return JsonResponse({'error': 'Failed to retrieve user data'}, status=response.status_code)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/users/',
        '/api/users/create/',
        '/api/users/<update>/<id>/',
        '/api/users/delete/<id>/',

        '/api/projects/',
        '/api/projects/create/',
        '/api/projects/<update>/<id>/',
        '/api/projects/delete/<id>/',

        '/api/jobs/',
        '/api/jobs/create/',
        '/api/jobs/<update>/<id>/',
        '/api/jobs/delete/<id>/',

        '/api/posts/',
        '/api/posts/create/',
        '/api/posts/<update>/<id>/',
        '/api/posts/delete/<post_id>/',
    ]

    return Response(routes)


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


def example_view(request):
    default_message = 'Hello World'
    return HttpResponse(default_message)

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
