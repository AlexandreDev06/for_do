from django.contrib import admin
from django.urls import path, include
from todo_api.views import TodoViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', TodoViewSets, basename='Todo')


urlpatterns = [
    path('admin/', admin.site.urls),
    # Rota ToDo
    path('', include(router.urls)),
]
