# Generated by Django 4.2 on 2023-07-02 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('documents', '0003_documentcategory_parent_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.group')),
            ],
        ),
    ]
