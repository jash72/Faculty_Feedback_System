from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Faculty, Faculty_Academics, Faculty_Development

def faculty_home(request):
    return render(request, 'faculty_home.html')

''' 
faculty = Faculty.objects.filter(Username = Username)
course = Faculty_Academics.objects.filter(Faculty_Id = faculty[0].Id)
development = Faculty_Development.objects.filter(Faculty_Id = faculty[0].Id)
return render(request, 'faculty_home.html',{'faculty':faculty, 'course':course, 'development' :development })
'''

def admin_home(request):
    return render(request, 'admin_home.html')

def faculty_register(request):
    return render(request, 'faculty_register.html')

def login_page(request):
    if request.method == "POST":
        Username = request.POST.get('username')
        Password = request.POST.get('password')

        if Username.lower() == 'admin' and Password == '12345678':
            return redirect('/admins/')
        
        users = authenticate(username=Username, password=Password)
        if not Faculty.objects.filter(Username=Username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/')
        user = Faculty.objects.filter(Username=Username)
        if user[0].Username == Username and user[0].Password != Password:
            messages.error(request, "Invalid Password")
            return redirect('/')
        else:
            login(request, users)
            return redirect('/home/')
    return render(request, 'login.html')


def faculty_registration(request):
    if request.method == "POST":
        my_list = request.POST.getlist('Qualification')
        separator = ','
        Id = request.POST['Id']
        Name = request.POST['Name']
        Gender = request.POST['Gender']
        Email_ID = request.POST['Email_ID']
        Phone_No = request.POST['Phone_No']
        Qualification = separator.join(my_list)
        Department = request.POST['Department']
        Designation = request.POST['Designation']
        L = list(map(str, Name.split()))
        Faculty_First_Name = ''.join(L[:-1])
        Faculty_Last_Name = L[-1]
        Username = Id
        Password = 'F' + str(Id)
        user = Faculty.objects.filter(Username=Username)
        useremail = Faculty.objects.filter(Email_ID=Email_ID)
        if user.exists():
            messages.info(request, f"Faculty was already Registered with this Faculty ID: {Username}")
            return redirect('/register/')
        if useremail.exists():
            messages.info(request, f"Faculty was already Registered with this mail {Email_ID}.")
            return redirect('/register/')
        data2 = User(username = Username, password = Password, first_name = Faculty_First_Name, last_name = Faculty_Last_Name, email = Email_ID)
        data = Faculty(Id=Id, Name=Name, Gender=Gender, Email_ID=Email_ID, Phone_No=Phone_No, Qualification=Qualification, Department=Department, Designation=Designation, Username=Username, Password=Password)
        data.save()  
        data2.save()
        messages.info(request, "Account created Successfully!")
        return redirect('/faculty_register/')
    else:
        return render(request,'register.html')



def faculty_register(request):
    faculties = Faculty.objects.all()
    return render(request,'faculty_register.html',{'faculties':faculties} )

def edit_faculty(request,id):
    faculties = Faculty.objects.get(pk=id)
    if request.method == 'POST':
            print(request.POST)
            faculties.Id = request.POST['Id']
            faculties.Name = request.POST['Name']
            faculties.Gender = request.POST['Gender']
            faculties.Email_ID = request.POST['Email_ID']
            faculties.Phone_No = request.POST['Phone_No']
            faculties.Qualification = request.POST['Qualification']
            faculties.Department = request.POST['Department']
            faculties.Designation = request.POST['Designation']
            faculties.save()   
            return redirect('/show')
    context = {
        'faculties': faculties,
    }

    return render(request,'edit.html',context)

def delete_faculty(request,id):
    faculties = Faculty.objects.get(pk=id)
    faculty = User.objects.filter(username = faculties.Username)
    if request.method == 'POST':
        faculties.delete()
        faculty.delete()
        messages.success(request, 'Faculty deleted successfully.')
        return redirect("/faculty_register/")
    context = {
        'faculties': faculties,
    }
    return render(request,'delete.html',context)


def course_assign(request):
    if request.method == 'POST':
        Faculty_Id = request.POST['Faculty_Id']
        Academic_Year = request.POST['Academic_Year']
        Semester_Status = False
        Academics_Status = False
        Semester_roman = request.POST['Semester']
        sem_no = ['I','II','III','IV','V','VI','VII','VIII']
        Semester = sem_no.index(Semester_roman) + 1
        if int(Semester) % 2 == 0:
            Semester_Type = 'Even'
        else:
            Semester_Type = 'Odd'
        Subject_Code = request.POST['Subject_Code']
        Subject_Name = request.POST['Subject_Name']
        No_of_Schedule_Classes = 0
        No_of_Actually_Held_Classes = 0
        Average_Student_Feedback = 0
        No_of_Students_Registered = 0
        No_of_Students_Passed = 0
        Cat_A_Points_Earned = 0
        Cat_B_Points_Earned = 0
        Result = 0
        Result_Points = 0
        Odd_Semester_Average = 0
        Even_Semester_Average = 0
        Supporting_Docs = "Null"
        data2 = Faculty_Academics(Faculty_Id = Faculty_Id, Academic_Year=Academic_Year, Semester_Status=Semester_Status, Academics_Status=Academics_Status, Semester_Type=Semester_Type, Semester=Semester, Subject_Code=Subject_Code, Subject_Name=Subject_Name, No_of_Schedule_Classes=No_of_Schedule_Classes, No_of_Actually_Held_Classes=No_of_Actually_Held_Classes, Average_Student_Feedback=Average_Student_Feedback, No_of_Students_Registered=No_of_Students_Registered, No_of_Students_Passed=No_of_Students_Passed, Cat_A_Points_Earned=Cat_A_Points_Earned, Cat_B_Points_Earned=Cat_B_Points_Earned, Result=Result, Odd_Semester_Average=Odd_Semester_Average, Even_Semester_Average=Even_Semester_Average, Supporting_Docs=Supporting_Docs, Result_Points = Result_Points)
        data2.save()  
        return redirect('/testing')
    else:
        return render(request, 'academics_1.html')

'''
def update_course_assign1(request,id):
    faculties = Faculty_Academics.objects.get(pk=id)
    if request.method == 'POST':
            print(request.POST)
            temp = 0
            #passing values to specific variable for easy calculation
            No_of_Schedule_Classes = request.POST['No_of_Schedule_Classes']
            No_of_Actually_Held_Classes = request.POST['No_of_Actually_Held_Classes']
            Average_Student_Feedback =  request.POST['Average_Student_Feedback'] 
            No_of_Students_Registered = request.POST['No_of_Students_Registered']
            No_of_Students_Passed = request.POST['No_of_Students_Passed']

            #points calculation 
            cat_a = (No_of_Actually_Held_Classes * 20) // No_of_Schedule_Classes

            if cat_a >= 20:
                cat_a = 20
            
            if Average_Student_Feedback >= 20:
                Average_Student_Feedback = 20
            
            result = (No_of_Students_Passed / No_of_Students_Registered) * 100

            if result >= 96.00 and result <= 100:
                temp = 10
            elif result >= 90.00 and result <= 95.99:
                temp = 9
            elif result >= 80.00 and result <= 89.99:
                temp = 8
            elif result >= 70.00 and result <= 79.99:
                temp = 7
            elif result >= 55.00 and result <= 69.99:
                temp = 5
            
                
            #updating data using variables
            result = (No_of_Students_Passed / No_of_Students_Registered) * 100
            faculties.No_of_Schedule_Classes = No_of_Schedule_Classes
            faculties.No_of_Actually_Held_Classes = No_of_Actually_Held_Classes
            faculties.Average_Student_Feedback = Average_Student_Feedback
            faculties.No_of_Students_Registered = No_of_Students_Registered
            faculties.No_of_Students_Passed = No_of_Students_Passed

            #updating calculation
            faculties.Cat_A_Points_Earned = cat_a
            faculties.Cat_B_Points_Earned = Average_Student_Feedback
            faculties.Result = result
            faculties.Result_Points = temp

            #saving updated data
            faculties.save()   
            return redirect('/show')
    context = {
        'faculties': faculties,
    }

    return render(request,'edit.html',context)
 

def faculty_development_approval(request):
    if request.method == 'POST':
        Category = request.POST['Category']
        Academic_Year = '2023-2024' #Change it every academic year
        Semester = request.POST['Semester']
        Activity = request.POST['Activity']
        Credit_Point = 0
        Criteria = request.POST['Criteria']
        Support_Document_No = request.POST['support_document_no']
        Verified_Status = "Pending"
        data = Faculty_Development(Category=Category, Academic_Year=Academic_Year, Semester=Semester, Activity=Activity, Credit_Point=Credit_Point, Criteria=Criteria, Support_Document_No=Support_Document_No, Verified_Status=Verified_Status)
        data.save()
        return redirect('home/')
    else:
        return render(request, 'faculty_document.html')


def report(request, id, year):
    year1 = year
    Faculty_Academics_Teaching_Process = Faculty_Academics.objects.filter(Id=id, Academic_Year = year).order_by("Semester")
    Faculty_Academics_Students_Feedback  = Faculty_Academics.objects.filter(Id=id, Academic_Year = year).order_by("Semester")
    Faculty_Development_Self_Development = Faculty_Development.objects.filter(Id=id, Academic_Year = year, Category = 'Self-Development').order_by("Semester")
    Faculty_Development_Institute_Development = Faculty_Development.objects.filter(Id=id, Academic_Year = year, Category = 'Institute/Departmental Responsibility').order_by("Semester")
    Faculty_Academics_ACR_Odd  = Faculty_Academics.objects.filter(Id=id, Academic_Year = year, Semester_Type = 'Odd').order_by("Semester")
    Faculty_Academics_ACR_Even  = Faculty_Academics.objects.filter(Id=id, Academic_Year = year, Semester_Type = 'Even').order_by("Semester")
    Faculty_Development_Society_Contribution = Faculty_Development.objects.filter(Id=id, Academic_Year = year, Category = 'Contribution to Society').order_by("Semester")
    return render(request,'report.html', {'academic_year':year1, 'Faculty_Academics_Teaching_Process':Faculty_Academics_Teaching_Process, 'Faculty_Academics_Students_Feedback':Faculty_Academics_Students_Feedback, 'Faculty_Development_Self_Development':Faculty_Development_Self_Development, 'Faculty_Development_Institute_Development':Faculty_Development_Institute_Development, 'Faculty_Academics_ACR_Odd':Faculty_Academics_ACR_Odd, 'Faculty_Academics_ACR_Even':Faculty_Academics_ACR_Even, 'Faculty_Development_Society_Contribution':Faculty_Development_Society_Contribution} )

'''

def points1(score):
    if score > 10:
        return 10
    return score

def points2(score):
    if score > 20:
        return 20
    return score

def sample(request):
    #Academics = Faculty_Academics.objects.filter(Faculty_Id = Id, Academic_Year = Year).order_by("Semester")
    testing = Faculty_Academics.objects.all().order_by("Semester")
    user = Faculty.objects.filter(Id='12345')
    Faculty_Academics_ACR_Odd  = Faculty_Academics.objects.filter(Semester_Type = 'Odd').order_by("Semester")
    Faculty_Academics_ACR_Even  = Faculty_Academics.objects.filter(Semester_Type = 'Even').order_by("Semester")
    Faculty_Development_Self_Development = Faculty_Development.objects.filter(Category = 'Self-Development').order_by("Semester")
    Faculty_Development_Institute_Development = Faculty_Development.objects.filter(Category = 'Institute/Departmental Responsibility').order_by("Semester")
    Faculty_Development_Society_Contribution = Faculty_Development.objects.filter(Category = 'Contribution to Society').order_by("Semester")
    scoreb = 0
    scorea = 0
    scorec = 0
    scored = 0
    scoree = 0
    scoref = 0
    for i in range(len(testing)):
        if testing[i].Cat_A_Points_Earned >= 10:
            scorea += 10
        else:
            scorea += testing[i].Cat_A_Points_Earned
        
        if testing[i].Cat_B_Points_Earned >= 10:
            scoreb += 10
        else:
            scoreb += testing[i].Cat_B_Points_Earned

    #result calculation
    scored_odd = 0
    scored_even = 0
    for semester in range(len(Faculty_Academics_ACR_Odd)):
        scored_odd += Faculty_Academics_ACR_Odd[semester].Result_Points 

    for semester in range(len(Faculty_Academics_ACR_Even)):
        scored_even += Faculty_Academics_ACR_Even[semester].Result_Points
    
    scored = points1(scored_odd) + points1(scored_even)
    
    for j in range(len(Faculty_Development_Self_Development)):
        if Faculty_Development_Self_Development[j].Credit_Point >= 10:
            scorec += 10
        else:
            scorec += Faculty_Development_Self_Development[i].Credit_Point
    
    for k in range(len(Faculty_Development_Institute_Development)):
        if Faculty_Development_Institute_Development[k].Credit_Point >= 10:
            scored += 10
        else:
            scored += Faculty_Development_Institute_Development[i].Credit_Point

    for m in range(len(Faculty_Development_Society_Contribution)):
        if Faculty_Development_Society_Contribution[m].Credit_Point >= 10:
            scoref += 10
        else:
            scoref = Faculty_Development_Society_Contribution[i].Credit_Point

    if scorec > 20:
        scorec = 20
    if scored > 10:
        scored = 10
    if scoree > 10:
        scoree = 10

    #data = Every_Academic_Report(Faulty_Id = Id, Faculty_Name = user.Name, Academic_Year = Year, Teaching_Process = Teaching_Process, Students_Feedback = Students_Feedback, Departmental_Activities = Departmental_Activities,)
    return render(request,'test.html',{'testing':testing, 'year':testing[0].Academic_Year, 'Department':user[0].Department, 'scorea':points2(scorea), 'scoreb':points2(scoreb)})


'''
academic year
faculty id
'''
