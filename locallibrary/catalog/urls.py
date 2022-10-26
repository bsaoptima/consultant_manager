"""

This is where we add our patterns as we build the application    
    
"""


from django.urls import path
from .views import RegisterView, TestView

urlpatterns = [
  path('register', RegisterView.as_view()),
  path('test', TestView.as_view()),
]