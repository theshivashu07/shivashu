from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrUsernameAuthBackend(ModelBackend):
    """
    Custom authentication backend that allows login with either email or username
    using the same authenticate() function.
    """

    def authenticate(self, request, email=None, username=None, password=None, **kwargs):
        user = None

        print("user :",user)
        print(email,username,password,kwargs,sep=" | ")
        
        # Try to find the user by username
        try:
            user = User.objects.get(username=username)
            print("user :",user)
        except User.DoesNotExist:
            # If not found, try finding the user by email
            try:
                user = User.objects.get(email=username)
                print("user :",user)
            except User.DoesNotExist:
                print("No")
                return None  # No user found
         
        print("user :",user)
        # Check if password is correct
        if user and user.check_password(password):
            print("You are successfully logged in !!!")
            return user  # Successful authentication
        return None  # Incorrect password



from django.contrib.auth import login
from django.http import JsonResponse
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_framework.decorators import api_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Error

@api_view(["POST"])
def google_login_popup(request):
    token = request.data.get("credential")  # Google sends "credential"

    if not token:
        return JsonResponse({"success": False, "error": "Invalid request"})

    try:
        adapter = GoogleOAuth2Adapter()
        login_token = adapter.complete_login(request, None, token)
        login(request, login_token.user)
        return JsonResponse({"success": True})
    except OAuth2Error:
        return JsonResponse({"success": False, "error": "Google authentication failed"})





