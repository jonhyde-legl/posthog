# Generated by Django 3.0.3 on 2020-04-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0046_event_names_properties_to_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user", name="email_opt_in", field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
