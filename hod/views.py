from django.shortcuts import get_object_or_404,render,redirect
from . import models
import calendar
import pytz
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.contrib.auth import authenticate,login as auth_login
from .models import Admission_fee,Student,Room_fee,Transient,Complaint,MessComplaint,Department,Coupon_generate,Guest_coupon,Course,Hod_student,Category,Noticeboard,Expenditure,Hod_registration,Room_registration,Mess_registration,Coupon,Block,Room,Room_type,Student,Feedback,Deallocation_Request,Mess_track,Room_rent
from django.db.models import Sum
from django.utils.timezone import make_aware
from django.db.models import Q, Sum, IntegerField, Value
from django.db.models.functions import Coalesce

# Create your views here.

# admin
def login_page(request):
    return render(request,'admins/login.html')

def admin_index(request):
    return render(request,'admins/index.html')

def forgot_password(request):
    return render(request,'admins/auth-forgot-password-basic.html')

def admin_admission_fee(request):
    data=Admission_fee.objects.all()
    return render(request,'admins/admissionfees.html',{'data':data})

def admin_courses(request):
    data=Course.objects.all()
    return render(request,'admins/courses.html',{'data':data})

def dashboard(request):
    return render(request,'admins/dashboard.html')

def admin_page(request):
    data=Mess_registration.objects.all()
    return render(request,'admins/admin.html',{'data':data})

def room_admin_page(request):
    data=Room_registration.objects.all()
    return render(request,'admins/roomadmin.html',{'data':data})

def admin_departments(request):
    data=Department.objects.all()
    return render(request,'admins/departments.html',{'data':data})

def admin_hod(request):
    data=Hod_registration.objects.all()
    return render(request,'admins/hod.html',{'data':data})

def hod_resign(request):
    data=Hod_registration.objects.all()
    return render(request,'admins/hodresignation.html',{'data':data})

def mess_resign(request):
    data=Mess_registration.objects.all()
    return render(request,'admins/messadminresignation.html',{'data':data})

def mess_complaint(request):
    return render(request,'admins/messcomplaints.html')

def admin_mess_fee(request):
    return render(request,'admins/messfees.html')

def admin_noticeboard(request):
    data=Noticeboard.objects.all()
    return render(request,'admins/noticeboard.html',{'data':data})

def room_resign(request):
    data=Room_registration.objects.all()
    return render(request,'admins/roomadminresignation.html',{'data':data})

def room_complaints(request):
    return render(request,'admins/roomcomplaints.html')

def admin_room_rent(request):
    return render(request,'admins/roomrent.html')

# def admin_students(request):
#     data=Student.objects.all()
#     return render(request,'admins/students.html',{'data':data})

def admin_view_room(request):
    return render(request,'admins/viewroom.html')

def hod_portal(request):
    data=Hod_registration.objects.all()
    return render(request,'admins/hodlogin.html',{'data':data})

def mess_portal(request):
    data=Mess_registration.objects.all()
    return render(request,'admins/messlogin.html',{'data':data})

def room_portal(request):
    data=Room_registration.objects.all()
    return render(request,'admins/roomlogin.html',{'data':data})


def admin_category(request):
    data=Category.objects.all()
    return render(request,'admins/category.html',{'data':data})

def transient_messages(request):
    data=Transient.objects.all()
    return render(request,'admins/messages.html',{'data':data})




# hod



def hod_index(request):
    return render(request,'hod/index2.html')

def hod_notifications(request):
    data=Noticeboard.objects.all()
    return render(request,'hod/notifications.html',{'data':data})


def student_details(request):
    data=Hod_student.objects.all()    
    return render(request,'hod/studentdetails.html',{'data':data})

def hod_transient(request):
    data=Transient.objects.all()
    return render(request,'hod/transient.html',{'data':data})

def hod_verification(request):
    data=Student.objects.all()
    return render(request,'hod/verification.html',{'data':data})

def add_student(request):
    data=Hod_student.objects.all()
    return render(request,'hod/addstudent.html',{'data':data})



# mess_admin

def approval(request):
    data=Deallocation_Request.objects.all()
    return render(request,'mess_admin/approval.html',{'data':data})

def mess_coupon_generate(request):
    data=Coupon_generate.objects.all()
    return render(request,'mess_admin/coupon.html',{'data':data})

def coupon_fee(request):
    data=Guest_coupon.objects.all()
    return render(request,'mess_admin/couponfee.html',{'data':data})

def coupon_add(request):
    data=Coupon.objects.all()
    return render(request,'mess_admin/coupongenerate.html',{'data':data})
    
def mess_guest_coupon(request):
    data=Guest_coupon.objects.all()
    return render(request,'mess_admin/guest.html',{'data':data})

def expense(request):
    data=Expenditure.objects.all()
    return render(request,'mess_admin/viewexpense.html',{'data':data})

def mess_feedback(request):
    data=Feedback.objects.all()
    return render(request,'mess_admin/feedback.html',{'data':data})

def inandout(request):
    return render(request,'mess_admin/inandout.html')

def mess_index(request):
    return render(request,'mess_admin/index.html')

def fee_mess(request):
    return render(request,'mess_admin/messfee.html')

def track_mess(request):
    data=Mess_track.objects.all()
    return render(request,'mess_admin/messtrack.html',{'data':data})

def mess_notification(request):
    data=Noticeboard.objects.all()
    return render(request,'mess_admin/notification.html',{'data':data})

def mess_reply_complaint(request):
    data=MessComplaint.objects.all()
    return render(request,'mess_admin/replycomplaint.html',{'data':data})

def mess_transient(request):
    data=Transient.objects.all()
    return render(request,'mess_admin/resign.html',{'data':data})

def mess_view_complaint(request):
    data=MessComplaint.objects.all()
    return render(request,'mess_admin/viewcomplaint.html',{'data':data})

def mess_student(request):
    data=Student.objects.all()
    return render(request,'mess_admin/viewstudent.html',{'data':data})



# room_admin

def room_block(request):
    data=Block.objects.all()
    return render(request,'room_admin/block.html',{'data':data})

def room_deallocation_request(request):
    data=Deallocation_Request.objects.all()
    return render(request,'room_admin/deallocationrequest.html',{'data':data})

def room_notification(request):
    data=Noticeboard.objects.all()
    return render(request,'room_admin/notification.html',{'data':data})

def room_feedback(request):
    data=Feedback.objects.all()
    return render(request,'room_admin/feedback.html',{'data':data})

def room_index(request):
    return render(request,'room_admin/index.html')

def room_reply_complaint(request):
    data=Complaint.objects.all()
    return render(request,'room_admin/replycomplaint2.html',{'data':data})

def room_transient(request):
    data=Transient.objects.all()
    return render(request,'room_admin/resignation.html',{'data':data})

def room_view_room(request):
    data=Room.objects.all()
    return render(request,'room_admin/room.html',{'data':data})

def rent_room(request):
    data=Room_rent.objects.all()
    return render(request,'room_admin/roomrent.html',{'data':data})

def request_room(request):
    data=Student.objects.all()
    print(data)
    return render(request,'room_admin/roomrequest.html',{'data':data})

def room_student(request):
    data=Student.objects.all()
    return render(request,'room_admin/student.html',{'data':data})

def room_view_complaint(request):
    data=Complaint.objects.all()
    return render(request,'room_admin/viewcomplaint1.html',{'data':data})

def roomadmin_roomtype(request):
    data=Room_type.objects.all()
    return render(request,'room_admin/roomtype.html',{'data':data})

def allocation(request):
    data=Student.objects.all()
    return render(request,'room_admin/roomallocation.html',{'data':data})

def deallocation(request):
    data=Deallocation_Request.objects.all()
    return render(request,'room_admin/deallocation.html',{'data':data}) 

def room_fee(request):
    data=Room_fee.objects.all()
    return render(request,'room_admin/roomfee.html',{'data':data})        








def hod_register(request):
    if request.method == 'POST' and request.FILES:
        name = request.POST.get('name')
        print(name)
        position = request.POST.get('position')
        print(position)
        email = request.POST.get('email')
        print(email)
        contact = request.POST.get('phone')
        print(contact)
        department = request.POST.get('department')
        print(department)
        username = request.POST.get('username')
        print(username)
        password1 = request.POST.get('password1')
        print(password1)
        password2 = request.POST.get('password2')
        print(password2)
        photo = request.FILES.get('photo')
        proof = request.FILES.get('identity')
        role = 'hod'
        status = "0"
        dept = Department.objects.filter(Department_name=department).first()

        # Check if all required fields are present
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # Username already exists
                return redirect('hod_portal')
            elif User.objects.filter(email=email).exists():
                # Email already exists
                return redirect('hod_portal')
            elif len(contact) != 10 or not contact.isdigit():
                # Invalid contact number
                return redirect('hod_portal')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()

        userDetail = models.Hod_registration(user=user,dpt=dept, Department_name=dept.Department_name,Name=name,Position=position, Email=email,Contact_no=contact, Photo=photo, Proof=proof, Role=role,Status=status)
                                           
        userDetail.save()

        messages.success(request, 'User created successfully')
        return redirect('login_page')

    else:
        return render(request, 'admins/hodlogin.html')




# room registration

def room_register(request):
    if request.method == 'POST' and request.FILES:
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        contact = request.POST.get('phone')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        photo = request.FILES['photo']
        proof = request.FILES['identity']
        role = 'room'
        status = "0"

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # Username already exists
                return redirect('room_portal')
            elif User.objects.filter(email=email).exists():
                # Email already exists
                return redirect('room_portal')
            elif len(contact) != 10 or not contact.isdigit():
                # Invalid contact number
                return redirect('room_portal')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()

                userDetail = models.Room_registration(
                    user=user,
                    Name=name,
                    Email=email,
                    Phone_no=contact,
                    DOB=dob,
                    Address=address,
                    Role=role,
                    Photo=photo,
                    Proof=proof,
                    Status=status
                )
                userDetail.save()

                print('User created successfully')
        else:
            # Passwords do not match
            return redirect('room_portal')

        return redirect('login_page')
    else:
        return render(request, 'admins/roomlogin.html')









# mess registration


def mess_register(request):
        if request.method == 'POST' and request.FILES:
            name = request.POST.get('name')
            dob = request.POST.get('dob')
            email = request.POST.get('email')
            contact = request.POST.get('phone')
            address = request.POST.get('address')
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            photo = request.FILES['photo']
            proof = request.FILES['identity']
            role = 'mess'
            status = "0"

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    # Username already exists
                    return redirect('mess_portal')
                elif User.objects.filter(email=email).exists():
                    # Email already exists
                    return redirect('mess_portal')
                elif len(contact) != 10 or not contact.isdigit():
                    # Invalid contact number
                    return redirect('mess_portal')
                else:
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()

                    userDetail = models.Mess_registration(
                        user=user,
                        Name=name,
                        Email=email,
                        Phone_no=contact,
                        DOB=dob,
                        Address=address,
                        Role=role,
                        Photo=photo,
                        Proof=proof,
                        Status=status
                    )
                    userDetail.save()

                    print('User created successfully')
            else:
                # Passwords do not match
                return redirect('mess_portal')

            return redirect('login_page')
        else:
            return render(request, 'admins/messlogin.html')








# department

def admin_add_department(request):
    if request.method == 'POST':

        department_name = request.POST.get('department')
        department_description = request.POST.get('description')
        status="0"

        deptDetail = models.Department(Department_name=department_name , Department_description=department_description, Status=status)
        deptDetail.save()
        print(deptDetail)
        print('department added')
        return render(request,'admins/departments.html')
    else:
        return render(request,'admins/departments.html')



# course


def admin_add_course(request):
    if request.method == 'POST':
        dpt = request.POST.get('department')
        print(dpt)
        course_name = request.POST.get('course')
        status = "0"

        dept = Department.objects.filter(Department_name=dpt).first()
        print(dept)

        if dept:
            courseDetail = models.Course(dpt=dept, Course_name=course_name, Department_name=dept.Department_name, Status=status)
            courseDetail.save()
            print(courseDetail)
            print('course added')
            return render(request, 'admins/courses.html')

        print('Department not found')
        return render(request, 'admins/courses.html')

    else:
        return render(request, 'admins/courses.html')




# noticeboard


def admin_add_notice(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Get the current date and time
        date = datetime.now().date()
        status = "0"

        noticeDetail = models.Noticeboard(user=user, Title=title, Content=content, Date=date, Status=status)
        noticeDetail.save()
        print(noticeDetail)
        print('notice added')
        return render(request, 'admins/noticeboard.html')
    else:
        return render(request, 'admins/noticeboard.html')



def admin_delete_notice(request,id):
    delmember = Noticeboard.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('admin_noticeboard')





# expenditure

def mess_add_expenditure(request):
    if request.method == 'POST':
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        print("==========year", year)
        print("-----------month", month)
        total = request.POST.get('total')
        if total.isdigit():
            t_p = int(total)
            print("-----------t_p", t_p)
        else:
            t_p = 0

        opening_stock = request.POST.get('opening')
        if opening_stock.isdigit():
            open_s = int(opening_stock)
            print("-----------open_s", open_s)
        else:
            open_s = 0

        closing_stock = request.POST.get('closing')
        if closing_stock.isdigit():
            close_s = int(closing_stock)
            print("-----------close_s", close_s)
        else:
            close_s = 0

        net_purchase = t_p + open_s - close_s
        net = int(net_purchase)
        print("]]]]]]]]]]]]]]]", net)

        start_date = make_aware(datetime(year, month, 1))
        print("-----------start_date", start_date)

        # Calculate the next month's start date
        if month == 12:
            end_month = 1
            end_year = year + 1
        else:
            end_month = month + 1
            end_year = year
        end_date = make_aware(datetime(end_year, end_month, 1))
        print("-----------end_date", end_date)



        guest = Guest_coupon.objects.filter(
        Q(Issued_date__gt=start_date) & Q(Issued_date__lt=end_date))

        Guest_coupon_charge = guest.aggregate(Amount=Coalesce(Sum('Amount', output_field=IntegerField()), Value(0)))

        g_coupon = int(Guest_coupon_charge['Amount'])
        print("----------Guest_coupon_charge", g_coupon)

        total_mess_attendance_result = Mess_track.objects.filter((Q(Mess_in_date__gt=start_date) & Q(Mess_out_date__lt=end_date)) |(Q(Mess_in_date__gte=start_date) & Q(Status=0)) |(Q(Mess_out_date__lt=end_date) & Q(Status=0))).aggregate(Date=Coalesce(Sum('Date', output_field=IntegerField()), Value(0)))

        total_mess_attendance = total_mess_attendance_result['Date']
        print("-----------total_mess_attendance", total_mess_attendance)


        total_mess_expenditure = net - g_coupon
        t_expense = int(total_mess_expenditure)
        
        pay = t_expense / total_mess_attendance if total_mess_attendance != 0 else 0
        pay_per_expense = int(pay)
        print("///////////", pay_per_expense)

        salary = request.POST.get('salary')
        if salary.isdigit():
            sal = int(salary)
            print("///////////sal", sal)
        else:
            sal = 0

        pf = request.POST.get('pf')
        if pf.isdigit():
            p_fund = int(pf)
            print("///////p_fund////", p_fund)
        else:
            p_fund = 0

        mis = request.POST.get('misc')
        if mis.isdigit():
            miscell = int(mis)
            print("///////miscell////", miscell)
        else:
            miscell = 0

        audit_fee = request.POST.get('audit')
        if audit_fee.isdigit():
            a_f = int(audit_fee)
            print("///////a_f////", a_f)
        else:
            a_f = 0

        printing_stationary = request.POST.get('print')
        if printing_stationary.isdigit():
            print_s = int(printing_stationary)
            print("///////print_s////", print_s)
        else:
            print_s = 0

        other_expense = request.POST.get('other')
        if other_expense.isdigit():
            other_e = int(other_expense)
            print("///////other_e////", other_e)
        else:
            other_e = 0

        total_amount = sal + p_fund + miscell + a_f + print_s + other_e

        no_of_inmates = request.POST.get('inmate')
        if no_of_inmates.isdigit():
            inmates = int(no_of_inmates)
            print("///////inmates////", inmates)
        else:
            inmates = 0

        if inmates != 0:
            expense = total_amount / inmates
            expense_per_inmate = int(expense)
            print("///////expense_per_inmate////", expense_per_inmate)
        else:
            expense_per_inmate = 0

        status = "0"

        utc_timezone = pytz.UTC

        _, num_days = calendar.monthrange(year, month)
        print("//days",num_days)

        student_entries = Mess_track.objects.all()

        for entry in student_entries:
            student_id = entry.student.id
            status = entry.student.Status
            mess_in_date = entry.Mess_in_date
            date_o = datetime.strptime(mess_in_date, "%Y-%m-%d")
            mess_in = date_o.day
            mess_out_date = entry.Mess_out_date
            date_ob = datetime.strptime(mess_out_date, "%Y-%m-%d")
            mess_out = date_ob.day
            no_days = entry.Date
            n_day = int(no_days)
            n_day += 1
            
            mess_in_date_aware = utc_timezone.localize(date_o)
            mess_out_date_aware = utc_timezone.localize(date_ob)

            if mess_in_date_aware > start_date and mess_out_date_aware < end_date:
                mess_fee = n_day * int(pay_per_expense)
            elif mess_in_date_aware <= start_date and mess_out_date_aware >= end_date:
                mess_fee = num_days * int(pay_per_expense)
            elif mess_in_date_aware <= start_date and mess_out_date_aware <= end_date:
                mess_fee = mess_out * int(pay_per_expense)
            elif mess_in_date_aware > start_date and mess_out_date_aware >= end_date:
                days = num_days - mess_in
                mess_fee = days * int(pay_per_expense)
            elif mess_in_date_aware >= start_date and mess_out_date_aware >=end_date:
                dayys = num_days - mess_in
                mess_fee = dayys * int(pay_per_expense)
            
            sg = Mess_track.objects.get(student=student_id)
            sg.Fee=mess_fee
            sg.save()
            print(f"Student ID: {student_id}, Mess in date: {mess_in_date}, Mess out date: {mess_out_date}, Mess Fee: {mess_fee}")


        userDetail = models.Expenditure(
            Year=year,
            Month=month,  # Pass the month number instead of datetime object
            Total_Purchase=total,
            Opening_stock=opening_stock,
            Closing_stock=closing_stock,
            Net_purchase=net_purchase,
            Guest_coupon_charge=g_coupon,
            Total_mess_attendance=total_mess_attendance,
            Total_mess_expenditure=total_mess_expenditure,
            Pay_per_expense=pay_per_expense,
            Salary=salary,
            Pf=pf,
            Mis=mis,
            Audit_fee=audit_fee,
            Printing_Stationary=printing_stationary,
            Total_fixed_expenditure=total,
            Other_expense=other_expense,
            No_of_inmates=no_of_inmates,
            Expense_per_inmates=expense_per_inmate,
        )
        userDetail.save()
        print(userDetail)
        print('expenditure added')

        return render(request, 'mess_admin/expense.html')
    else:
        return render(request, 'mess_admin/expense.html')


# coupon add

def coupon_add_mess(request):
    if request.method == 'POST':

        coupon_type = request.POST.get('type')
        amount = request.POST.get('price')
        print(amount)

        status="0"

        userDetail = models.Coupon(Type=coupon_type, Amount=amount,Status=status)
        userDetail.save()
        print(userDetail)
        print('coupon added')
        return render(request,'mess_admin/coupongenerate.html')
    else:
        return render(request,'mess_admin/coupongenerate.html')





# mess notice


def mess_add_notice(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Get the current date and time
        date = datetime.now().date()
        status = "0"

        noticeDetail = models.Noticeboard(user=user, Title=title, Content=content, Date=date, Status=status)
        noticeDetail.save()
        print(noticeDetail)
        print('notice added')
        return render(request, 'mess_admin/notification.html')
    else:
        return render(request, 'mess_admin/notification.html')





# room notice


def room_add_notice(request):
   if request.method == 'POST':

        user = request.POST.get('user')
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Get the current date and time
        date = datetime.now().date()
        status = "0"

        noticeDetail = models.Noticeboard(user=user, Title=title, Content=content, Date=date, Status=status)
        noticeDetail.save()
        print(noticeDetail)
        print('notice added')
        return render(request, 'room_admin/notification.html')



# room block


def room_add_block(request):
    if request.method == 'POST':

        block_name = request.POST.get('block')
        block_description = request.POST.get('description')
        status="0"

        blockDetail = models.Block(Block_name=block_name , Block_description=block_description, Status=status)
        blockDetail.save()
        print(blockDetail)
        print('block added')
        return render(request,'room_admin/block.html')
    else:
        return render(request,'room_admin/block.html')




# view room

def roomadmin_add_room(request):
    if request.method == 'POST':
        
        room_no = request.POST.get('room_no')
        block = request.POST.get('block')
        room = request.POST.get('type')
        max_accomodation = request.POST.get('max_acco')
        vaccancy = request.POST.get('vaccancy')
        amount = request.POST.get('amount')
        status = "0"

        blk = Room.objects.filter(Block_name=block).values()
        rmtyp = Room.objects.filter(Rooms_type=room).values()


        if blk and rmtyp:
            roomDetail = models.Room(block=blk, Room_number=room_no,Vaccancy=vaccancy, Block_name=blk.Block_name, room=room, Rooms_type=rmtyp.Rooms_type, Max_accommodation=max_accomodation,  Amount=amount, Status=status)
            roomDetail.save()
            print(roomDetail)
            print('room added')
            return render(request, 'room_admin/room.html')

        print('room not found')
        return render(request, 'room_admin/room.html')

    else:
        return render(request, 'room_admin/room.html')





# generate coupon


def mess_generate_coupon(request):
     if request.method == 'POST' and request.FILES:

        coupon_type = request.POST.get('coupon_type')
        amount = request.POST.get('amount')
        status="0"

        userDetail = models.userDetails(Type=coupon_type, Amount=amount)
        userDetail.save()
        print(userDetail)
        print('coupon generated')
        return render(request,'mess_admin/coupon.html')


     else:
        return render(request,'mess_admin/coupon.html')




# category


def admin_add_category(request):
    if request.method == 'POST':

        category = request.POST.get('category')
        status="0"

        catDetail = models.Category(Category=category , Status=status)
        catDetail.save()
        print(catDetail)
        print('category added')
        return render(request,'admins/category.html')
    else:
        return render(request,'admins/category.html')




# room type


def roomadmin_add_roomtype(request):
    if request.method == 'POST':

        room_type = request.POST.get('room_type')
        status="0"

        typeDetail = models.Room_type(Room_type=room_type , Status=status)
        typeDetail.save()
        print(typeDetail)
        print('type added')
        return render(request,'room_admin/roomtype.html')
    else:
        return render(request,'room_admin/roomtype.html')




# hod student
def hod_add_student_details(request):
    if request.method == "POST":
        student_name = request.POST.get('student_name')
        admission_no = request.POST.get('admission_no')
        joining_date = request.POST.get('joining_date')
        status = "0"

        studDetail = Hod_student(
            hod=request.user,
            Student_name=student_name,
            Admission_no=admission_no,
            Joining_date=joining_date,
            Status=status
        )
        studDetail.save()
        print(studDetail)
        print('Student added')

    students = Hod_student.objects.filter(hod=request.user)  # Fetch all the student details for the current user (HOD)
    return render(request, 'hod/studentdetails.html', {'students': students})




# admission fee

def admin_add_admission_fee(request):
    if request.method == 'POST':
        caution_deposit = request.POST.get('caution_deposit')
        registration_amenities = request.POST.get('registration_amenities')
        mess_advance_fee = request.POST.get('mess_advance_fee')
        amount_for_concession = request.POST.get('amount_for_concession')
        amount_for_non_concession = request.POST.get('amount_for_non_concession')
        amount_for_oec = request.POST.get('amount_for_oec')
        status="0"

        feeDetail = models.Admission_fee(Caution_deposit=caution_deposit, Registration_amenities=registration_amenities,
        Mess_advance_fee=mess_advance_fee, Amount_for_concession=amount_for_concession,Amount_for_oec=amount_for_oec,
        Amount_for_non_concession=amount_for_non_concession, Status=status)
        feeDetail.save()
        print(feeDetail)
        print('fee added')
        return render(request, 'admins/admissionfees.html')
    else:
        return render(request, 'admins/admissionfees.html')


# admission fee delete

def admin_delete_admission_fee(request,id):
    delmember = Admission_fee.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('admin_admission_fee')




# add room

def roomadmin_add_room(request):
    if request.method == 'POST':
        block = request.POST.get('block')
        print(block)
        room = request.POST.get('type')
        print(room)
        room_no = request.POST.get('room_no')
        max_acco= request.POST.get('max_acco')
        vaccancy= request.POST.get('vaccancy')
        amt=request.POST.get('amount')
        status = "0"

        blk = Block.objects.filter(Block_name=block).first()
        print(blk)
        room_type = Room_type.objects.filter(Room_type=room).first()
        print(room_type)

        if blk and room_type:
            roomDetail = models.Room(block=blk,room=room_type,Block_name=blk.Block_name, Room_number=room_no,Rooms_type=room_type.Room_type ,Max_accommodation=max_acco,Amount=amt ,Vaccancy=vaccancy,Status=status)
            roomDetail.save()
            print(roomDetail)
            print('room added')
            return render(request, 'room_admin/room.html')


        return render(request, 'room_admin/room.html')

    else:
        return render(request, 'room_admin/room.html')



# room edit delete

def roomadmin_delete_block(request,id):
    delmember = Block.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('room_block')


def roomadmin_edit_block(request,id):
    Data=  Block.objects.get(id=id) 
    print(Data)
    return render(request,'room_admin/editblock.html',{'data':Data}) 


def blockforumupdate(request,id):
    if request.method == 'POST':
        add=Block.objects.get(id=id)
        add.Block_name=request.POST["block"]
        add.Block_description=request.POST["description"]
        add.save()
        return redirect("room_block")




# admin edit delete

def admin_delete_department(request,id):
    delmember = Department.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('admin_departments')


def admin_edit_department(request,id):
    Data=  Department.objects.get(id=id) 
    return render(request,'admins/editdepartment.html',{'data':Data}) 


def departmentforumupdate(request,id):
    if request.method == 'POST':
        add=Department.objects.get(id=id)
        add.Department_name=request.POST["department"]
        add.Department_description=request.POST["description"]
        add.save()
        return redirect("admin_departments")


# mess edit delete


def mess_delete_coupon(request,id):
    delmember = Coupon.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('coupon_add')




def mess_edit_coupon(request,id):
    Data=  Coupon.objects.get(id=id) 
    return render(request,'mess_admin/editcoupon.html',{'data':Data}) 


def couponforumupdate(request,id):
    if request.method == 'POST':
        add=Coupon.objects.get(id=id)
        add.Type=request.POST["type"]
        add.Amount=request.POST["price"]
        add.save()
        return redirect("coupon_add")


# mess reply

def mess_student_reply_complaint(request):
    if request.method == 'POST':
        reply = request.POST.get('reply')
        status="0"

        replyDetail = models.Complaint(Reply=reply, Status=status)
        replyDetail.save()
        print(replyDetail)
        print('reply added')
        return render(request, 'mess_admin/replycomplaint.html')
    else:
        return render(request, 'mess_admin/replycomplaint.html')


# room reply

def room_student_reply_complaint(request,id):
    data = Complaint.objects.get(id=id)
    return render(request, 'room_admin/replycomplaint2.html',{'data':data})




def roomcomplaintforumupdate(request,id):
    if request.method == 'POST':
        data=Complaint.objects.get(id=id)
        data.Reply=request.POST["message"]
        data.save()
        return redirect('room_view_complaint')
      

  
   


def mess_student_reply_complaint(request,id):
    data = MessComplaint.objects.get(id=id)
    return render(request, 'mess_admin/replycomplaint.html',{'data':data})




def messcomplaintforumupdate(request,id):
    if request.method == 'POST':
        data=MessComplaint.objects.get(id=id)
        data.Reply=request.POST["message"]
        data.save()
        return redirect('mess_view_complaint')





# login


def login_admin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role=""
        data=User.objects.filter(username=username).values()
        print("userModelData==>",data)
        for i in data:
            u_name = i['username']
            id=i['id']

            d=Hod_registration.objects.filter(user_id=id).values()
            print("hoddata==>",d)
            for i in d:
                stat=i['Status']
                role= i['Role']

            da=Room_registration.objects.filter(user_id=id).values()
            print("roomdata==>",da)
            for i in da:
                sta=i['Status']
                role= i['Role']

            dta=Mess_registration.objects.filter(user_id=id).values()
            print("messdata==>",dta)
            for i in dta:
                stas=i['Status']
                role= i['Role']


            user = authenticate(username=username,password=password)
            print("user------------------",user)

            if user is not None and role=="hod" and username==u_name and stat=="1":
                auth_login(request,user)
                return render(request,'hod/index2.html')

            elif user is not None and role=="room" and username==u_name and sta=="1":
                auth_login(request,user)
                return render(request,'room_admin/index.html')

            elif user is not None and role=="mess" and username==u_name and stas=="1":
                auth_login(request,user)
                return render(request,'mess_admin/index.html')

            elif username=="admin" and password=="admn":
                return render(request,'admins/index.html')
            else:pass
            
            
            
        else:
            return redirect('login_page')

    else:
        return render(request,'login.html')




# guest coupon generate

def mess_generate_guest_coupon(request):
    if request.method == 'POST':
        

        coupon = request.POST.get('type')
        amount = request.POST.get('price')
        name = request.POST.get('name')
        date = request.POST.get('date')
        status="1"

        typ = Coupon.objects.filter(Type=coupon).first()
        print(typ)


        if typ:
            userDetail = models.Guest_coupon(coupon=typ, Type=typ.Type, Amount=amount, Guest_name=name, Issued_date=date, Status=status)
            userDetail.save()
            print(userDetail)

        print('coupon generated')
        return render(request,'mess_admin/guest.html')
    else:
        return render(request,'mess_admin/guest.html')
        
        



# hod edit profile

def hod_edit_profile(request,id):
    if request.user:
        user=request.user.id
        print(user)
        if user==id:
            Data=  Hod_registration.objects.get(user=user) 
            return render(request,'hod/hodprofile.html',{'i':Data}) 
        return render(request,'hod/hodprofile.html') 




def hodforumupdate(request,id):
    if request.method == 'POST':
        add=Hod_registration.objects.get(id=id)
        add.Name=request.POST["name"]
        add.Email=request.POST["email"]
        # add.Office_no=request.POST["office"]
        add.Contact_no=request.POST["phone"]
        add.Department_name=request.POST["department"]
        add.save()
        return render(request,'hod/index2.html')





# mess edit profile

def mess_edit_profile(request,id):
    if request.user:
        user=request.user.id
        print(user)
        if user==id:
            Data=  Mess_registration.objects.get(user=user) 
            return render(request,'mess_admin/profile.html',{'i':Data}) 
        return render(request,'mess_admin/profile.html') 


def messforumupdate(request,id):
    if request.method == 'POST':
        add=Mess_registration.objects.get(id=id)
        add.Name=request.POST["name"]
        add.Email=request.POST["email"]
        add.Phone_no=request.POST["phone"]
        add.Address=request.POST["address"]
        add.save()
        return render(request,'mess_admin/index.html')




def room_edit_profile(request,id):
    if request.user:
        user=request.user.id
        print(user)
        if user==id:
            Data=  Room_registration.objects.get(user=user) 
            return render(request,'room_admin/profile.html',{'i':Data}) 
        return render(request,'room_admin/profile.html') 


def roomforumupdate(request,id):
    if request.method == 'POST':
        add=Room_registration.objects.get(id=id)
        add.Name=request.POST["name"]
        add.Email=request.POST["email"]
        add.Phone_no=request.POST["phone"]
        add.Address=request.POST["address"]
        add.save()
        return render(request,'room_admin/index.html')






# hod approve and reject

def admin_approve_hod(request,id):
    user = Hod_registration.objects.get(id=id)
    user.Status = 1
    user.save()
    return redirect('admin_hod')



def admin_reject_hod(request,id):
    delmember =Hod_registration.objects.generate(id=id)
    print(delmember)
    print(delmember.log_id)
    l_id=delmember.log_id
    print(l_id)
    data=Log.objects.get(Username=l_id)
    data.delete()
    return redirect('hod_resign')




# mess approve and reject

def admin_approve_mess(request,id):
    user = Mess_registration.objects.get(id=id)
    user.Status = 1
    user.save()
    return redirect('admin_page')


def admin_reject_mess(request,id):
    delmember =Mess_registration.objects.generate(id=id)
    print(delmember)
    print(delmember.log_id)
    l_id=delmember.log_id
    print(l_id)
    data=Log.objects.get(Username=l_id)
    data.delete()
    return redirect('mess_resign')



# room approve and reject

def admin_approve_room(request,id):
    user = Room_registration.objects.get(id=id)
    user.Status = 1
    user.save()
    return redirect('room_admin_page')


def admin_reject_room(request,id):
    delmember =Room_registration.objects.generate(id=id)
    print(delmember)
    print(delmember.log_id)
    l_id=delmember.log_id
    print(l_id)
    data=Log.objects.get(Username=l_id)
    data.delete()
    return redirect('room_resign')




# admin  delete hod

def admin_delete_hod(request,id):
    delmember = Hod_registration.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('hod_resign')



# admin  delete mess

def admin_delete_mess(request,id):
    delmember = Mess_registration.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('mess_resign')



# admin  delete room

def admin_delete_room(request,id):
    delmember = Room_registration.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('room_resign')



# logout

def logout(request):
    return render(request,'admins/login.html')







def resignation(request):
    if request.user.is_authenticated:
        user = request.user
        message = request.POST.get('message')
        name = user.username

        hod_registrations = Hod_registration.objects.filter(user=user)
        room_registrations = Room_registration.objects.filter(user=user)
        mess_registrations = Mess_registration.objects.filter(user=user)

        for registration in hod_registrations:
            registration.Status = '2'
            registration.save()

        for registration in room_registrations:
            registration.Status = '2'
            registration.save()

        for registration in mess_registrations:
            registration.Status = '2'
            registration.save()

        status = '0'
        userDetails = models.Transient(user=user, Name=name, Message=message, Status=status)
        userDetails.save()
        print(userDetails)
        print('details added')
        return render(request, 'admins/login.html')
    else:
        return render(request, 'admins/transient.html')


# delete admins

def transient_delete(request,id):
    delmember = Transient.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('transient_messages')




# def admin_search_student(request):
#     if request.method == 'POST':
#         query = request.POST.get('department')
#         print(query)

#         students = Student.objects.filter(Department_name=query)
#         print(students)

#         data = [{'sname': student.Student_name, 'department': student.Department_name, 'roomno': student.Room_no, 'blck': student.Block_name, 'status': student.Status} for student in students]
#         print(data)
#         return render(request, 'admins/searchview.html', {'data': data})



def hod_search_student(request):
    if request.method == 'POST':
        query = request.POST.get('sname')
        print(query)

        students = Hod_student.objects.filter(Student_name=query)
        print(students)

        data = [{'sname': student.Student_name, 'admission_no': student.Admission_no, 'joining_date': student.Joining_date} for student in students]
        print(data)
        return render(request, 'hod/hodview.html', {'data': data})

    return render(request, 'hod/studentdetails.html')



def room_search_student(request):
    if request.method == 'POST':
        query = request.POST.get('department')
        print(query)

        i = Student.objects.filter(Department_name=query)
        print(i)

        data = [{'block':info.Block_name, 'room_no':info.Room_no,'sname': info.Student_name, 'admission': info.Admission_no, 'department': info.Department_name, 'contact':info.Student_phone} for info in i]
        print(data)
        return render(request, 'room_admin/roomview.html', {'data': data})


def mess_search_student(request):
    if request.method == 'POST':
        query = request.POST.get('Student_name')
        
        print(query)

        i = Student.objects.filter(Student_name=query)
        print(i)

        data = [{'sname': info.Student_name, 'admission': info.Admission_no, 'department': info.Department_name, 'contact':info.Student_phone} for info in i]
        print(data)
        return render(request, 'mess_admin/studentview.html', {'data': data})




def room_send_verification(request,id):
    user = Student.objects.get(id=id)
    user.Status = 2
    user.save()
    return redirect('room_request')      



def hod_verify_student(request):
    if request.user:
        user=request.user
        data = Hod_registration.objects.filter(user=user).values()
        for i in data:
            dept = i["Department_name"]
            print(dept)
        dta = Student.objects.filter(Department_name=dept).values()
        print(dta)
        return render(request,'hod/verification.html',{'data':dta})  




def hod_send_verification(request,id):
    user = Student.objects.get(id=id)
    user.Status = 3
    user.save()
    return redirect('hod_verify_student')




def room_allocate_student(request):
    
        data = Student.objects.all()
        print(data)
        return render(request,'room_admin/roomallocation.html',{'data':data})



def allocation_view(request, sid):
    block = request.POST.get('block')
    room_no = request.POST.get('room')

    data = Room.objects.filter(Room_number=room_no)

    for i in data:
        i.Vaccancy = i.Vaccancy - 1  # Corrected attribute name
        i.save()

    r = Student.objects.get(id=sid)
    r.Block_name = block
    r.Room_no = room_no
    r.Status = "4"
    r.save()
    return redirect('room_allocate_student')
  



def room_edit_allocation(request,id):
    Data=  Student.objects.get(id=id) 
    print(Data)
    return render(request,'room_admin/allocationview.html',{'data':Data}) 
    


def mess_generate_coupon_for_students(request,id):
    user = Coupon_generate.objects.get(id=id)
    user.Status = 1
    user.save()
    return redirect('mess_coupon_generate') 




def Room_deallocation(request, id):
    user = Deallocation_Request.objects.get(id=id)
    user.Status = 1
    room = ''
    user.save()
    return redirect('room_deallocation_request')
    # data = Room.objects.filter(Room_number=room)
    # for room in data:
    #     # room.Vaccancy += 1  # Increment the Vaccancy field by 1
    #     room.save()
   




def Mess_approval(request,id):
    user = Deallocation_Request.objects.get(id=id)
    user.Status = 2
    user.save()
    return redirect('approval')





def Room_approval(request, id):
    deallocation_request = get_object_or_404(Deallocation_Request, id=id)

    # Get the associated Student object using the related manager
    student = deallocation_request.student

    # Assuming you want to update the Status fields of both models
    deallocation_request.Status = 3
    student.Status = 5

    # Save the changes to the models
    deallocation_request.save()
    student.save()

    # Increment the vacancy count
    room_no = student.Room_no
    room = Room.objects.get(Room_number=room_no)
    room.Vaccancy = room.Vaccancy + 1
    room.save()

    return redirect('deallocation')



def mess_track_search(request):
    if request.method == 'POST':
        query = request.POST.get('department')
        que = request.POST.get('name')
        
        print(query)
        print(que)

        i = Mess_track.objects.filter(Department_name=query,Student_name=name)
        print(i)

        data = [{'sname': info.Student_name, 'amount': info.Mess_fees, 'inout': info.In_or_out, 'time':info.Time} for info in i]
        print(data)
        return render(request, 'mess_admin/trackview.html', {'data': data})



def mess_track_search_student(request):
    if request.method == 'POST':
        query = request.POST.get('department')
        que = request.POST.get('name')
        print(query)
        print(que)

        i = Mess_track.objects.filter(Department_name=query, Student_name=que)
        print(i)

        data = [{'sname': info.Student_name, 'department':info.Department_name, 'inorout': info.In_or_out, 'status': info.Status, 'messindate':info.Mess_in_date, 'messoutdate':info.Mess_out_date} for info in i]
        # print(data)

        return render(request, 'mess_admin/trackview.html', {'data': data})
        

def Count_messin(request):
    current_date = date.today()
    previous_date = current_date - timedelta(days=1)
    blocks = Mess_track.objects.values('Block_name').distinct()

    data = []
    for block in blocks:
        blk = block['Block_name']
        in_count = Mess_track.objects.filter(Mess_in_date=previous_date, Status="0", Block_name=blk).count()
        out_count = Mess_track.objects.filter(Mess_out_date=previous_date, Status="1", Block_name=blk).count()
        present_count = Mess_track.objects.filter(Status="0", Block_name=blk).count()

        block_data = {
            'Block_name': blk,
            'Mess_in_count': in_count,
            'Mess_out_count': out_count,
            'Students_present': present_count
        }
        data.append(block_data)

    return render(request, 'mess_admin/inandout.html', {'data': data})



def roomadmin_add_roomfee(request):
    if request.method == 'POST':
        month = request.POST.get('month')
        amount = request.POST.get('amount')
        status="0"

        feeDetail = models.Room_fee(Month=month, Amount=amount, Status=status)
        feeDetail.save()
        print(feeDetail)
        print('fee added')
        return render(request, 'room_admin/roomfee.html')
    else:
        return render(request, 'room_admin/roomfee.html')




def roomadmin_delete_roomfee(request,id):
    delmember = Room_fee.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('room_fee')



    
def all_forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        print(email)
        print(user)

        if user:
            new_password = get_random_string(length=10)
            user.set_password(new_password)
            user.save()

            subject = 'Password Reset'
            message = f'Dear {user.username},\n\nYour new password is: {new_password}\n\nPlease change your password after logging in.'

            send_mail(subject, message, 'mubashiraajnas@gmail.com', [email])

            messages.success(request, 'A new password has been sent to your email. Please check your inbox.')
            return redirect('login')
        else:
            messages.error(request, 'No user found with the provided email address.')

    return render(request, 'admins/auth-forgot-password-basic.html')





def room_reject_student(request,id):
    delmember = Student.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('room_request')



def hod_reject_student(request,id):
    delmember = Student.objects.get(id=id)
    print(delmember)
    delmember.delete()
    return redirect('hod_verify_student')