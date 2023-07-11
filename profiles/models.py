from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from foods.models import Food


class Profile(models.Model):
    """Model representing the profile of the user.

    Returns:
        Profile: An instance of the Profile model.
    """
    # A user can have only one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(
        default='profile-default.jpg', upload_to='profile_images')

    calorie_goal = models.FloatField(
        max_length=25, default=0, verbose_name='Calories')

    protein_goal = models.FloatField(
        max_length=25, default=0, verbose_name='Protein')

    carb_goal = models.FloatField(
        max_length=25, default=0, verbose_name='Carb')

    fat_goal = models.FloatField(max_length=25, default=0, verbose_name='Fat')

    def __str__(self):
        """Return a string representation of the profile.

        Returns:
            str: The user to whom the profile belongs.
        """
        return f"{self.user.username}'s profile"

    def save(self, *args, **kwargs):
        """Save the profile instance.

        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        super().save(*args, **kwargs)

        image = Image.open(self.image.path)
        # Rezise the image automatically to a maximum dimension of 300px
        if image.height > 300 or image.width > 300:
            new_size = (300, 300)
            image.thumbnail(new_size)

            image.save(self.image.path)


class ProfileList(models.Model):
    """Model representing a list of food items in a profile.

    Returns:
        ProfileList: An instance of the PrifleList model.
    """
    title = models.CharField(max_length=100)
    ready = models.BooleanField(default=False)
    # A profile can be associated with many ProfileList objects.
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of the ProfileList model.

        Returns:
            str: The title of the list.
        """
        return f"{self.title} list"


class ProfileFood(models.Model):
    """Model representing a food item within a user's profile list.

    Returns:
        ProfileList: An instance of the PrifleList model.
    """
    # A Food can be associated with many ProfileFood objects.
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='foods')
    # A ProfileList can be associated with many ProfileFood objects.
    current_list = models.ForeignKey(
        ProfileList, on_delete=models.CASCADE, related_name='selected_foods')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        """Return a string representation of the ProfileFood.

        Returns:
            str: The food name within the user's list.
        """
        return self.food.name
