# Generated by Django 5.0.4 on 2024-04-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultymanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_Academics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Academic_Year', models.CharField(max_length=16)),
                ('Semester_Status', models.BooleanField()),
                ('Academics_Status', models.BooleanField()),
                ('Semester_Type', models.CharField(max_length=10)),
                ('Semester', models.CharField(max_length=254)),
                ('Subject_Code', models.CharField(max_length=254)),
                ('Subject_Name', models.CharField(max_length=254)),
                ('No_of_Schedule_classes', models.IntegerField()),
                ('No_of_Actually_Held_classes', models.IntegerField()),
                ('Average_Student_Feedback', models.IntegerField()),
                ('No_of_Students_Registered', models.IntegerField()),
                ('No_of_Students_Passed', models.IntegerField()),
                ('Cat_A_points_Earned', models.IntegerField()),
                ('Cat_B_points_Earned', models.IntegerField()),
                ('Result', models.DecimalField(decimal_places=2, max_digits=2)),
                ('Odd_Semester_Average', models.DecimalField(decimal_places=2, max_digits=2)),
                ('Even_Semester_Average', models.DecimalField(decimal_places=2, max_digits=2)),
                ('Supporting_Docs', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'Faculty_Academics',
            },
        ),
        migrations.CreateModel(
            name='Faculty_Development',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=254)),
                ('Academic_Year', models.CharField(max_length=16)),
                ('Semester', models.CharField(max_length=254)),
                ('Activity', models.CharField(max_length=254)),
                ('Credit_Point', models.IntegerField()),
                ('Criteria', models.CharField(max_length=254)),
                ('Support_Document_No', models.CharField(max_length=48)),
                ('Verified_Status', models.CharField(max_length=48)),
            ],
            options={
                'db_table': 'Faculty_Development',
            },
        ),
    ]
