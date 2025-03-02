# Django Templates Setup

This guide walks you through setting up Django templates, creating views, and routing URLs for your project.

## 📂 **Project Structure**

Make sure your templates are placed correctly inside your app:

```
myapp/
├── templates/
│   └── home.html
```

## 🖼️ **Create a Simple Template (home.html)**

```html
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
```

## ⚙️ **Update settings.py**

Tell Django where to find your templates:

```python
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
```

## 🛠️ **Create a View (views.py)**

Handle the request and render the template:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

## 🛣️ **Add URL Routing (urls.py)**

Define the URL pattern for the homepage:

```python
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Route for the homepage
]
```

## 🚀 **Run the Server**

In your terminal, start the development server:

```bash
python manage.py runserver
```

## 🧭 **Test in Browser**

Open a browser and go to:

```
http://127.0.0.1:8000/
```

You should see:

```
Welcome to My Django App!
```

## 🟠 **Handling Dynamic Content**

Pass dynamic data to your template:

```python
def home(request):
    context = {'name': 'Gautam'}
    return render(request, 'home.html', context)
```

Then use Django template tags to display the data:

```html
<h1>Hello, {{ name }}!</h1>
```

## 🛠️ **What’s Next?**

Would you like to add forms, handle static files, or build a layout with template inheritance? Let me know — I’d love to help you level up your Django app! 🚀✨

