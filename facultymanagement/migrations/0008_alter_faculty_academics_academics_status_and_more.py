# Generated by Django 5.0.4 on 2024-04-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultymanagement', '0007_alter_faculty_development_credit_point_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_academics',
            name='Academics_Status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='Average_Student_Feedback',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='Cat_A_Points_Earned',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='Cat_B_Points_Earned',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='Even_Semester_Average',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='No_of_Actually_Held_Classes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='No_of_Schedule_Classes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='No_of_Students_Passed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='No_of_Students_Registered',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='Odd_Semester_Average',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='Result',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='Semester_Status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='Semester_roman',
            field=models.CharField(default='XX', max_length=5),
        ),
        migrations.AlterField(
            model_name='faculty_academics',
            name='Supporting_Docs',
            field=models.CharField(default='Null', max_length=254),
        ),
        migrations.AlterField(
            model_name='faculty_development',
            name='Support_Document_No',
            field=models.CharField(default='Null', max_length=48),
        ),
    ]