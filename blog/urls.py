from django.urls import path,include
from .views import Home, About, Contact, Login, Signup, Dashboard, Logout, AddPost, UpdatePost, DeletePost



from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Blog API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)




urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about-us/', About.as_view(), name='about'),
    path('contact-us/', Contact.as_view(), name='contact'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Signup.as_view(), name='signup'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('logout/', Logout.as_view(), name='logout'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('update/<int:id>', UpdatePost.as_view(), name='updatepost'),
    path('delete/<int:id>', DeletePost.as_view(), name='deletepost'),
     path('blogapi/',include('blog.api.urls')),


    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
