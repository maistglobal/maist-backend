# Generated by Django 5.1.6 on 2025-02-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0003_alter_customuser_industry_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="TechProvider",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("industry_type", models.CharField(max_length=255)),
                ("company_name", models.CharField(max_length=255, unique=True)),
                ("company_registered_number", models.CharField(max_length=50, unique=True)),
                ("company_address", models.TextField()),
                ("primary_email", models.EmailField(max_length=254, unique=True)),
                ("linkedin_link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="TechSeeker",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("company_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("linkedin_link", models.URLField()),
                ("contact_number", models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
