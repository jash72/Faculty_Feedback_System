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
    Semester_Status = models.BooleanField()
    Academics_Status = models.BooleanField()
    Semester_Type = models.CharField(max_length=10)
    Semester = models.IntegerField()  #change
    Subject_Code = models.CharField(max_length=254)
    Subject_Name = models.CharField(max_length=254)
    No_of_Schedule_Classes = models.IntegerField()
    No_of_Actually_Held_Classes = models.IntegerField()
    Average_Student_Feedback = models.IntegerField()
    No_of_Students_Registered =  models.IntegerField()
    No_of_Students_Passed = models.IntegerField()
    Cat_A_Points_Earned = models.IntegerField()
    Cat_B_Points_Earned = models.IntegerField()
    Result = models.DecimalField(max_digits=2, decimal_places=2)
    Result_Points = models.IntegerField(default= 0 )
    Odd_Semester_Average = models.DecimalField(max_digits=2, decimal_places=2)
    Even_Semester_Average = models.DecimalField(max_digits=2, decimal_places=2)
    Supporting_Docs = models.CharField(max_length=254)
    class Meta:
        db_table = 'Faculty_Academics'

class Faculty_Development(models.Model):
    Faculty_Id = models.CharField(max_length=12, default='000000')
    Category = models.CharField(max_length=254)
    Academic_Year = models.CharField(max_length=16)
    Semester = models.CharField(max_length=254)
    Activity = models.CharField(max_length=254)
    Credit_Point = models.IntegerField()
    Criteria = models.CharField(max_length=254)
    Support_Document_No = models.CharField(max_length=48)
    Verified_Status = models.CharField(max_length=48)
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

