from .serializer import ToDoSerializer
from rest_framework import viewsets
from .models import ToDo


class TodoViewSets(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer