# Generated by Django 2.0.6 on 2018-06-27 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='choicetext',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_date',
            new_name='pubdate',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='questiontext',
        ),
    ]
