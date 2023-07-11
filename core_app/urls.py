from django.urls import path
import core_app.views

urlpatterns = [
    path('', core_app.views.home, name='home')
]
