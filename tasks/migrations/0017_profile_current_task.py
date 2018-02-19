# Generated by Django 2.0 on 2018-02-19 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_task_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_task',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
            preserve_default=False,
        ),
    ]
