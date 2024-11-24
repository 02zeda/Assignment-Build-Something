from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class TaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        title = request.data.get("title")
        if not title:
            return Response({"error": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)

        task = Task.objects.create(user=request.user, title=title)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
