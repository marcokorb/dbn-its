# Generated by Django 3.1.2 on 2020-12-19 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0020_networksubjectprobabilities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networksubjectprobabilities',
            name='transition_probabilities',
        ),
    ]