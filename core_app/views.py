from django.shortcuts import render, redirect


def home(request):
    """Handle the home page request.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    # Prevent users from seeing the home page if they are authenticated
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        context = {'title': 'home'}
        return render(request, 'core_app/home.html', context=context)
