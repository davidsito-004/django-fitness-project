from django.urls import path
import foods.views


urlpatterns = [
    path('foods/', foods.views.show_foods, name='food-list'),
    path('category/<int:category_id>',
         foods.views.show_by_category, name='category-url'),
    path('results/',
         foods.views.SearchFoodView.as_view(), name='food-search')
]
