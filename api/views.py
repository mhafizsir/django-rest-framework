from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import TaskSerializer


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    apiUrls = {
        'LIST': '/task-list/',
        'DETAIL_VIEW': '/task-detail/<str:pk>/',
        'CREATE': '/task-create/',
        'UPDATE': '/task-update/<str:pk>/',
        'DELETE': '/task-delete/<str:pk>/',
    }
    return Response(apiUrls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)

    task.delete()

    return Response("Item Deleted")
