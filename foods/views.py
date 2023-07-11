from django.shortcuts import render, get_object_or_404
from foods.models import Food, Category
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


@login_required
def show_foods(request):
    """Display a list of all available foods.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    Notes:
        The retrieval of all foods is implemented through the 
        context processor.
    """
    context = {'title': 'foods',
               'content_title': 'All'}

    return render(request, 'foods/foods.html', context=context)


@login_required
def show_by_category(request, category_id: int):
    """Display a list of all available foods by category.

    Args:
        request (HttpRequest): The HTTP request object.
        category_id (int): The id of the category to filter foods.

    Returns:
        HttpResponse: The HTTP response object.

    Notes:
        The retrieval of foods by category is implemented through the 
        context processor.
    """
    c = get_object_or_404(Category, id=category_id)

    context = {'category': c,
               'title': c,
               'content_title': c}

    return render(request, 'foods/category.html', context=context)


class SearchFoodView(ListView):
    """Display a list of foods based on search query.

    Returns:
        ListView: An instance of ListView with the paginated search results.

    Notes:
        The variable name `page_obj` is utilized for consistency 
        across the context processor.
    """
    model = Food
    template_name = 'foods/food_search.html'
    context_object_name = 'page_obj'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        """Add the title to the context

        Args:
            kwargs (dict): Additional keyword arguments.

        Returns:
            dict: The updated context dictionary.
        """
        context = super().get_context_data(**kwargs)

        context['title'] = 'results'

        return context

    def get_queryset(self):
        """Get the Food queryset based on search query

        Returns:
            QuerySet: List of foods based on search query
        """
        query = self.request.GET.get("query")
        food_search_results = Food.objects.filter(
            name__icontains=query
        )

        if not food_search_results:
            food_search_results = ''

        return food_search_results
