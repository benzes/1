from django.urls import path, include
from main.views import GetView

urlpatterns = [
    path('', GetView),
]