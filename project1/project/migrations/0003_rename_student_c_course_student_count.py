# Generated by Django 5.0.7 on 2024-12-22 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_course_description_course_course_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='student_c',
            new_name='student_count',
        ),
    ]
