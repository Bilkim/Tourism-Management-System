# Generated by Django 3.2.9 on 2021-11-15 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelName', models.CharField(max_length=300, verbose_name='Hotel Name')),
                ('roomImage', models.ImageField(default='img1.jpg', upload_to='Images/', verbose_name='Image')),
                ('address', models.CharField(max_length=300, verbose_name='Location')),
                ('phone', models.CharField(max_length=25, verbose_name='Contact Phone')),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField(max_length=150, verbose_name='Price per Night')),
            ],
        ),
        migrations.CreateModel(
            name='HotelMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inDate', models.DateField(max_length=300, verbose_name='Check In Date')),
                ('outDate', models.DateField(max_length=25, verbose_name='Check Out Date')),
                ('adultNo', models.IntegerField(verbose_name='Number of Adults')),
                ('childrenNo', models.IntegerField(verbose_name='Number of Children')),
                ('roomNo', models.IntegerField(verbose_name='Number of Rooms')),
                ('last_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
