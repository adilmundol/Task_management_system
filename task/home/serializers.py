from rest_framework import serializers
from .models import Task



class TaskSerializer(serializers.ModelSerializer):
    status_name = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields ='__all__'

    def get_status_name(self, obj):
        return obj.status.status if obj.status else None
    
class TaskSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields =['status']

 
