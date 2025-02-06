from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    task_id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=500)
    status = serializers.CharField(default="pending")
