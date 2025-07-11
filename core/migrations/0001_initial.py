# Generated by Django 5.2.4 on 2025-07-11 19:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeSheetEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("supplier_name", models.CharField(max_length=255)),
                ("customer", models.CharField(max_length=255)),
                ("project_name", models.CharField(max_length=255)),
                ("project_id", models.CharField(max_length=100)),
                ("service_type_id", models.CharField(max_length=100)),
                ("phase", models.CharField(max_length=100)),
                ("task_id", models.CharField(blank=True, max_length=100, null=True)),
                ("date_of_services", models.DateField()),
                ("duration", models.TimeField()),
                ("work_description", models.TextField()),
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("admin", "Admin"),
                            ("consultant", "Consultant"),
                            ("client", "Client"),
                        ],
                        max_length=20,
                    ),
                ),
                ("organization", models.CharField(blank=True, max_length=100, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Profile",
                "verbose_name_plural": "User Profiles",
            },
        ),
    ]
