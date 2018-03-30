from django.urls import path
from simplemooc.courses.views import index, detalhes

app_name = "courses"

urlpatterns = [
    path('', index, name="index"),
    path('detalhes/<slug:slug>/', detalhes, name="detalhes")
]

app_name = "courses"

urlpatterns = [
    path('', index, name="index"),
    path('detalhes/<slug:slug>/', detalhes, name="detalhes")
]