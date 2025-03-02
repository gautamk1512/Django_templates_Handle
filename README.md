# Django_templates_Handle

Place home.html Correctly Make sure your template is in the right directory. Inside your Django app, create a templates folder:
myapp/
├── templates/
│   └── home.html

Inside home.html, add something simple to test:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
</head>
<body>
    <h1>Welcome to My Django App!</h1>
</body>
</html>

Update settings.py: Tell Django where to find your templates. In your project folder, open settings.py and add this:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Add this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

Create a View (views.py): In your app’s views.py, create a function to handle the request and render the template:
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

Add URL Routing (urls.py): Now, tell Django what URL should show the home.html template. In your project’s urls.py, add a path:
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Route for the homepage
]

Run the Server: In your terminal, start the development server:
python manage.py runserver

Test in Browser: Open a browser and go to:
http://127.0.0.1:8000/

You should see your home.html content:
Welcome to My Django App!

Handling Dynamic Content: If you want to pass data to your template, you can use Django's context dictionary:
def home(request):
    context = {'name': 'Gautam'}
    return render(request, 'home.html', context)

In your home.html, use template tags to display the data:
<h1>Hello, {{ name }}!</h1>

Would you like to add forms, handle static files, or build a more complex layout with template inheritance? Let me know! 🚀✨
