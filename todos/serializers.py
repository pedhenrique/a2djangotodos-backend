from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Todo
        fields = ('url', 'id', 'text', 'is_completed', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    todos = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'todos')