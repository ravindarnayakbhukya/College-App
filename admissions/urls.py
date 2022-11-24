from django.urls import path
from admissions.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('newadm/', addAdmissions),
    path('admreport/', admissionReport),
    path('newvendor/', addVendor),
    path('delete/<int:id>', deleteStudent),
    path('update/<int:id>', updateStudent),

    path('firstcbv/', login_required(FirstClassBasedView.as_view())),
    path('teacherlist/', login_required(TeacherList.as_view()),name = 'teacherlist'),
    path('teacherdetail/<int:pk>/', login_required(TeacherDetail.as_view()),name='teacherdetail'),
    path('addteacher/', login_required(AddTeacher.as_view())),
    path('updateteacher/<int:pk>/', login_required(UpdateTeacher.as_view())),
    path('deleteteacher/<int:pk>/', login_required(DeleteTeacher.as_view())),

]
