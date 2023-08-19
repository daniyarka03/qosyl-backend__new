from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
import requests
from main.models import Project
from main.serializers import ProjectSerializer

from rest_framework import status


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(project_id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createProject(request):
    data = request.data
    project = Project.objects.create(
        title=data['title'],
        description=data['description'],
        image_src=data['image_src'],
        type=data['type'],
        contact=data['contact']
    )
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteProject(request, pk):
    project = Project.objects.get(project_id=pk)
    project.delete()
    return Response('Project was deleted')


@api_view(['PUT'])
def updateProject(request, pk):
    data = request.data
    project = Project.objects.get(project_id=pk)

    project.title = data['title']
    project.description = data['description']
    project.image_src = data['image_src']
    project.type = data['type']
    project.contact = data['contact']

    project.save()

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
