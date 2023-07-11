# Generated by Django 4.1.7 on 2023-04-04 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=40)),
                ('protein', models.TextField(max_length=10)),
                ('carbs', models.TextField(max_length=10)),
                ('fat', models.TextField(max_length=10)),
                ('image', models.ImageField(
                    default='generic.jpg', upload_to='foods_pictures')),
                ('categories', models.ManyToManyField(to='foods.category')),
            ],
        ),
    ]