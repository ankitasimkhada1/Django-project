
# from django.contrib import admin
# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('main.urls')),  # Add this line
# ]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]