from django.urls import path
from hod import views

urlpatterns = [

 # admin
    path("", views.login_page,name="login_page"),
    path("admin_home", views.admin_index,name="admin_home"),
    path("admin_admission_fee", views.admin_admission_fee,name="admin_admission_fee"),
    path("all_forgot_password", views.all_forgot_password,name="all_forgot_password"),
    path("admin_courses", views.admin_courses,name="admin_courses"),
    path("dashboard", views.dashboard,name="dashboard"),
    path("admin_page",views.admin_page,name="admin_page"),
    path("room_admin_page",views.room_admin_page,name="room_admin_page"),
    path("admin_departments", views.admin_departments,name="admin_departments"),
    path("admin_hod",view&s.admin_hod,name="admin_hod"),
    path("hod_resign",views.hod_resign,name="hod_resign"),
    path("mess_resign",views.mess_resign,name="mess_resign"),
    path("admin_noticeboard",views.admin_noticeboard,name="admin_noticeboard"),
    path("room_resign",views.room_resign,name="room_resign"),
    # path("students",views.admin_students,name="students"),
    path("hod_portal",views.hod_portal,name="hod_portal"),
    path("room_portal",views.room_portal,name="room_portal"),
    path("mess_portal",views.mess_portal,name="mess_portal"),
    path("admin_category",views.admin_category,name="admin_category"),
    path("transient_messages",views.transient_messages,name="transient_messages"),

    

    path("admin_add_department",views.admin_add_department,name="admin_add_department"),
    path("admin_add_course",views.admin_add_course,name="admin_add_course"),
    path("admin_add_notice",views.admin_add_notice,name="admin_add_notice"),
    path("hod_register",views.hod_register,name="hod_register"),
    path("room_register",views.room_register,name="room_register"),
    path("mess_register",views.mess_register,name="mess_register"),
    path("admin_add_category",views.admin_add_category,name="admin_add_category"),
    path("admin_add_admission_fee",views.admin_add_admission_fee,name="admin_add_admission_fee"),
    path("admin_delete_department/<int:id>",views.admin_delete_department,name="admin_delete_department"),
    path("admin_edit_department/<int:id>",views.admin_edit_department,name="admin_edit_department"),
    path("departmentforumupdate/<int:id>",views.departmentforumupdate,name="departmentforumupdate"),
    path("login_admin",views.login_admin,name="login_admin"),


    path("admin_approve_hod/<int:id>",views.admin_approve_hod,name="admin_approve_hod"),
    path("admin_delete_hod/<int:id>",views.admin_delete_hod,name="admin_delete_hod"),
    path("admin_approve_room/<int:id>",views.admin_approve_room,name="admin_approve_room"),
    path("admin_delete_room/<int:id>",views.admin_delete_room,name="admin_delete_room"),
    path("admin_approve_mess/<int:id>",views.admin_approve_mess,name="admin_approve_mess"),
    path("admin_delete_mess/<int:id>",views.admin_delete_mess,name="admin_delete_mess"),
    path("logout",views.logout,name="logout"),
    path("resignation",views.resignation,name="resignation"),
    path("transient_delete/<int:id>",views.transient_delete,name="transient_delete"),
    path("admin_delete_admission_fee/<int:id>",views.admin_delete_admission_fee,name="admin_delete_admission_fee"),
    # path("admin_search_student",views.admin_search_student,name="admin_search_student"),
    
    
    




   


# hod


    path("hod_home",views.hod_index,name="hod_home"),
    path("hod_notifications",views.hod_notifications,name="hod_notifications"),
    path("student_details",views.student_details,name="student_details"),
    path("hod_verification",views.hod_verification,name="hod_verification"),
    path("hod_transient",views.hod_transient,name="hod_transient"),

    path("hod_register",views.hod_register,name="hod_register"),
    path("add_student",views.add_student,name="add_student"),
    path("hod_add_student_details",views.hod_add_student_details,name="hod_add_student_details"),
    path("hod_edit_profile/<int:id>",views.hod_edit_profile,name="hod_edit_profile"),
    path("hodforumupdate/<int:id>",views.hodforumupdate,name="hodforumupdate"),
    path("hod_search_student",views.hod_search_student,name="hod_search_student"),
    path("hod_verify_student",views.hod_verify_student,name="hod_verify_student"),
    path("hod_send_verification/<int:id>",views.hod_send_verification,name="hod_send_verification"),

    



# mess_admin

    path("approval",views.approval,name="approval"),
    path("mess_coupon_generate",views.mess_coupon_generate,name="mess_coupon_generate"),
    path("mess_guest_coupon",views.mess_guest_coupon,name="mess_guest_coupon"),
    path("coupon_fee",views.coupon_fee,name="coupon_fee"),
    path("coupon_add",views.coupon_add,name="coupon_add"),
    path("expense",views.expense,name="expense"),
    path("mess_feedback",views.mess_feedback,name="mess_feedback"),
    path("inandout",views.inandout,name="inandout"),
    path("mess_home",views.mess_index,name="mess_home"),
    path("mess_fee",views.fee_mess,name="mess_fee"),
    path("mess_track",views.track_mess,name="mess_track"),
    # path("mess_profile",views.mess_profile,name="mess_profile"),
    path("mess_notification",views.mess_notification,name="mess_notification"),
    path("mess_reply_complaint",views.mess_reply_complaint,name="mess_reply_complaint"),
    path("mess_transient",views.mess_transient,name="mess_transient"),
    path("mess_view_complaint",views.mess_view_complaint,name="mess_view_complaint"),
    path("mess_student",views.mess_student,name="mess_student"),

    path("coupon_add_mess",views.coupon_add_mess,name="coupon_add_mess"),
    path("mess_register",views.mess_register,name="mess_register"),
    path("mess_add_notice",views.mess_add_notice,name="mess_add_notice"),
    path("mess_add_expenditure",views.mess_add_expenditure,name="mess_add_expenditure"),
    path("mess_delete_coupon/<int:id>",views.mess_delete_coupon,name="mess_delete_coupon"),
    path("mess_edit_coupon/<int:id>",views.mess_edit_coupon,name="mess_edit_coupon"),
    path("couponforumupdate/<int:id>",views.couponforumupdate,name="couponforumupdate"),
    path("mess_generate_guest_coupon",views.mess_generate_guest_coupon,name="mess_generate_guest_coupon"),
    path("mess_student_reply_complaint/<int:id>",views.mess_student_reply_complaint,name="mess_student_reply_complaint"),
    path("mess_generate_coupon",views.mess_generate_coupon,name="mess_generate_coupon"),
    # path("mess_account",views.mess_account,name="mess_account"),
    path("mess_edit_profile/<int:id>",views.mess_edit_profile,name="mess_edit_profile"),
    path("messforumupdate/<int:id>",views.messforumupdate,name="messforumupdate"),
    path("mess_search_student",views.mess_search_student,name="mess_search_student"),
    path("messcomplaintforumupdate/<int:id>",views.messcomplaintforumupdate,name="messcomplaintforumupdate"),
    path("mess_generate_coupon_for_students/<int:id>",views.mess_generate_coupon_for_students,name="mess_generate_coupon_for_students"),
    path("Mess_approval/<int:id>",views.Mess_approval,name="Mess_approval"),
    path("mess_track_search",views.mess_track_search,name="mess_track_search"),
    path("mess_track_search_student",views.mess_track_search_student,name="mess_track_search_student"),
    path("Count_messin",views.Count_messin,name="Count_messin"),






# room_admin

     path("room_block",views.room_block,name="room_block"),
     path("room_deallocation_request",views.room_deallocation_request,name="room_deallocation_request"),
     path("room_notification",views.room_notification,name="room_notification"),
     path("room_feedback",views.room_feedback,name="room_feedback"),
     path("room_home",views.room_index,name="room_home"),
    #  path("room_profile",views.room_profile,name="room_profile"),
     path("room_reply_complaint",views.room_reply_complaint,name="room_reply_complaint"),
     path("room_transient",views.room_transient,name="room_transient"),
     path("room_view_room",views.room_view_room,name="room_view_room"),
     path("room_rent",views.rent_room,name="room_rent"),
     path("room_request",views.request_room,name="room_request"),
     path("room_student",views.room_student,name="room_student"),
     path("room_view_complaint",views.room_view_complaint,name="room_view_complaint"),
     path("roomadmin_roomtype",views.roomadmin_roomtype,name="roomadmin_roomtype"),
     path("allocation",views.allocation,name="allocation"),
     path("deallocation",views.deallocation,name="deallocation"),

     path("room_register",views.room_register,name="room_register"),
     path("room_add_notice",views.room_add_notice,name="room_add_notice"),
     path("room_add_block",views.room_add_block,name="room_add_block"),
     path("roomadmin_add_room",views.roomadmin_add_room,name="roomadmin_add_room"),
     path("roomadmin_add_roomtype",views.roomadmin_add_roomtype,name="roomadmin_add_roomtype"),
     path("roomadmin_delete_block/<int:id>",views.roomadmin_delete_block,name="roomadmin_delete_block"),
     path("roomadmin_delete_block/<int:id>",views.roomadmin_delete_block,name="roomadmin_delete_block"),
     path("roomadmin_edit_block/<int:id>",views.roomadmin_edit_block,name="roomadmin_edit_block"),
     path("blockforumupdate/<int:id>",views.blockforumupdate,name="blockforumupdate"),
     path("room_student_reply_complaint/<int:id>",views.room_student_reply_complaint,name="room_student_reply_complaint"),
     #  path("room_account",views.room_account,name="room_account"),
     path("room_edit_profile/<int:id>",views.room_edit_profile,name="room_edit_profile"),
     path("roomforumupdate/<int:id>",views.roomforumupdate,name="roomforumupdate"),
     path("room_search_student",views.room_search_student,name="room_search_student"),
     path("roomcomplaintforumupdate/<int:id>",views.roomcomplaintforumupdate,name="roomcomplaintforumupdate"),
     path("room_send_verification/<int:id>",views.room_send_verification,name="room_send_verification"),
     path("room_allocate_student",views.room_allocate_student,name="room_allocate_student"),
     path("allocation_view/<int:sid>",views.allocation_view,name="allocation_view"),
     path("room_edit_allocation/<int:id>",views.room_edit_allocation,name="room_edit_allocation"),
     path("Room_deallocation/<int:id>",views.Room_deallocation,name="Room_deallocation"),
     path("Room_approval/<int:id>",views.Room_approval,name="Room_approval"),
     path("room_fee",views.room_fee,name="room_fee"),
     path("roomadmin_add_roomfee",views.roomadmin_add_roomfee,name="roomadmin_add_roomfee"),
     path("roomadmin_delete_roomfee/<int:id>",views.roomadmin_delete_roomfee,name="roomadmin_delete_roomfee"),
     path("room_reject_student/<int:id>",views.room_reject_student,name="room_reject_student"),
     path("hod_reject_student/<int:id>",views.hod_reject_student,name="hod_reject_student"),
     path("admin_delete_notice/<int:id>",views.admin_delete_notice,name="admin_delete_notice"),
   


   



    
]