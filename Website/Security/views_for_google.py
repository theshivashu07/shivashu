import json
import requests
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt

from Security.models import CustomUser  # replace `yourapp` with your actual app name

@csrf_exempt
def google_onetap_popup_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        token = data.get("credential")

        # Verify the token with Google
        response = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={token}")
        idinfo = response.json()

        email = idinfo.get("email")
        name = idinfo.get("name")
        picture = idinfo.get("picture")

        if email:
            user, created = CustomUser.objects.get_or_create(email=email, defaults={
                "username": email.split('@')[0],
                "first_name": name,
                "profile_picture_url": picture  # only if you have this field
            })
            login(request, user)
            return JsonResponse({"message": "Logged in successfully"})
        
        return JsonResponse({"error": "Email not found"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)




import json
import google.auth.transport.requests
import google.oauth2.id_token
from django.http import JsonResponse
from django.contrib.auth import login
from Security.models import CustomUser  # ✅ Correct import

def google_onetap_popup_login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        token = body.get('credential')

        try:
            request_obj = google.auth.transport.requests.Request()
            idinfo = google.oauth2.id_token.verify_oauth2_token(token, request_obj)

            email = idinfo.get('email')
            name = idinfo.get('name')
            picture = idinfo.get('picture')

            user, created = CustomUser.objects.get_or_create(email=email, defaults={
                'username': email.split('@')[0],
                'first_name': name.split(' ')[0] if name else '',
                'last_name': ' '.join(name.split(' ')[1:]) if name and len(name.split(' ')) > 1 else '',
            })

            login(request, user)
            return JsonResponse({'success': True})

        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request'})


