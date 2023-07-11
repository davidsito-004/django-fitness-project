from foods.models import Category, Food
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from foods.models import Category


def get_categories(request):
    """Retrieve foods categories for rendering in templates.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary containing a QuerySet with all instances
        of Category.
    """
    categories = Category.objects.all()

    return {'categories': categories}


def get_foods_pages(request):
    """Retrieve paginated food pages for the context.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary containing the paginated food page
        object, or an empty dictionary if no paginator is available.
    """
    paginator = None
    page_number = request.GET.get('page')

    # Based on the URL name, retrieve and paginated food instances
    if request.resolver_match.url_name == 'food-list':
        # Paginate all Food instances
        foods = Food.objects.all()
        paginator = Paginator(foods, 5)
    elif request.resolver_match.url_name == 'category-url':
        # Filter and paginate Food instances by category
        category_id = request.resolver_match.kwargs.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        foods = Food.objects.filter(categories=category)
        paginator = Paginator(foods, 5)

    return {'page_obj': paginator.get_page(page_number)} if paginator else {}
