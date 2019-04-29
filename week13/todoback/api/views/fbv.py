from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  status
from api.models import Task,TaskList
from api.serializers import TaskListSerializer


@api_view(['GET', 'POST'])
def task_list (request) :
    if request.method == 'GET':
        taskLists = TaskList.objects.all()
        serializer = TaskListSerializer(taskLists, many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer=TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response()


@api_view(['GET', 'PUT', 'DELETE'])
def task_list_detail(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskListSerializer(tasklist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance=tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        tasklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# def task_get (request, pk):
#     taskLists = TaskList.objects.all()
#     tasks = []
#     for i in range(pk):
#         tasks.append(taskLists[i])
#     json_tasks = [t.to_json() for t in tasks]
#     return JsonResponse(json_tasks, safe=False)


