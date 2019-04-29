from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Task,TaskList
from api.serializers import TaskListSerializer


class ListOfTaskLists(APIView):
    def get(self, request):
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer(tasklists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self , request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskListDetail(APIView):
    def get_task_list(self,pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist as e:
            return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        tasklist = self.get_task_list(pk)
        serializer = TaskListSerializer(tasklist)
        return Response(serializer.data)

    def put(self, request, pk):
        tasklist = self.get_task_list(pk)
        serializer = TaskListSerializer(instance=tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        tasklist = self.get_task_list(pk)
        tasklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
