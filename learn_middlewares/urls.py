from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.func_middleware_view),
    path('class/', views.class_middleware_view),
    path('exception/', views.exceptionView),
]