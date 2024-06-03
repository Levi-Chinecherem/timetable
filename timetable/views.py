from django.shortcuts import render
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def timetable_view(request):
    json_path = os.path.join(os.path.join(BASE_DIR, 'static/courses.json'))
    with open(json_path, 'r') as file:
        courses = json.load(file)
    return render(request, 'timetable.html', {'courses': json.dumps(courses)})
