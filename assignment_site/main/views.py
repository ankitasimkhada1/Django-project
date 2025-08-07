
# from django.shortcuts import render

# def home(request):
#     context = {
#         'title': 'Welcome to Home Page',
#         'name': 'Ankita'
#     }
#     return render(request, 'home.html', context)

# def about(request):
#     context = {
#         'title': 'About Us',
#         'description': 'This is a Django project for your assignment.'
#     }
#     return render(request, 'about.html', context)

# # Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html', {'title': 'Home'})

def about(request):
    courses = [
        {'name': 'BBA', 'fee': '60,000+', 'seats': 90},
        {'name': 'BBA-F', 'fee': '60,000+', 'seats': 90},
        {'name': 'BIM', 'fee': '60,000+', 'seats': 60},
        {'name': 'BBM', 'fee': '60,000+', 'seats': 70},
        {'name': 'MBS', 'fee': '80,000+', 'seats': 'N/A'},
        {'name': 'MBA', 'fee': '80,000+', 'seats': 'N/A'},
    ]
    return render(request, 'main/about.html', {'title': 'About', 'courses': courses})
