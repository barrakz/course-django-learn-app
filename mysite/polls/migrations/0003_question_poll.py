# Generated by Django 4.0.4 on 2022-05-14 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.poll'),
        ),
    ]
