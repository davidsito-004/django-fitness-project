from django.urls import path
import profiles.views


urlpatterns = [
    path('profile/', profiles.views.profile, name='profile'),
    path('lists/', profiles.views.lists, name='user-lists'),
    path('add-food/', profiles.views.add_food, name='add-food'),
    path('create-list/',
         profiles.views.create_list, name='create-list'),
    path('list/<int:list_id>/', profiles.views.show_list, name='list')
]
