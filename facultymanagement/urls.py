from django.urls import path,include
from .  import views

urlpatterns = [
    path("", views.login_page, name='login_page'),
    path("testing/", views.sample, name='sample'),
    path("register/", views.faculty_registration, name='faculty_registration'),
    path('faculty_register/', views.faculty_register, name = 'faculty_register'),
    path('home/', views.faculty_home, name='faculty_home'),
    path("developement/", views.faculty_development, name='faculty_development'),
    path('admins/', views.admin_home, name='admin_home'),
    path('course/', views.course_assign, name='course_assign'),
    path('edit/<int:id>', views.edit_faculty, name='edit_faculty'),
    path('remove/<int:id>', views.delete_faculty, name='delete_faculty'),

]