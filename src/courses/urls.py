from django.urls import path
from .views import course_list

urlpatterns = [
    path('', course_list, name='course-list'), 
]