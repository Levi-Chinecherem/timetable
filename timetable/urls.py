from django.urls import path
from .views import timetable_view

urlpatterns = [
    path('', timetable_view, name='timetable'),
]
