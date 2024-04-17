from django.db import models


class Faculty(models.Model):
    Id = models.CharField(max_length=6)
    Name = models.CharField(max_length=254)
    Email_ID = models.EmailField(max_length=254)
    Gender = models.CharField(max_length=254)
    Department = models.CharField(max_length=254)
    Phone_No = models.CharField(max_length=10)
    Qualification = models.CharField(max_length=32)
    Designation = models.CharField(max_length=32)
    Username = models.CharField(max_length=8)
    Password = models.CharField(max_length=12)
    class Meta:
        db_table = "Faculty"

class Faculty_Academics(models.Model):
    Faculty_Id = models.CharField(max_length=12, default='000000')
    Academic_Year = models.CharField(max_length=16)
    Semester_Status = models.BooleanField(default=False)
    Academics_Status = models.BooleanField(default=False)
    Semester_roman = models.CharField(max_length=5, default='XX')
    Semester_Type = models.CharField(max_length=10)
    Semester = models.IntegerField()  #change
    Subject_Code = models.CharField(max_length=254)
    Subject_Name = models.CharField(max_length=254)
    No_of_Schedule_Classes = models.IntegerField(default=0)
    No_of_Actually_Held_Classes = models.IntegerField(default=0)
    Average_Student_Feedback = models.IntegerField(default=0)
    No_of_Students_Registered =  models.IntegerField(default=0)
    No_of_Students_Passed = models.IntegerField(default=0)
    Cat_A_Points_Earned = models.IntegerField(default=0)
    Cat_B_Points_Earned = models.IntegerField(default=0)
    Result = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    Result_Points = models.IntegerField(default= 0 )
    Odd_Semester_Average = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    Even_Semester_Average = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    Supporting_Docs = models.CharField(max_length=254, default="Null")
    class Meta:
        db_table = 'Faculty_Academics'

class Faculty_Development(models.Model):
    Faculty_Id = models.CharField(max_length=12, default='000000')
    Category = models.CharField(max_length=254)
    Academic_Year = models.CharField(max_length=16)
    Semester_Status = models.BooleanField(default=False)
    Academics_Status = models.BooleanField(default=False)
    Semester_roman = models.CharField(max_length=5, default='xxx')
    Semester_Type = models.CharField(max_length=10, default='Odd')
    Semester = models.IntegerField(default=0)
    Activity = models.CharField(max_length=254)
    Credit_Point = models.IntegerField(default=0)
    Criteria = models.CharField(max_length=254)
    Support_Document_No = models.CharField(max_length=48, default="Null")
    Verified_Status = models.CharField(max_length=48, default="Pending")
    class Meta:
        db_table = 'Faculty_Development'

class Every_Academic_Report(models.Model):
    Faulty_Id = models.CharField(max_length=12, default='000000')
    Faculty_Name = models.CharField(max_length=254)
    Academic_Year = models.CharField(max_length=10)
    Teaching_Process = models.IntegerField()
    Students_Feedback = models.IntegerField()
    Departmental_Activities = models.IntegerField()
    Institute_Activities = models.IntegerField()
    ACR = models.IntegerField()
    Society_Contribution = models.IntegerField()
    Total_points = models.IntegerField()
    Total_points_Scale = models.IntegerField()

