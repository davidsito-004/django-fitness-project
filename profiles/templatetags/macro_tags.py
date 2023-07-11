from django import template
from profiles.models import ProfileFood, ProfileList

register = template.Library()


@register.simple_tag
def total_macro(food_obj: ProfileFood, macro: str):
    """Calculate the total macro value per food added to the list.

    Args:
        food_obj (ProfileFood): The food that belongs to the current list.
        macro (str): The name of the macro field to be retrieved.

    Returns:
        (bool): The total macro value per food item added.
    """
    total = getattr(food_obj.food, macro) * food_obj.quantity
    return round(total, 2)


@register.simple_tag
def total_list_macro(list_obj: ProfileList, macro: str):
    """Calculate the total macro value in the list.

    Args:
        list_obj (ProfileList): The current list.
        macro (str): The name of the macro field to be retrieved.

    Returns:
        (bool): The total macro value.
    """
    foods = list_obj.selected_foods.all()
    # Get the total per food and sum it
    total = sum([total_macro(food, macro) for food in foods])
    return round(total, 2)


@register.simple_tag
def remaining_macros(list_obj: ProfileList, macro: str, p_field: str):
    """Calculate the remaining total macro values in the list.

    Args:
        list_obj (ProfileList): The current list.
        macro (str): The name of the macro field to be retrieved.
        p_field (str): The name of the user macro goal field.

    Returns:
        (bool): The total macros remaining.
    """

    # Get the user's macro goal
    goal_macro = getattr(list_obj.author, p_field)
    # Get the total list
    total_list = total_list_macro(list_obj, macro)

    remaining = goal_macro - total_list

    return round(remaining, 2)
