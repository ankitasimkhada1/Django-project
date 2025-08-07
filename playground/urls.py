

from django.urls import path
from playground import views
from  . import views
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    ...
]

# Debug toolbar URL
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns


urlpatterns = [
    path('', views.say_hello),
    path('hello/', views.say_hello),
    
]

# urlpatterns = [
#     path('hello/', views.say_hello, name='hello'),  # for /playground/hello/
#     path('', views.say_hello, name='home'),        # for /playground/
# ]

