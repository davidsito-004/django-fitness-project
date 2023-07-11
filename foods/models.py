from django.db import models
from PIL import Image


class Category(models.Model):
    """Define the category model.

    Returns:
        Category: An instance of the Category model.

    Meta:
        verbose_name_plural (str): The plural name for the Category model
        in the admin interface.
    """
    title = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Represent the category as a string.

        Returns:
            str: The title of the category.
        """
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Food(models.Model):
    """Define the food model.

    Returns:
        Food: An instance of the Food model.
    """
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    calories = models.FloatField(max_length=25, default=0)
    proteins = models.FloatField(max_length=10, default=0)
    carbs = models.FloatField(max_length=10, default=0)
    fat = models.FloatField(max_length=10, default=0)
    image = models.ImageField(default='generic.jpg',
                              upload_to='foods_pictures')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        """Return a string representation of the food.

        Returns:
            str: The name of the food.
        """
        return self.name

    def save(self, *args, **kwargs):
        """Save the food instance.

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
