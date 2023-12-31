# Generated by Django 4.2.2 on 2023-07-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('bullet_points', models.TextField(help_text='Enter bullet points separated by newline')),
                ('display', models.BooleanField(default=True)),
            ],
        ),
    ]
