# Generated by Django 3.1.2 on 2020-12-06 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0018_remove_usercoursequestion_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercoursequestion',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_questions', to='its.course'),
            preserve_default=False,
        ),
    ]