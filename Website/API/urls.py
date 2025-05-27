from django.urls import path
from . import views

urlpatterns = [
          

    # functality based views
    path('',views.index,name='index'),
    # path('index',views.index,name='index'),
    path('documentations',views.documentations,name='documentations'),


    # class based views
    # path('designations',views.DesignationListCreateView.as_view(),name='designations'),
    # path('users',views.UsersListCreateView.as_view(),name='users'),


]

