# Generated by Django 3.2.6 on 2021-09-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=50, unique=True)),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
                ('description', models.TextField(blank=True, default='', max_length=400)),
                ('cat_image', models.ImageField(blank=True, default='', upload_to='photos/categories')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
