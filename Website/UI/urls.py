from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('index',views.index,name='index'),
    
    path('docs/', views.docs, name='docs'),
    path('courses/', views.courses, name='courses'),
    path('connect/', views.connect, name='connect'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('resume/', views.resume, name='resume'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions'),

    path('error/404/', views.error_404, name='error_404'),
    path('error/server/', views.error_server, name='error_server'),
    path('error/under-maintenance/', views.error_under_maintenance, name='error_under_maintenance'),

    

    path('careers/', views.careers, name='careers'),
    path('explore/', views.explore, name='explore'),
    path('profile/', views.profile, name='profile'),




    
    path('profile/', views.profile, name='profile'),
    path('notifications/', views.notifications, name='notifications'),
    # path('users-list/', views.users_list, name='users_list'),
    path('security/users-list/', views.users_list, name='users_list'),
    # path('default-user/', views.default_user, name='default_user'),
    path('security/default-user/', views.default_user, name='default_user'),
    # path('asked-questions/', views.asked_questions, name='asked_questions'),
    path('security/asked-questions/', views.asked_questions, name='asked_questions'),


    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<str:blog_slug>', views.blogs, name='blogs'),





    
    path('tutorials/', views.tutorials, name='tutorials'),
    path('tutorials/<str:skills>/', views.tutorials, name='tutorials'),
    path('tutorials/<str:skills>/<str:slugs>/', views.tutorials, name='tutorials'),





]



"""

    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),

    path('career/', views.career, name='career'),
    path('career/posting/', views.career_posting, name='career-posting'),
    path('career/apply/', views.career_apply, name='career-apply'),
    # path('career/posting-job/', views.career_posting_job, name='career-posting-job'),
    
    path('docs/', views.docs, name='docs'),
    path('connect/', views.connect, name='connect'),
    path('courses/', views.courses, name='courses'),
    path('asks/', views.asks, name='asks'),
    # path('asks/', views.asks, name='asks'),

    path('explore/', views.explore, name='explore'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions'),

    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<str:blog_type>', views.blogs, name='blogs'),

"""

