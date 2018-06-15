from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from todo.models import Task


class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        authorization = Authorization()
        always_return_data = True