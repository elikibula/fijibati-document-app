# Generated by Django 4.2 on 2023-07-07 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('preferred_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('yasana', models.CharField(max_length=255)),
                ('tikina', models.CharField(max_length=255)),
                ('koro', models.CharField(max_length=255)),
                ('country_of_birth', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bc_number', models.BigIntegerField()),
                ('passport_number', models.BigIntegerField()),
                ('driverslicense_number', models.BigIntegerField()),
                ('evr_number', models.BigIntegerField()),
                ('designation', models.CharField(blank=True, choices=[('coach_grade_1', 'Coach Grade 1'), ('coach_grade_2', 'Coach Grade 2'), ('coach_grade_a', 'Coach Grade A'), ('sports_trainer_grade_1', 'Sports Trainer 1'), ('sports_trainer_grade_2', 'Sports Trainer 2'), ('sports_trainer_grade_3', 'Sports Trainer 3'), ('sports_trainer_grade_4', 'Sports Trainer 4'), ('team_manager_grade_a', 'Team Manager Grade A'), ('team_manager_grade_b', 'Team Manager Grade B'), ('team_manager_grade_c', 'Team Manager Grade C'), ('volunteer', 'Volunteer'), ('match_official', 'Match Official'), ('team_official', 'Team Official'), ('player', 'Player'), ('others', 'Others')], help_text='Please select Designation', max_length=50)),
                ('club_name', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=255, null=True)),
                ('regional_league_zone', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('clearance', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]