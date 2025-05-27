"""
URL configuration for Website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# import views
# from Security.views_for_google import google_onetap_popup_login as google_onetap
from .views_for_google import google_onetap_popup_login as google_onetap


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('UI.urls')),
    # path('ui/', include('ui.urls')),
    path('api/', include('API.urls')),
    path('security/', include('Security.urls')),

    
    path("ckeditor/", include("ckeditor_uploader.urls")),

          

    # all auth - google, facebook, github
    path("accounts/", include("allauth.urls")),  # Normal Google Login
    # suggested by google authentication 
    # path("google-login/", google_login_popup, name="google_login_popup"),
    path("security/google-onetap-popup-login/", google_onetap, name="google_login_popup"),
    # path('accounts/google/one-tap-login/', google_one_tap_login, name='google_one_tap_login'),
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



