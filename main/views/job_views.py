from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Job
from main.serializers import JobSerializer

from rest_framework import status


@api_view(['GET'])
def getJobs(request):
    # return HttpResponse('Hello')
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def addJob(request):
    data = request.data
    project = Job.objects.create(
        project_id=data['project_id'],
        title=data['title'],
        description=data['description'],
        work_format=data['work_format'],
        responsibility=data['responsibility'],
        requirements=data['requirements'],
        we_offer=data['we_offer'],
    )
    serializer = JobSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['DELETE', 'GET'])
def deleteJob(request, pk):
    job = Job.objects.get(job_id=pk)
    job.delete()
    return Response('Job was deleted')


@api_view(['PUT'])
def updateJob(request, pk):
    data = request.data
    try:
        job = Job.objects.get(job_id=pk)
    except Job.DoesNotExist:
        return Response({"detail": "Job not found."}, status=status.HTTP_404_NOT_FOUND)

    job.project_id = data.get('project_id', job.project_id)
    job.title = data.get('title', job.title)  # Provide a default value if 'title' is missing
    job.description = data.get('description', job.description)  # Provide a default value if 'description' is missing
    job.work_format = data.get('work_format', job.work_format)  # Provide a default value if 'work_format' is missing
    job.responsibility = data.get('responsibility', job.responsibility)  # Provide a default value if 'responsibility' is missing
    job.requirements = data.get('requirements', job.requirements)  # Provide a default value if 'requirements' is missing
    job.we_offer = data.get('we_offer', job.we_offer)  # Provide a default value if 'we_offer' is missing


    job.save()

    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getJob(request, pk):
    job = Job.objects.get(job_id=pk)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)