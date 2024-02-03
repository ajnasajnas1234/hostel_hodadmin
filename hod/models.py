from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid




class  Login(models.Model):
    Username=models.CharField(max_length=200,null=True)
    Password=models.CharField(max_length=500,null=True)
    Role=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.Username







class Noticeboard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='hostelmanagment_noticeboard',null=True)    
    Title=models.CharField(max_length=200,null=True)
    Content=models.CharField(max_length=500,null=True)
    Date=models.DateField(null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Title

   


class  Department(models.Model):
    Department_name=models.CharField(max_length=200,null=True)
    Department_description=models.CharField(max_length=500,null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Department_name




class Hod_registration(models.Model):
    dpt=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hod_registration')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='hostelmanagment_hod_registrations')
    Department_name=models.CharField(max_length=200,null=True)
    Name=models.CharField(max_length=200,null=True)
    Position=models.CharField(max_length=200,null=True)
    Email=models.EmailField(null=True)
    Contact_no=models.IntegerField(null=True)
    Photo=models.ImageField(upload_to='images/')
    Proof=models.ImageField(upload_to='images/')
    Username=models.CharField(max_length=200,null=True)
    Password1=models.CharField(max_length=200,null=True)
    Password2=models.CharField(max_length=200,null=True)
    Status=models.CharField(max_length=100)
    Role=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    



class  Course(models.Model):
    dpt =models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    Course_name=models.CharField(max_length=200,null=True)
    Department_name=models.CharField(max_length=200,null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Course_name





class Block(models.Model):
    Block_name=models.CharField(max_length=200,null=True)
    Block_description=models.CharField(max_length=500,null=True)
    Status=models.CharField(max_length=100)

    # def __str__(self):
    #     return self.Block_name


class Room_type(models.Model):
    Room_type=models.CharField(max_length=200,null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Room_type



class Room(models.Model):
    block=models.ForeignKey(Block,on_delete=models.CASCADE,null=True)
    room=models.ForeignKey(Room_type,on_delete=models.CASCADE,null=True)
    Block_name=models.CharField(max_length=200,null=True)
    Room_number=models.CharField(max_length=200,null=True)
    Rooms_type=models.CharField(max_length=200,null=True)
    Max_accommodation=models.IntegerField(null=True)
    Vaccancy=models.IntegerField(null=True,blank=True,default=0)
    Amount=models.IntegerField(null=True)
    Status=models.CharField(max_length=100)

    # def __str__(self):
    #     return self.Room_number



class Category(models.Model):
   Category=models.CharField(max_length=200,null=True)
   Status=models.CharField(max_length=100)

   def __str__(self):
        return self.Category





class Admission_fee(models.Model):
    Caution_deposit=models.IntegerField(null=True)
    Registration_amenities=models.IntegerField(null=True)
    Mess_advance_fee=models.IntegerField(null=True)
    Amount_for_concession=models.IntegerField(null=True)
    Amount_for_oec=models.IntegerField(null=True)
    Amount_for_non_concession=models.IntegerField(null=True)
    Status=models.CharField(max_length=100)







class Student(models.Model):
    log_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    dpt=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    block=models.ForeignKey(Block,on_delete=models.CASCADE,null=True)
    Categoryname=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    room_type=models.ForeignKey(Room_type,on_delete=models.CASCADE,null=True)
    Student_name=models.CharField(max_length=200)
    Address=models.CharField(max_length=500,null=True)
    State=models.CharField(max_length=200,null=True)
    Street=models.CharField(max_length=200,null=True)
    District=models.CharField(max_length=200,null=True)
    Country=models.CharField(max_length=200,null=True)
    Pincode=models.IntegerField(null=True)
    Guardian_name=models.CharField(max_length=200,null=True)
    Student_phone=models.IntegerField(null=True)
    Guardian_phone=models.IntegerField(null=True)
    Email=models.EmailField(null=True)
    Religion=models.CharField(max_length=200,null=True)
    Caste=models.CharField(max_length=200,null=True)
    Concession=models.CharField(max_length=200,null=True)
    DOB=models.DateField(null=True)
    Distance_from_home=models.IntegerField(null=True)
    Year_of_admission=models.DateField(null=True)
    Room_type=models.CharField(max_length=200,null=True)
    Room_no=models.CharField(max_length=200,null=True)
    Documents=models.FileField(null=True)
    Photo=models.FileField(null=True)
    Course_name=models.CharField(max_length=200,null=True)
    Department_name=models.CharField(max_length=200,null=True)
    Block_name=models.CharField(max_length=200,null=True)
    Category_name=models.CharField(max_length=200,null=True)
    Status=models.CharField(max_length=100)
    Place=models.CharField(max_length=200,null=True)
    Gender=models.CharField(max_length=200,null=True)
    Admission_no=models.IntegerField(null=True)
    Post=models.CharField(max_length=200,null=True)
    Admission_fees=models.IntegerField(null=True)

    # def __str__(self):
    #     return self.Student_name

    






class Complaint(models.Model):
    dpt=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    block=models.ForeignKey(Block,on_delete=models.CASCADE,null=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    Date=models.DateField(null=True)
    Complaint_description=models.CharField(max_length=500,null=True)
    Reply=models.CharField(max_length=500,null=True,default="no reply")
    Title=models.CharField(max_length=500,null=True)
    Department_name=models.CharField(max_length=200,null=True)
    Block_name=models.CharField(max_length=200,null=True)
    Student_name=models.CharField(max_length=200,null=True)
    Room_no=models.CharField(max_length=200,null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Title


    



class MessComplaint(models.Model):
    block=models.ForeignKey(Block,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    Date=models.DateField(null=True)
    Complaint_description=models.CharField(max_length=500,null=True)
    Reply=models.CharField(max_length=500,null=True,default="no reply")
    Title=models.CharField(max_length=500,null=True)
    Block_name=models.CharField(max_length=200,null=True,blank=True)
    Student_name=models.CharField(max_length=200,null=True,blank=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Title


    
class Room_request(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    dpt=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    Department_name=models.CharField(max_length=200,null=True)
    Date=models.DateField(null=True)
    Verification_status=models.CharField(max_length=100,null=True)
    Admission_no=models.IntegerField(null=True)
    Student_name= models.CharField(max_length=200,null=True)
    Distance_from_home=models.IntegerField(null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Student_name

    







# class Mess_fee(models.Model):
#     student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
#     dpt=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
#     Paid_date=models.DateField(null=True)
#     No_of_days_present=models.IntegerField(null=True)
#     Mess_fee=models.IntegerField(null=True)
#     # Fine=models.IntegerField(null=True)
#     Total=models.IntegerField(null=True)
#     Month_year=models.DateField(null=True)
#     Department_name=models.CharField(max_length=200,null=True)
#     Student_name=models.CharField(max_length=200,null=True)
#     Status=models.CharField(max_length=100)





class Room_rent(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    dpt=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    Payment_status=models.CharField(max_length=50,null=True)
    Date=models.DateField(null=True)
    Rent=models.IntegerField(null=True,default=80)
    Status=models.CharField(max_length=100)
    block=models.ForeignKey(Block,on_delete=models.CASCADE,null=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    Block_name=models.CharField(max_length=200,null=True,blank=True)
    Student_name=models.CharField(max_length=200,null=True,blank=True)
    Room_number=models.CharField(max_length=200,null=True,blank=True)
    Department_name=models.CharField(max_length=200,null=True,blank=True)
    Month=models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.Student_name




class Coupon(models.Model):
    Type=models.CharField(max_length=200,null=True)
    Amount=models.CharField(max_length=200,null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Type



class Coupon_generate(models.Model):
    Issued_date=models.DateField(null=True)
    Amount=models.FloatField(null=True)
    Type=models.CharField(max_length=200,null=True)
    Student_name=models.CharField(max_length=200,null=True)
    coupon=models.ForeignKey(Coupon,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Student_name

    



class Guest_coupon(models.Model):
    Guest_name=models.CharField(max_length=100,null=True)
    Issued_date=models.DateField(null=True)
    Type=models.CharField(max_length=200,null=True)
    coupon=models.ForeignKey(Coupon,on_delete=models.CASCADE,null=True)
    Amount=models.CharField(max_length=200,null=True)
    Start_date=models.DateField(null=True)
    End_date=models.DateField(null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return str(self.Guest_name)

    


class Expenditure(models.Model):
    Year=models.IntegerField(max_length=100,null=True)
    Month=models.IntegerField(max_length=100,null=True)
    Total_Purchase=models.FloatField(null=True)
    Opening_stock=models.FloatField(null=True)
    Closing_stock=models.FloatField(null=True)
    Net_purchase=models.FloatField(null=True)
    Guest_coupon_charge=models.IntegerField(null=True)
    Total_mess_attendance=models.IntegerField(null=True)
    Total_mess_expenditure=models.FloatField(null=True)
    Pay_per_expense=models.FloatField(null=True)
    Salary=models.FloatField(null=True)
    Pf=models.FloatField(null=True)
    Mis=models.FloatField(null=True)
    Audit_fee=models.FloatField(null=True)
    Printing_Stationary=models.FloatField(null=True)
    Other_expense=models.FloatField(null=True)
    Total_fixed_expenditure=models.FloatField(null=True)
    No_of_inmates=models.IntegerField(null=True)
    Expense_per_inmates=models.FloatField(null=True)
    Status=models.CharField(max_length=100)
    
    
    amt=models.ForeignKey(Guest_coupon,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return str(self.Expense_per_inmates)
   




class Room_registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='hostelmanagment_room_registrations')
    Name=models.CharField(max_length=200,null=True)
    DOB=models.DateField(null=True)
    Email=models.EmailField(null=True)
    Phone_no=models.IntegerField(null=True)
    Address=models.CharField(max_length=500,null=True)
    Photo=models.ImageField(upload_to='images/')
    Proof=models.ImageField(upload_to='images/')
    Username=models.CharField(max_length=200,null=True)
    Password1=models.CharField(max_length=200,null=True)
    Password2=models.CharField(max_length=200,null=True)
    Status=models.CharField(max_length=100)
    Role=models.CharField(max_length=100)

    def __str__(self):
        return self.Name





class Mess_registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=200,null=True)
    DOB=models.DateField(null=True)
    Email=models.EmailField(null=True)
    Phone_no=models.IntegerField(null=True)
    Address=models.CharField(max_length=500,null=True)
    Photo=models.ImageField(upload_to='images/')
    Proof=models.ImageField(upload_to='images/')
    Username=models.CharField(max_length=200,null=True)
    Password1=models.CharField(max_length=200,null=True)
    Password2=models.CharField(max_length=200,null=True)
    Status=models.CharField(max_length=100)
    Role=models.CharField(max_length=100)


    def __str__(self):
        return self.Name
    


class Feedback(models.Model):
     Feedback=models.CharField(max_length=500,null=True)
     Date=models.DateField(null=True)
     Feedback_title=models.CharField(max_length=200,null=True)
     Student_name=models.CharField(max_length=200,null=True,blank=True)
     Department_name=models.CharField(max_length=200,null=True,blank=True)
     Status=models.CharField(max_length=100)
     dpt=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
     student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
          
     def __str__(self):
        return self.Feedback_title
    


class Mess_track(models.Model):
    
    Mess_in_date=models.CharField(max_length=50,null=True,blank=True)
    Mess_out_date=models.CharField(max_length=50,null=True,blank=True)
    In_or_out=models.CharField(max_length=50,null=True,blank=True)
    Time=models.CharField(max_length=50,null=True,blank=True)
    Department_name=models.CharField(max_length=200,null=True,blank=True)
    Student_name=models.CharField(max_length=200,null=True,blank=True)
    Status=models.CharField(max_length=100,blank=True)
    dpt=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    Date=models.CharField(max_length=50,null=True,blank=True)
    Block_name=models.CharField(max_length=200,null=True,blank=True)
    block=models.ForeignKey(Block,on_delete=models.CASCADE,null=True,blank=True)
    Mess_in_count=models.IntegerField(null=True,blank=True)
    Mess_out_count=models.IntegerField(null=True,blank=True)
    Students_present=models.IntegerField(null=True,blank=True)
    Month=models.CharField(max_length=200,null=True,blank=True)
    Fee=models.CharField(max_length=200,null=True,blank=True)




class Deallocation_Request(models.Model):
    dpt=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    block=models.ForeignKey(Block,on_delete=models.CASCADE,null=True)
    # Categoryname=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    # course_name=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    Reason=models.CharField(max_length=100,null=True)
    Date=models.DateField(max_length=100,null=True)
    Block_name=models.CharField(max_length=200,null=True)
    Student_name=models.CharField(max_length=200,null=True)
    Room_number=models.CharField(max_length=200,null=True)
    Department_name=models.CharField(max_length=200,null=True)
    # Course=models.CharField(max_length=200,null=True)
    Payment_status=models.CharField(max_length=50,null=True)
    Status=models.CharField(max_length=100)





class  Hod_student(models.Model):
    hod=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Student_name=models.CharField(max_length=200,null=True)
    Admission_no=models.CharField(max_length=500,null=True)
    Joining_date=models.DateField(null=True)
    Status=models.CharField(max_length=100)


    def __str__(self):
        return self.Student_name




class Transient(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)  
    Name=models.CharField(max_length=200,null=True)
    Message=models.CharField(max_length=500,null=True)
    Role=models.CharField(max_length=100,null=True)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Name



class Room_fee(models.Model):
    Month=models.CharField(max_length=200,null=True)
    Amount=models.IntegerField(null=True)
    Status=models.CharField(max_length=100)


    def __str__(self):
        return self.Month
   
