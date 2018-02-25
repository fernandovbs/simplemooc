from django.urls import path
from simplemooc.courses.views import index, detalhes

app_name = "courses"

urlpatterns = [
    path('', index, name="index"),
    path('detalhes/<int:pk>/', detalhes, name="detalhes")
]