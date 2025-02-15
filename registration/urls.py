from django.urls import path
from .views import TechProviderRegisterView, TechSeekerRegisterView

urlpatterns = [
    path('register/tech-provider/', TechProviderRegisterView.as_view(), name='tech-provider-register'),
    path('register/tech-seeker/', TechSeekerRegisterView.as_view(), name='tech-seeker-register'),
]