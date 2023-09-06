from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import StudentsClub
from main.serializers import StudentsClubSerializer

from rest_framework import status


@api_view(['GET'])
def getStudentsClubs(request):
    clubs = StudentsClub.objects.all()
    serializer = StudentsClubSerializer(clubs, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def addStudentsClub(request):
    data = request.data
    club = StudentsClub.objects.create(
        title=data['title'],
        description=data['description'],
        author_id=data['author_id'],
        related_by_uni=data['related_by_uni'],
        members=data['members'],
        image_src=data['image_src'],
        contact=data['contact'],
    )
    serializer = StudentsClubSerializer(club, many=False)
    return Response(serializer.data)


@api_view(['DELETE', 'GET'])
def deleteStudentsClub(request, pk):
    club = StudentsClub.objects.get(students_club_id=pk)
    club.delete()
    return Response('StudentsClub was deleted')


@api_view(['PUT'])
def updateStudentsClub(request, pk):
    data = request.data
    try:
        club = StudentsClub.objects.get(students_club_id=pk)
    except StudentsClub.DoesNotExist:
        return Response({"detail": "StudentsClub not found."}, status=status.HTTP_404_NOT_FOUND)

    club.title = data.get('title', club.title)  # Provide a default value if 'title' is missing
    club.description = data.get('description', club.description)  # Provide a default value if 'description' is missing
    club.author_id = data.get('author_id', club.author_id)  # Provide a default value if 'author_id' is missing
    club.related_by_uni = data.get('related_by_uni',
                                   club.related_by_uni)  # Provide a default value if 'related_by_uni' is missing
    club.members = data.get('members', club.members)  # Provide a default value if 'members' is missing
    club.image_src = data.get('image_src', club.image_src)  # Provide a default value if 'image_src' is missing
    club.contact = data.get('contact', club.contact)  # Provide a default value if 'contact' is missing

    club.save()

    serializer = StudentsClubSerializer(club, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getStudentsClub(request, pk):
    club = StudentsClub.objects.get(students_club_id=pk)
    serializer = StudentsClubSerializer(club, many=False)
    return Response(serializer.data)
