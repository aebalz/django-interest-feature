from rest_framework import routers
from django.urls import path, include
from apis.tasks.v1.views import tasks


# ===================== /api/v1/ =====================
router = routers.DefaultRouter()
router.register(r'tasks', tasks.TaskModelViewSet)

api_v1_urls = (router.urls, 'v1_tasks')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
