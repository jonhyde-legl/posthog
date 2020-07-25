# Generated by Django 3.0.6 on 2020-07-25 20:59

from django.db import migrations, models
from posthog.models.utils import generate_random_token


def add_signup_tokens(apps, schema_editor):
    User = apps.get_model("posthog", "User")
    for user in User.objects.filter(personal_access_token__isnull=True):
        user.personal_access_token = generate_random_token()
        user.save()


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0072_auto_20200725_2059"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="personal_access_token",
            field=models.CharField(default=generate_random_token, max_length=32),
        ),
    ]
