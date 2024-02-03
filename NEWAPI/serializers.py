from rest_framework import serializers
from hod.models import Mess_track,Room_rent,MessComplaint,Complaint,Deallocation_Request,Login,Student,Department,Course,Category,Room_type,Noticeboard,Coupon,Block,Admission_fee,Feedback, Coupon_generate




class LoginUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields='__all__'



class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    def create(self, validated_data):
        return Student.objects.create(**validated_data)



   
class FeedbackRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'
   
    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)


class ComplaintRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Complaint
        fields='__all__'
   
    def create(self, validated_data):
        return Complaint.objects.create(**validated_data)


class MessComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model=MessComplaint
        fields='__all__'
   
    def create(self, validated_data):
        return MessComplaint.objects.create(**validated_data)


 
class RoomallocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
   
    def create(self, validated_data):
        return Student.objects.create(**validated_data)       


   
   
class CourseselectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
   

class DepartmentselectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'
   


class CategoryselectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
   


class RoomtypeselectionSerializer(serializers.ModelSerializer):
    class Meta:
         model=Room_type
         fields='__all__'

class NotificationlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Noticeboard
        fields='__all__'
   

class CouponlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coupon
        fields='__all__'
   

class BlocklistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Block
        fields='__all__'
   


   

class Admission_fee_selectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admission_fee
        fields='__all__'





class CouponApplySerializer(serializers.ModelSerializer):
    class Meta:
        model=Coupon_generate
        fields='__all__'
   
    def create(self, validated_data):
        return Coupon_generate.objects.create(**validated_data)





class MessinSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mess_track
        fields='__all__'
   
    def create(self, validated_data):
        return Mess_track.objects.create(**validated_data)      



class DeallocationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Deallocation_Request
        fields='__all__'
   
    def create(self, validated_data):
        return Deallocation_Request.objects.create(**validated_data)      




class RoompaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room_rent
        fields='__all__'
   
    def create(self, validated_data):
        return Room_rent.objects.create(**validated_data)