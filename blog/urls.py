from django.urls import path
from .views import Home, About, Contact, Login, Signup,Dashboard,Logout

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about-us/', About.as_view(), name='about'),
    path('contact-us/', Contact.as_view(), name='contact'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Signup.as_view(), name='signup'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    path('logout/', Logout.as_view(), name='logout'),

]
