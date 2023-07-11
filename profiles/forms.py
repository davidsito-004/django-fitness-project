from django import forms
from django.contrib.auth.models import User
from .models import Profile, ProfileList
from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    """Custom File input widget.
    """

    def render(self, name, value, attrs=None, renderer=None):
        """Return the modified HTML output for the widget.

        Args:
            name (str): The form field's name.
            value (str): The value of the form field.
            attrs (dict, optional): Attributes for the widget. Defaults to None.
            renderer (Renderer, optional): Renderer object to use for rendering. Defaults to None.

        Returns:
            str: String representation of the HTML to be rendered.
        """
        format_html = super().render(name, value, attrs, renderer)
        # Remove the label and image url from the widget
        format_html = format_html.replace('Currently: ', '')
        format_html = format_html.replace('Change:', '')
        format_html = format_html.split('</label>')[-1]
        return format_html


class PictureUpdateForm(forms.ModelForm):
    """Form for updating user profile picture.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the PictureUpdateForm instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        # Show a cleaner widget
        self.fields['image'].label = ''
        self.fields['image'].widget = CustomClearableFileInput()

    class Meta:
        model = Profile
        fields = ['image']


class ReadOnlyUserInfoForm(forms.ModelForm):
    """Form for displaying user information with read-only fields.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the ReadOnlyUserInfoForm instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        # Clean fields and make them readonly
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['readonly'] = True

    class Meta:
        model = User
        fields = ['username', 'email']


class ReadOnlyMacroDataForm(forms.ModelForm):
    """Form for displaying user macros information with read-only fields.
    """

    def __init__(self, *args, **kwargs):
        """Initialized the ReadOnlyMacroDataForm instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        # Clean fields and make them readonly
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['readonly'] = True

    class Meta:
        model = Profile
        fields = ['calorie_goal', 'protein_goal', 'carb_goal', 'fat_goal']


class EditableUserInfoForm(ReadOnlyUserInfoForm):
    """Form for displaying user information with editable fields.
    """

    def __init__(self, *args, **kwargs):
        """Initialized the EditableUserInfoForm instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = False
            self.fields[field].required = True


class EditableMacroDataForm(ReadOnlyMacroDataForm):
    """Form for displaying user macros information with editable fields.
    """

    def __init__(self, *args, **kwargs):
        """Initialized the EditableMacroDataForm instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = False


class ProfileListForm(forms.ModelForm):
    """Form for creating a user list.
    """
    title = forms.CharField(max_length=100,
                            help_text="You will see your list displayed like this: 'Your title' list")

    class Meta:
        model = ProfileList
        fields = ['title']
