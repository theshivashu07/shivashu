import json
import requests
from django.contrib.auth import login, get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

# Use your CustomUser
CustomUser = get_user_model()

@csrf_exempt
def google_onetap_popup_login(request):
    if request.method == "POST":
        body = json.loads(request.body)
        token = body.get('credential')

        if not token:
            return JsonResponse({'error': 'Missing token'}, status=400)

        try:
            idinfo = id_token.verify_oauth2_token(
                token,
                google_requests.Request(),
                "608674038178-m2afsu45qt7le6vvejra469bhvq40a1l.apps.googleusercontent.com"
            )

            email = idinfo.get('email')
            first_name = idinfo.get('given_name', '')
            last_name = idinfo.get('family_name', '')

            try:
                # Try to find ONE user with email
                user = CustomUser.objects.get(email=email)
            except CustomUser.MultipleObjectsReturned:
                # If multiple users with same email -> pick the latest one
                user = CustomUser.objects.filter(email=email).order_by('-id').first()
            except CustomUser.DoesNotExist:
                # If no user found, create a new one
                username = email.split('@')[0]

                user = CustomUser.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )

            # login the user
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return JsonResponse({'message': 'Login successful'})

        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Invalid token'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
