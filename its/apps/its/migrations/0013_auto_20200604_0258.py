# Generated by Django 2.2.2 on 2020-06-04 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0012_networksubject_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Código')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('is_evidence', models.BooleanField(default=False, verbose_name='É uma evidência?')),
            ],
        ),
        migrations.RemoveField(
            model_name='usercourseevidence',
            name='evidence',
        ),
        migrations.RemoveField(
            model_name='userevidence',
            name='evidence',
        ),
        migrations.RemoveField(
            model_name='usersubject',
            name='subject',
        ),
        migrations.AlterField(
            model_name='networksubject',
            name='evidences',
            field=models.ManyToManyField(related_name='networks_subjects_evidences', to='its.Node'),
        ),
        migrations.AlterField(
            model_name='networksubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='networks_subjects', to='its.Node'),
        ),
        migrations.AlterField(
            model_name='networksubject',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='networks_subjects_parents', to='its.Node'),
        ),
        migrations.AlterField(
            model_name='question',
            name='evidences',
            field=models.ManyToManyField(to='its.Node', blank=True),
        ),
        migrations.AlterField(
            model_name='usercourseevidence',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_evidences', to='its.Course'),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AddField(
            model_name='usercourseevidence',
            name='node',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_courses', to='its.Node'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userevidence',
            name='node',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_evidences', to='its.Node'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersubject',
            name='node',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_subjects', to='its.Node'),
            preserve_default=False,
        ),
    ]