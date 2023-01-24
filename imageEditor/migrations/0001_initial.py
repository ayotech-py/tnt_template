# Generated by Django 4.1.5 on 2023-01-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='images')),
                ('big_card_img', models.ImageField(blank=True, upload_to='images')),
                ('card_01_img', models.ImageField(blank=True, upload_to='images')),
                ('card_02_img', models.ImageField(blank=True, upload_to='images')),
                ('card_03_img', models.ImageField(blank=True, upload_to='images')),
                ('about_property', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('option', models.CharField(max_length=255)),
            ],
        ),
    ]
