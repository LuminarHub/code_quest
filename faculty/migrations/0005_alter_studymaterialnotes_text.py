# Generated by Django 5.1.4 on 2025-02-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_language_alter_studymaterialfile_file_questions_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studymaterialnotes',
            name='text',
            field=models.URLField(),
        ),
    ]
