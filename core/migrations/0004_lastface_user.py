# Generated by Django 4.1.4 on 2022-12-23 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_age_profile_certicate_profile_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastface',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]