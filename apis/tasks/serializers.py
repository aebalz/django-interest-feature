from rest_framework import serializers

from apis.tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['childs'] = TaskSerializer(instance.task_set.all(), many=True).data
        return data