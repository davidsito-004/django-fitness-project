from django.shortcuts import render, redirect
from .forms import RegisterForm, CustomLoginForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView


def register_user(request):
    """Register new users.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been registered!')
            return redirect('login-user')

    else:  # GET method
        form = RegisterForm()

    context = {'form': form,
               'title': 'register'}

    return render(request, 'accounts/register_user.html', context=context)


class CustomLoginView(LoginView):
    """Custom login view.

    Extend the Django built-in LoginView and customize the behavior.

    Returns:
        HttpResponse: The HTTP response object.
    """
    authentication_form = CustomLoginForm
    extra_context = {'title': 'login'}

    def get(self, request, *args, **kwargs):
        """Handle GET requests for login.

        Args:
            request (HttpRequest): The HTTP request object.
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.


        Returns:
            HttpResponse: The HTTP response object.
        """
        # If the user is already authenticated, redirect them to the home page.
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return super().get(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    """Custom logout view.

    Extend the Django built-in LogoutView and add a title to the context.

    Returns:
        HttpResponse: The HTTP response object.
    """
    extra_context = {'title': 'logout'}
