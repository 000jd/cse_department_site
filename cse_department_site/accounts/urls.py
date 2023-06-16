from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register', views.register_page, name='register'),

    path('register/student/', views.student_form, name='register_student'),

    path('register/alumni/', views.alumni_form, name='register_alumni'),

    path('register/staff/', views.staff_form, name='register_staff'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name="logout"),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="components/password_reset.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="components/password_reset_sent.html"
    ),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="components/password_reset_sent_form.html"),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="components/password_reset_done.html"),
         name='password_reset_complete'),
]
