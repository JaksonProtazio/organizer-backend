from rest_framework.routers import DefaultRouter
from .viewsets import TarefaViewSet

routter = DefaultRouter()
routter.register(r"tarefas", TarefaViewSet)

urlpatterns = routter.urls