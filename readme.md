
# Timetable Generation System

The Timetable Generation System is a web-based application built with Django, HTML, CSS (using Tailwind CSS), and JavaScript. It allows users to generate timetables for different levels (ND1, ND2, HND1, HND2) and semesters (first semester, second semester) automatically from a JSON dataset of courses.

## Features

- Generate timetables for ND1, ND2, HND1, and HND2 levels.
- Select between first semester and second semester.
- Display courses on each day of the week, starting from 8 AM and ending by 12 PM or 2 PM.
- Include a break from 12 PM to 1 PM.
- Repeat important courses or tag them as "Practical" from 1 PM to 2 PM.

## Requirements

- Python 3.x
- Django
- Tailwind CSS

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/timetable-generation-system.git
```

2. Install dependencies:

```
pip install django
```

3. Run the Django server:

```
python manage.py runserver
```

4. Visit `http://127.0.0.1:8000/` in your web browser.

## Usage

1. Select the semester from the dropdown menu.
2. Timetables for ND1, ND2, HND1, and HND2 levels will be generated automatically.
3. Each day's timetable will display courses from 8 AM to 12 PM with a break from 12 PM to 1 PM.
4. Optionally, repeat important courses or tag them as "Practical" from 1 PM to 2 PM.

## JSON Data

Ensure that the JSON dataset of courses (`courses.json`) is correctly structured with courses categorized by level and semester.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
