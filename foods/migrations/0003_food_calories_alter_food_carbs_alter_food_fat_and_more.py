# Generated by Django 4.1.7 on 2023-04-10 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_alter_category_options_category_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.FloatField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(default=0, max_length=10),
        ),
    ]
