from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings


from Security.models import CustomUser

def index(request):
        ReturningData = dict()
        return render(request,"UI/index.html",ReturningData); 



def docs(request):
        ReturningData = dict()
        return render(request,"UI/docs.html",ReturningData); 

def courses(request):
        ReturningData = dict()
        return render(request,"UI/courses.html",ReturningData); 

def connect(request):
        ReturningData = dict()
        return render(request,"UI/connect.html",ReturningData); 

def tutorials(request):
        ReturningData = dict()
        return render(request,"UI/tutorials.html",ReturningData); 

def resume(request):
        ReturningData = dict()
        return render(request,"UI/resume.html",ReturningData); 




def about(request):
        ReturningData = dict()
        return render(request,"UI/about.html",ReturningData); 

def contact(request):
        ReturningData = dict()
        return render(request,"UI/contact.html",ReturningData); 

def help(request):
        ReturningData = dict()
        return render(request,"UI/help.html",ReturningData); 

def terms_and_conditions(request):
        ReturningData = dict()
        return render(request,"UI/terms-and-conditions.html",ReturningData); 




def error_404(request):
        ReturningData = dict()
        return render(request,"UI/error/404.html",ReturningData); 

def error_server(request):
        ReturningData = dict()
        return render(request,"UI/error/server.html",ReturningData); 

def error_under_maintenance(request):
        ReturningData = dict()
        return render(request,"UI/error/under-maintenance.html",ReturningData); 




def careers(request):
        ReturningData = dict()
        return render(request,"UI/careers.html",ReturningData); 

def explore(request):
        ReturningData = dict()
        return render(request,"UI/explore.html",ReturningData); 

def blogs(request,blog_slug=None):
        ReturningData = dict()
        return render(request,"UI/blogs.html",ReturningData); 




def profile(request):
        ReturningData = dict()
        return render(request,"UI/profile.html",ReturningData); 

def notifications(request):
        ReturningData = dict()

        ReturningData = {
            "paths" : [
                {
                    "url" : "/profile/",
                    "name" : "User",
                    "activate" : True
                },
                {
                    "url" : "/notifications/",
                    "name" : "Notifications",
                    "activate" : False
                }
                ]        
        }
        
        return render(request,"UI/notifications.html",ReturningData); 


def users_list(request):
        ReturningData = dict()
        return render(request,"UI/users-list.html",ReturningData); 

def default_user(request):
        ReturningData = dict()

        users = CustomUser.objects.all()
        print(users)

        ReturningData = {
                "paths" : [
                        {
                                "url" : "/security/",
                                "name" : "Security",
                                "activate" : True
                        },
                        {
                        "url" : "/default-user/",
                        "name" : "Default User",
                        "activate" : False
                        }
                ],
                'users' : users
        }
        
        return render(request,"UI/default-user.html",ReturningData); 

def asked_questions(request):
        ReturningData = dict()
        return render(request,"UI/asked-questions.html",ReturningData); 













        """
        
    path('docs/', views.docs, name='docs'),
    path('courses/', views.courses, name='courses'),
    path('connect/', views.connect, name='connect'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('resume/', views.resume, name='resume'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions'),

    path('404-error/', views.error_404, name='error_404'),
    path('server-error/', views.error_server, name='error_server'),
    path('under-maintenance/', views.error_under_maintenance, name='error_under_maintenance'),

    

    path('career/', views.career, name='career'),
    path('explore/', views.explore, name='explore'),
    path('blogs/', views.blogs, name='blogs'),

    
    path('profile/', views.profile, name='profile'),
    path('notifications/', views.notifications, name='notifications'),
    path('users-list/', views.users_list, name='users_list'),
    path('default-user/', views.default_user, name='default_user'),
    path('asked-questions/', views.asked_questions, name='asked_questions'),


        """






def tutorials(request, skills='python',slugs=None):
    
    if slugs:
            return render(request, 'tutorials/open-up.html')
    
    return render(request, 'tutorials/landing-page.html')