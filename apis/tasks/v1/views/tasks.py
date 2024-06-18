from rest_framework.viewsets import ModelViewSet

from apis.tasks.models import Task
from apis.tasks.serializers import TaskSerializer


class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(child__isnull=True)
        return super().list(request, *args, **kwargs)
