from django.shortcuts import render
from hod.models import Complaint,Login,Student,Department,Course,Deallocation_Request,Category,Room_type,Noticeboard,Coupon,Block,Admission_fee,Feedback,Room, Coupon_generate
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework.generics import GenericAPIView
from .serializers import RoompaymentSerializer,MessinSerializer,DeallocationRequestSerializer,LoginUsersSerializer,MessComplaintSerializer,StudentRegisterSerializer,CourseselectionSerializer,DepartmentselectionSerializer,CategoryselectionSerializer,RoomtypeselectionSerializer,NotificationlistSerializer,CouponlistSerializer,BlocklistSerializer,Admission_fee_selectionSerializer,FeedbackRegistrationSerializer,ComplaintRegistrationSerializer,RoomallocationSerializer, CouponApplySerializer

# Create your views here.

class StudentRegisterAPIView(GenericAPIView):

    serializer_class=StudentRegisterSerializer
    serializer_class_login=LoginUsersSerializer

    def post(self,request):

        login_id=''
        studentname = request.data.get('studentname')
        # Lastname = request.data.get('Lastname')
        Gender = request.data.get('Gender')
        Dateofbirth = request.data.get('Dateofbirth')
        phone = request.data.get('phone')
        Email=request.data.get('Email')
        Address = request.data.get('Address')
        place = request.data.get('place')
        street = request.data.get('street')
        post = request.data.get('post')
        pincode = request.data.get('pincode')
        Admission_no=request.data.get('Admission_no')
        Guardianname=request.data.get('Guardianname')
        Guardiancontact=request.data.get('Guardiancontact')
        Yearofadmission=request.data.get('Yearofadmission')
        Course=request.data.get('Course')
        Departments=request.data.get('Department')
        Studentusername=request.data.get('Studentusername')
        StudentPassword=request.data.get('StudentPassword')
        role = 'student'
        studentstatus = '0'
        data=Department.objects.all().filter(id=Departments).values()
        for i in data:
            dpt_name=i["Department_name"]
        

        if (Login.objects.filter(Username=Studentusername)):
            return Response({'message' : 'Duplicate Username Found!'},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login= self.serializer_class_login(data= {'Username':Studentusername, 'Password':StudentPassword, 'Role':role})

        if serializer_login.is_valid():
            log =serializer_login.save()
            login_id=log.id
            print(login_id)
        serializer = self.serializer_class(data= {'login_id':login_id,'Student_name':studentname,'Gender':Gender,'DOB':Dateofbirth,'Student_phone':phone,'Email':Email,'Address':Address,'Place':place,'Street':street,'Post':post,'Pincode':pincode,'Admission_no':Admission_no,'Guardian_name':Guardianname,'Guardian_phone':Guardiancontact,'Year_of_admission':Yearofadmission,'Course_name':Course,'dpt':Departments,'Department_name':dpt_name,'role':role, 'Status':studentstatus})
        print(serializer)
        if serializer.is_valid():
            print("hiii")
            serializer.save()
            return Response({'data':serializer.data,'message':'student registered succesfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)




class loginUsersAPIView(GenericAPIView):
    serializer_class=LoginUsersSerializer

    def post(self,request):
        u_id=''
        l_status=""
        
        Username=request.data.get('Username')
        Password=request.data.get('Password')
        logreg=Login.objects.filter(Username=Username,Password=Password)
        if (logreg.count()>0):
            read_serializer=LoginUsersSerializer(logreg,many=True)
            for i in read_serializer.data:
                id = i['id']
                # print(id)
                role=i['Role']
                regdata=Student.objects.all().filter(log_id=id).values()
                # print(regdata)
                for i in regdata:
                    u_id = i['id']
                    l_status = i['Status']
                    print(u_id)

            return Response({'data':{'login_id':id,'Username': Username,'Password':Password,'Role':role,'user_id':u_id,'l_status':l_status},'success':True,'message':'Logged in successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'data':'username or password is invalid','success':False,},status=status.HTTP_400_BAD_REQUEST)



class FeedbackRegistrationAPIView(GenericAPIView):

    serializer_class=FeedbackRegistrationSerializer

    def post(self,request):
        dptname=''
        Stdname=''
        Feedback=request.data.get('Feedback')
        Date=request.data.get('Date')
        Feedbacktitle=request.data.get('Feedbacktitle')
        department=request.data.get('department')
        student=request.data.get('student')
        studentstatus = '0'

        data=Department.objects.all().filter(id=department).values()
        for i in data:
            dptname=i['Department_name']
            
        data=Student.objects.all().filter(id=student).values()
        for i in data:
            Stdname=i['Student_name']
            print(Stdname)
           
            
        
        serializer = self.serializer_class(data= {'Feedback':Feedback,'Date':Date,'Feedback_title':Feedbacktitle,'Student_name':Stdname,'Department_name':dptname,'dpt':department,'student':student,'Status':studentstatus})
        print(serializer)
        if serializer.is_valid():
            print("hiii")
            serializer.save()
            return Response({'data':serializer.data,'message':'student entered feedback succesfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)




class ComplaintRegistrationAPIView(GenericAPIView):

    serializer_class=ComplaintRegistrationSerializer

    def post(self,request):
        Stdname=""
        dptname=""
        roomnumber=""
        blockname=""
        department=request.data.get('department')
        block=request.data.get('block')
        room=request.data.get('room')
        student=request.data.get('student')
        Date=request.data.get('Date')
        Complaintdescription=request.data.get('Complaintdescription')
        Reply=request.data.get('Reply')
        Title=request.data.get('Title')
        studentstatus = '0'

        data=Department.objects.all().filter(id=department).values()
        for i in data:
            dptname=i['Department_name']
        
        data=Student.objects.all().filter(id=student).values()
        for i in data:
            Stdname=i['Student_name']
            
        data=Room.objects.all().filter(id=room).values()
        for i in data:
            roomnumber=i['Room_number']
            print(roomnumber)
        data=Block.objects.all().filter(id=block).values()
        for i in data:
            blockname=i['Block_name']
            print(blockname)
            
        
        serializer = self.serializer_class(data= {'Department_name':dptname,'Block_name':blockname,'Room_number':roomnumber,'block':block,'room':room,'Student_name':Stdname,'Date':Date,'Complaint_description':Complaintdescription,'Title':Title,'Reply':Reply,'dpt':department,'student':student,'Status':studentstatus})
        print(serializer)
        if serializer.is_valid():
            print("hiii")
            serializer.save()
            return Response({'data':serializer.data,'message':'student entered Complaint succesfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)


class MessComplaintRegistrationAPIView(GenericAPIView):

    serializer_class=MessComplaintSerializer

    def post(self,request):
        Stdname=""
        blockname=""
        block=request.data.get('block')
        student=request.data.get('student')
        Date=request.data.get('Date')
        Complaintdescription=request.data.get('Complaintdescription')
        Reply=request.data.get('Reply')
        Title=request.data.get('Title')
        studentstatus = '0'
        
        data=Student.objects.all().filter(id=student).values()
        for i in data:
            Stdname=i['Student_name']
            
        
        data=Block.objects.all().filter(id=block).values()
        for i in data:
            blockname=i['Block_name']
            print(blockname)
            
        
        serializer = self.serializer_class(data= {'Block_name':blockname,'block':block,'Student_name':Stdname,'Date':Date,'Complaint_description':Complaintdescription,'Title':Title,'Reply':Reply,'student':student,'Status':studentstatus})
        print(serializer)
        if serializer.is_valid():
            print("hiii")
            serializer.save()
            return Response({'data':serializer.data,'message':'student entered Complaint succesfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)



class RoomallocationAPIView(GenericAPIView):

    serializer_class = StudentRegisterSerializer

    def post(self, request, id):
        distance = request.data.get('Distance')
        room_type = request.data.get('roomtype')
        category = request.data.get('category')
        concession = request.data.get('Concession')
        photo = request.data.get('photo')
        document = request.data.get('document')


        data=Room_type.objects.all().filter(id=room_type).values()
        for i in data:
            roomtypes=i['Room_type']
        
        data=Category.objects.all().filter(id=category).values()
        for i in data:
            categorynames=i['Category']



        if id:
            student = Student.objects.get(id=id)
            student.Distance_from_home = distance
            student.Category_name = categorynames
            student.Room_type = roomtypes
            student.Concession = concession
            student.Photo = photo
            student.Documents = document
            student.Status = '1'
            student.save()

            serializer = self.serializer_class(student)
            return Response({'data': serializer.data, 'message': 'Student data updated successfully', 'success': True}, status=status.HTTP_201_CREATED)

        return Response({'message': 'Invalid request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)




class Category_selectionAPIView(GenericAPIView):
    serializer_class=CategoryselectionSerializer

    def get(self,request):
        queryset=Category.objects.all()
        if (queryset.count()>0):
            serializer=CategoryselectionSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'All Category Data','success':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':serializer.error,'message':'failed','success':False},status=status.HTTP_400_BAD_Request)











class Department_selectionAPIView(GenericAPIView):
    serializer_class=DepartmentselectionSerializer


    def get(self,request):
        queryset=Department.objects.all()
        if (queryset.count()>0):
            serializer=DepartmentselectionSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'All Department Data','success':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':serializer.error,'message':'failed','success':False},status=status.HTTP_400_BAD_Request)





class Notification_listAPIView(GenericAPIView):
    serializer_class=NotificationlistSerializer


    def get(self,request):
        queryset=Noticeboard.objects.all()
        if (queryset.count()>0):
            serializer=NotificationlistSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'All Notification Data','success':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':serializer.error,'message':'failed','success':False},status=status.HTTP_400_BAD_Request)




class Feedback_listAPIView(GenericAPIView):
    serializer_class=FeedbackRegistrationSerializer


    def get(self,request):
        queryset=Feedback.objects.all()
        if (queryset.count()>0):
            serializer=FeedbackRegistrationSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'All Notification Data','success':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':serializer.error,'message':'failed','success':False},status=status.HTTP_400_BAD_Request)



class Coupon_listAPIView(GenericAPIView):
    serializer_class=CouponlistSerializer


    def get(self,request):
        queryset=Coupon.objects.all()
        if (queryset.count()>0):
            serializer=CouponlistSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'All Coupon Data','success':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':serializer.error,'message':'failed','success':False},status=status.HTTP_400_BAD_Request)








class Course_selectionAPIView(GenericAPIView):
    serializer_class=CourseselectionSerializer

    def get(self,request):
        queryset=Course.objects.all()
        if (queryset.count()>0):
            serializer=CourseselectionSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'All Category Data','success':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':serializer.error,'message':'failed','success':False},status=status.HTTP_400_BAD_Request)





class Roomtype_selectionAPIView(GenericAPIView):
    serializer_class=RoomtypeselectionSerializer

    def get(self,request):
        queryset=Room_type.objects.all()
        if (queryset.count()>0):
            serializer=RoomtypeselectionSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'All Roomtype are here','success':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':serializer.error,'message':'failed','success':False},status=status.HTTP_400_BAD_Request)










class Block_listAPIView(GenericAPIView):
    serializer_class=BlocklistSerializer

    def get(self,request):
        queryset=Block.objects.all()
        if (queryset.count()>0):
            serializer=BlocklistSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'All Block are here','success':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':serializer.error,'message':'failed','success':False},status=status.HTTP_400_BAD_Request)



class Admission_fee_selectionAPIView(GenericAPIView):
    serializer_class=Admission_fee_selectionSerializer

    def get(self,request):
        queryset=Admission_fee.objects.all()
        if (queryset.count()>0):
            serializer=Admission_fee_selectionSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'All fee Data','success':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':serializer.error,'message':'failed','success':False},status=status.HTTP_400_BAD_Request)


class SinglestudentAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=Student.objects.get(pk=id)
        serializer=StudentRegisterSerializer(queryset)
        return Response({'data':serializer.data,'message':'single student data','success':True},status=status.HTTP_200_OK)


class SingleComplaintAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=Complaint.objects.get(student=id)
        serializer=StudentRegisterSerializer(queryset)
        return Response({'data':serializer.data,'message':'single student data','success':True},status=status.HTTP_200_OK)
        



class Update_studentAPIView(GenericAPIView):
    serializer_class=StudentRegisterSerializer
    def put(self,request,id):
        queryset=Student.objects.get(pk=id)
        print(queryset)
        serializer=StudentRegisterSerializer(instance=queryset,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'All updated  Data','success':True},status=status.HTTP_200_OK)
        else:
            return Response({'data':'somethingwent wrong','success':False},status=status.HTTP_400_BAD_REQUEST)


class Delete_studentAPIView(GenericAPIView):
    def delete(self,request,id):
            delmember=Login.objects.get(pk=id)
            delmember.delete()
            return Response({'message':'deleted','success':False},status=status.HTTP_200_OK)




class CouponApplyAPIView(GenericAPIView):

    serializer_class=CouponApplySerializer

    def post(self,request):
        Stdname=""
        Type=request.data.get('Type')
        Amount=request.data.get('Amount')
        Date=request.data.get('Issued_date')
        student=request.data.get('student')
        coupon=request.data.get('coupon')
        couponstatus = '0'
        
        data=Student.objects.all().filter(id=student).values()
        for i in data:
            Stdname=i['Student_name']
            
        
        serializer = self.serializer_class(data= {'Issued_date':Date,'Amount':Amount,'Type':Type,'student':student,'coupon':coupon,'Student_name':Stdname,'Status':couponstatus})
        print(serializer)
        if serializer.is_valid():
            print("hiii")
            serializer.save()
            return Response({'data':serializer.data,'message':'student Coupon Applied succesfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)





class messissuedcouponAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=Coupon_generate.objects.all().filter(student=id).values()
        # serializer=CouponApplySerializer(queryset)
        return Response({'data':queryset,'message':'Coupon Generated Success','success':True},status=status.HTTP_200_OK)
 




class MessinAPIView(GenericAPIView):
    serializer_class = MessinSerializer

    def post(self, request):
        Stdname=""
        Dptname=""
        
        student=request.data.get('student')
        
        Mess_in_date_str = request.data.get('Mess_in_date')
        Mess_out_date_str = request.data.get('Mess_out_date')
        Time = request.data.get('Time')
        
        if Mess_in_date_str and Mess_out_date_str:
            Mess_in_date = datetime.strptime(Mess_in_date_str, '%Y-%m-%d').date()
            Mess_out_date = datetime.strptime(Mess_out_date_str, '%Y-%m-%d').date()

            Dates = Mess_out_date - Mess_in_date
            days = Dates.days
            print(days)
        

        data=Student.objects.all().filter(id=student).values()
        for i in data:
            Stdname=i['Student_name']
            Dptname=i['Department_name']
        messinstatus="0"
      
            

        
        serializer = self.serializer_class(data= {'Student_name':Stdname,'Department_name':Dptname, 'student':student,'Mess_in_date':Mess_in_date_str,'Mess_out_date':Mess_out_date_str,'Time':Time,'student':student,'Status':messinstatus,'Date':days})
        print(serializer)
        if serializer.is_valid():
            print("hiii")
            serializer.save()
            return Response({'data':serializer.data,'message':'student entered Complaint succesfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)





class DeallocationRegistrationAPIView(GenericAPIView):

    serializer_class=DeallocationRequestSerializer

    def post(self,request):
        Stdname=""
        coursename=""
        roomnumber=""
        blockname=""
        department=request.data.get('department')
        Course=request.data.get('Course')
        block=request.data.get('block')
        room=request.data.get('room')
        student=request.data.get('student')
        Date=request.data.get('Date')
        Reason=request.data.get('Reason')
        studentstatus = '0'

        data=Department.objects.all().filter(id=department).values()
        for i in data:
            dptname=i['Department_name']
        
        data=Student.objects.all().filter(id=student).values()
        for i in data:
            Stdname=i['Student_name']

            
        data=Room.objects.all().filter(id=room).values()
        for i in data:
            roomnumber=i['Room_number']
            print(roomnumber)
        data=Block.objects.all().filter(id=block).values()
        for i in data:
            blockname=i['Block_name']
            print(blockname)
            
        
        serializer = self.serializer_class(data= { 'Date':Date, 'Reason':Reason,'Department_name':dptname,'Block_name':blockname,'Room_number':roomnumber,'block':block,'room':room,'Student_name':Stdname,'dpt':department,'student':student,'Status':studentstatus})
        print(serializer)
        if serializer.is_valid():
            print("hiii")
            serializer.save()
            return Response({'data':serializer.data,'message':' deallocation request succesfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)






class RoompaymentAPIView(GenericAPIView):

    serializer_class=RoompaymentSerializer

    def post(self,request):
        Stdname=""
        coursename=""
        roomnumber=""
        blockname=""
        dptname=""
        department=request.data.get('department')
        Course=request.data.get('Course')
        block=request.data.get('block')
        room=request.data.get('room')
        student=request.data.get('student')
        Date=request.data.get('Date')
        Rent=request.data.get('Rent')
        # Reason=request.data.get('Reason')
        studentstatus = '0'

        data=Department.objects.all().filter(id=department).values()
        for i in data:
            dptname=i['Department_name']
        
        data=Student.objects.all().filter(id=student).values()
        for i in data:
            Stdname=i['Student_name']

            
        data=Room.objects.all().filter(id=room).values()
        for i in data:
            roomnumber=i['Room_number']
            print(roomnumber)
        data=Block.objects.all().filter(id=block).values()
        for i in data:
            blockname=i['Block_name']
            print(blockname)
            
        
        serializer = self.serializer_class(data= { 'Rent':Rent,'Date':Date,'Department_name':dptname,'Block_name':blockname,'Room_number':roomnumber,'block':block,'room':room,'Student_name':Stdname,'dpt':department,'student':student,'Status':studentstatus})
        print(serializer)
        if serializer.is_valid():
            print("hiii")
            serializer.save()
            return Response({'data':serializer.data,'message':' deallocation request succesfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)




class MessinAPIView(GenericAPIView):
    serializer_class = MessinSerializer

    def post(self, request):
        Stdname=""
        # date=""
        student=request.data.get('student')
        
        Mess_in_date_str = request.data.get('Mess_in_date')
        Mess_out_date_str = request.data.get('Mess_out_date')
        Time = request.data.get('Time')
        Month = request.data.get('Month')
        # Date=request.data.get('Date')
        if Mess_in_date_str and Mess_out_date_str:
            Mess_in_date = datetime.strptime(Mess_in_date_str, '%Y-%m-%d').date()
            Mess_out_date = datetime.strptime(Mess_out_date_str, '%Y-%m-%d').date()

            Dates = Mess_out_date - Mess_in_date
            days = Dates.days
            print(days)
        

        data=Student.objects.all().filter(id=student).values()
        for i in data:
            Stdname=i['Student_name']
            Deptname=i['Department_name']
            Blkname=i['Block_name']
            
        messinstatus="0"
      
            

        
        serializer = self.serializer_class(data= {'Student_name':Stdname,'student':student,'Department_name':Deptname,'Block_name':Blkname,'Mess_in_date':Mess_in_date_str,'Mess_out_date':Mess_out_date_str,'Time':Time,'Month':Month,'student':student,'Status':messinstatus,'Date':days})
        print(serializer)
        if serializer.is_valid():
            print("hiii")
            serializer.save()
            return Response({'data':serializer.data,'message':'student entered Complaint succesfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)