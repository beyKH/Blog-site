# Generated by Django 3.1.7 on 2021-03-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.CharField(default='https://images.unsplash.com/photo-1471107340929-a87cd0f5b5f3?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=966&q=80', max_length=400),
        ),
    ]