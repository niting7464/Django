from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    
    context = {
         "name" : "nitin",
         "age" : 22,
         "skills": ["python", "django", "react"],
         "user": User(name='John', age=20),
         "blog" : {
             "title": "My Blog",
             "content": "<b> This is my blog content</b>",
             "date": datetime.now(),
         },
         "empty_value": "",
    }
    return render(request, 'blog/home.html', context)

# Create your views here.
