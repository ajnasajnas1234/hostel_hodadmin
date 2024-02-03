from django.urls import path
from NEWAPI import views

urlpatterns = [
# admin

   
    path("all_category", views.Category_selectionAPIView.as_view(),name="all_category"),
    path("all_Department", views.Department_selectionAPIView.as_view(),name="all_Department"),
    path("view_all_Course",views.Course_selectionAPIView.as_view(),name="view_all_Course"),
    path("view_room_type", views.Roomtype_selectionAPIView.as_view(),name="view_room_type"),
    path("view_notificationlist", views.Notification_listAPIView.as_view(),name="view_notificationlist"),
    path("view_couponlist", views.Coupon_listAPIView.as_view(),name="view_couponlist"),
    path("view_blocklist", views.Block_listAPIView.as_view(),name="view_blocklist"),
    path("view_Admission_fee", views.Admission_fee_selectionAPIView.as_view(),name="view_Admission_fee"),
    path("login_user", views.loginUsersAPIView.as_view(),name="login_user"),
    path("single_student/<int:id>",views.SinglestudentAPIView.as_view(),name="single_student"),
    path("update_student/<int:id>",views.Update_studentAPIView.as_view(),name="update_student"),
    path("delete_student/<int:id>",views.Delete_studentAPIView.as_view(),name="delete_student"),
    path("feedback_list", views.Feedback_listAPIView.as_view(),name="feedback_list"),
    path("complaint_list/<int:id>", views.SingleComplaintAPIView.as_view(),name="complaint_list"),
    
    
    
    


    path("Room_allocate/<int:id>", views.RoomallocationAPIView.as_view(),name="Room_allocate"),
    path("Register_student", views.StudentRegisterAPIView.as_view(),name="Register_student"),
    path("feedback_student", views.FeedbackRegistrationAPIView.as_view(),name="feedback_student"),
    path("complaint_student", views.ComplaintRegistrationAPIView.as_view(),name="complaint_student"),
    path("messcomplaint_student",views.MessComplaintRegistrationAPIView.as_view(),name="messcomplaint_student"),



    path("coupon_apply_student",views.CouponApplyAPIView.as_view(),name="coupon_apply_student"),
    path("coupon_issued_student/<int:id>",views.messissuedcouponAPIView.as_view(),name="coupon_issued_student"),
    path("messin",views.MessinAPIView.as_view(),name="messin"),
    path("deallocation_request",views.DeallocationRegistrationAPIView.as_view(),name="deallocation_request"),
    
    path("Roomrent", views.RoompaymentAPIView.as_view(),name="Roomrent"),

]