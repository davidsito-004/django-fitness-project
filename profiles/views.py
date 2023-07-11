from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (ReadOnlyUserInfoForm,
                    EditableUserInfoForm,
                    ReadOnlyMacroDataForm,
                    EditableMacroDataForm,
                    PictureUpdateForm,
                    ProfileListForm)
from foods.models import Food
from profiles.models import ProfileList, ProfileFood
from django.http import JsonResponse
import json
from django.core.paginator import Paginator


@login_required
def profile(request):
    """Display and update user information, profile picture and macro data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    Notes:
        User information and macro data can be displayed in either read-only 
        or editable mode based on the edit button's interaction.

    """
    # Functionality based on the flag, defaults to False if not set
    request.session.get('editable', False)

    if request.method == 'POST':
        # User can interact with two buttons
        if 'picture_button' in request.POST:  # Change profile picture

            # Create a PictureUpdateForm with the new picture
            picture_update_form = PictureUpdateForm(
                request.POST, request.FILES, instance=request.user.profile)
            # Check if the form is valid and save it
            if picture_update_form.is_valid():
                picture_update_form.save()
                # Create readonly ReadOnlyUserInfoForm and ReadOnlyMacroDataForm
                user_update_form = ReadOnlyUserInfoForm(instance=request.user)
                profile_update_form = ReadOnlyMacroDataForm(
                    instance=request.user.profile)
                # Set the editable flag to False in order to show the edit button
                request.session['editable'] = False
                redirect('profile')

        elif 'info_button' in request.POST:  # User information and macros data

            # If the button's value is 'edit' when clicked, create editable instances
            # to display them
            if request.POST.get('info_button') == 'edit':
                user_update_form = EditableUserInfoForm(
                    instance=request.user)
                profile_update_form = EditableMacroDataForm(
                    instance=request.user.profile)
                picture_update_form = PictureUpdateForm(
                    instance=request.user.profile)
                # Set the editable flag to True
                request.session['editable'] = True

            elif request.POST.get('info_button') == 'save':
                # Create instances with the new user's info
                user_update_form = EditableUserInfoForm(request.POST,
                                                        instance=request.user)
                profile_update_form = EditableMacroDataForm(request.POST,
                                                            instance=request.user.profile)

                if user_update_form.is_valid() and profile_update_form.is_valid():
                    user_update_form.save()
                    profile_update_form.save()
                    # Set the flag to False in order to show the edit button
                    request.session['editable'] = False

                    # Create readonly instances with the new user's info
                    user_update_form = ReadOnlyUserInfoForm(
                        instance=request.user)
                    profile_update_form = ReadOnlyMacroDataForm(
                        instance=request.user.profile)
                    # Create PIctureUpdateForm in order to display the template correctly
                    picture_update_form = PictureUpdateForm(
                        instance=request.user.profile)

                    redirect('profile')

    # If the method is GET, create readonly instances
    else:
        # Set the editable flag to False
        request.session['editable'] = False
        user_update_form = ReadOnlyUserInfoForm(instance=request.user)
        profile_update_form = ReadOnlyMacroDataForm(
            instance=request.user.profile)
        picture_update_form = PictureUpdateForm(instance=request.user.profile)

    # Pass the correct forms to the context
    context = {'title': 'profile',
               'profile': request.user.profile,
               'user_update_form': user_update_form,
               'profile_update_form': profile_update_form,
               'picture_update_form': picture_update_form}

    return render(request, 'profiles/user_profile.html', context=context)


@login_required
def lists(request):
    """Display user food lists.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    # If the user removes a list
    if request.method == "POST":
        # Get the id of the food by getting the remove button value
        list_id = request.POST.get('remove')
        # Get the ProfileFood object
        profile_food = ProfileList.objects.get(id=list_id)
        profile_food.delete()
        return redirect('user-lists')

    current_user = request.user.profile

    # Order the lists from newest to oldest
    lists = ProfileList.objects.all().filter(author=current_user)[::-1]

    p = Paginator(lists, 4)

    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)

    context = {'title': 'my lists',
               'page_obj': page_obj}

    return render(request, 'profiles/user_lists.html', context=context)


@login_required
def create_list(request):
    """Create a new user food list.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == "POST":
        form = ProfileListForm(request.POST)
        if form.is_valid():
            # Don't save the list to the database yet
            new_list = form.save(commit=False)
            # Set the author
            new_list.author = request.user.profile
            new_list.save()
            # Get the id of the new list
            id = new_list.id
            return redirect('list', list_id=id)
    else:
        form = ProfileListForm()

    context = {'title': 'create list', 'form': form}

    return render(request, 'profiles/create_list.html', context=context)


@login_required
def show_list(request, list_id: int):
    """_summary_

    Args:
        request (HttpRequest): The HTTP request object.
        list_id (int): The id of the selected list.

    Returns:
        HttpResponse: The HTTP response object.
    """
    # If the user removes a food from the list
    if request.method == "POST":
        # Get the id of the food by getting the remove button value
        food_id = request.POST.get('remove')
        # Get the ProfileFood object
        profile_food = ProfileFood.objects.get(id=food_id)
        profile_food.delete()
        return redirect('list', list_id=list_id)

    current_list = ProfileList.objects.get(id=list_id)

    # This allows adding foods to the current list
    request.session['current_list_id'] = current_list.id

    # Retrieve all the foods that belong to the current list.
    selected_foods = current_list.selected_foods.all()

    context = {'title': 'list',
               'current_list': current_list,
               'selected_foods': selected_foods}

    return render(request, 'profiles/edit_list.html', context=context)


def add_food(request):
    """Add a food to the list that is being displayed.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response object.

    Notes:
        The JSON response object is used in conjunction with the addToList
        function in the javascript file to redirect the user to the updated list.
    """
    # Decode data into Python object and get the
    # respective object
    data = json.loads(request.body)
    food_id = data['id']
    food = Food.objects.get(id=food_id)

    # Retrive the current list
    current_list_id = request.session.get('current_list_id')
    current_list = ProfileList.objects.get(id=current_list_id)

    # Add the food to the new list
    food_added, created = ProfileFood.objects.get_or_create(
        current_list=current_list, food=food)

    # Increase the quantity by one
    food_added.quantity += 1

    food_added.save()

    return JsonResponse({'list_id': current_list_id})
