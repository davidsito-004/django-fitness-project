from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):
    """Custom register form based on UserCreationForm.

    Notes:
        The labels for the username, email, password1, and 
        password2 fields are customized.
    """

    def __init__(self, *args, **kwargs):
        """Initilize the RegisterForm instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Your username'
        self.fields['email'].label = 'Your email'
        self.fields['password1'].label = 'Your password'
        self.fields['password2'].label = 'Confirm your password'
        self.label_suffix = ""

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    """Custom login form based on AuthenticationForm.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the CustomLoginForm.

         Override the parent class's init method to set 
         an empty label suffix.

         Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
