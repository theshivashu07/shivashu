from django.shortcuts import render, redirect
from django.http import JsonResponse

# import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.contrib.auth.models import User


from .decorators import redirect_if_authenticated, redirect_if_superuser

from django.conf import settings

import requests
# Create your views here.







def index(request):
        ReturningData = dict()
        return render(request,"Security/index.html",ReturningData); 


# Important Decorator, active only if not logged in
@redirect_if_authenticated(redirect_to='index')
def login_view(request):

    if request.method == "POST":
        next = request.GET.get("next", "/") 
        user = request.POST.get("user")
        password = request.POST.get("password")
        by = request.POST.get("by")
        
        # if anything coming without email or username, go back
        if by not in [ "email", "username" ]:
            return redirect(request.path)

        # if come with email, important 
        if by == "email":
            user = User.objects.filter(email=user)
            user = user.first().username if user else None

        user = authenticate(request, username=user, password=password)  # Check credentials
        print(user)
        
        # if user is not None:
        if user:
            login(request, user)  
            return redirect(next) 
        
        return redirect(request.path) 

    ReturningData = {
        "paths" : [
            {
                "url" : "/security/",
                "name" : "Security",
                "activate" : True
            },
            {
                "url" : "/security/login/",
                "name" : "Login",
                "activate" : False
            }
        ]
    }
    return render(request,"Security/login.html",ReturningData);

# @login_required(login_url="/login/")
@login_required(login_url="/security/login/")
def logout_view(request):
        ReturningData = dict()
        return render(request,"Security/logout.html",ReturningData);

# @login_required(login_url="/login/")
@login_required(login_url="/security/login/")
def logout_confirmations(request):
        

        if request.method == "POST":
                
                # Log out the user (clears the session completely)
                logout(request)

                # Clear any specific cookies manually if you have set tokens etc.
                # response = HttpResponseRedirect('/')  # Redirect to home page or login page
                # response.delete_cookie('sessionid')  # Django session cookie
                # response.delete_cookie('csrftoken')  # CSRF token (if you want)

                # If you have any custom cookies (like JWT access/refresh tokens), clear them too:
                # response.delete_cookie('access_token')
                # response.delete_cookie('refresh_token')

                return redirect("/")

        ReturningData = dict()
        return render(request,"Security/logout-confirmations.html",ReturningData);



# def register_view(request):
#         ReturningData = dict()
#         return render(request,"Security/register.html",ReturningData);

from Security.models import CustomUser as User
def register_view(request):
    
    print("coming to register view")
    
    ReturningData = dict()    

    if request.method == "POST":

        print("coming to register view post")

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # user = User(
        #         username=username,
        #         email=email,
        # )
        user = User.objects.create_user(
              username=username, 
              email=email
        )
        user.set_password(password)
        user.save()

        print("User Created")
        
        # ReturningData['message'] = "Registration successful!"
        return redirect('/security/profile-setup/')  # 👈 after registration, redirect to login page (ya jo chaaho)


    return render(request,"Security/register.html",ReturningData);


def reset_password(request):
        ReturningData = dict()
        return render(request,"Security/reset-password.html",ReturningData);

# @login_required(login_url="/login/")
@login_required(login_url="/security/login/")
def refresh_token_view(request):
        ReturningData = dict()
        return render(request,"Security/refresh-token.html",ReturningData);


# @login_required(login_url="/login/")
@login_required(login_url="/security/login/")
def profile_setup(request):        
        ReturningData = dict()

        print("coming to profile setup")
        
        if request.method == 'POST':
                print("coming to profile setup post")
                image = request.FILES.get('profile_picture')
                print("image :",image)

                if True:
                        user = request.user
                        user.username = request.POST.get('username')
                        user.first_name = request.POST.get('firstname')
                        user.last_name = request.POST.get('lastname')
                        user.email = request.POST.get('email')
                        user.profession = request.POST.get('profession')
                        user.password = request.POST.get('password')
                        user.set_password(user.password)

                        # image/image.name : profiles/users/smile.png
                        # image.url : /_uploads/profiles/users/smile.png
                        if image:
                                user.profile_picture = image
                                print("profile_picture :", user.profile_picture)
                                # user.profile_picture_url = f"{settings.MEDIA_URL}{user.profile_picture.name}"
                                # print("profile_picture_url :", user.profile_picture_url)

                        user.save()
                        
                        user.backend = 'django.contrib.auth.backends.ModelBackend'  # Default backend

                        # Log the user back in
                        login(request, user)

                        print("User Profile Updated")
                        print( user.username, user.first_name, user.last_name, user.email, user.profession, user.password, user.profile_picture, user.profile_picture_url, sep=" | ")
                        return redirect('/')  # or any page you want
                print("No image found")
                return render(request, "Security/profile-setup.html", ReturningData)

        user = request.user
        print( user.username, user.first_name, user.last_name, user.email, user.profession, user.password, user.profile_picture, user.profile_picture_url, sep=" | ")
        return render(request,"Security/profile-setup.html",ReturningData);








