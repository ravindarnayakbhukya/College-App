from django.shortcuts import render
from admissions.models import *
from admissions.forms import *
from django.views.generic import *
from django.http import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import *

# function-based views

@login_required
def homePage(request):
    return render(request,'index.html')




def userLogout(request):
    return render(request,'registration/logout.html')




@login_required
def addAdmissions(request):
    form = StudentModelForm
    studentdict = {'forms':form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return admissionReport(request)

    return render(request,'admissions/add admissions.html',studentdict)



@login_required
def admissionReport(request):
    #fetch all data from Student
    result = Student.objects.all()  #select * from Student
    #store it in a students dictionary
    students = {'allstudents':result}
    return render(request,'admissions/admission report.html',students)




@login_required
#add, delete, update = change, view
@permission_required('admissions.change_student')       #@permission_required('application.operation_model')
def updateStudent(request,id):
    s = Student.objects.get(id=id)  #select * from Student where id = idvalue
    form = StudentModelForm(instance=s)
    updatedict = {'forms':form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return admissionReport(request)

    return render(request,'admissions/update-student.html',updatedict)




@login_required
@permission_required('admissions.delete_student')      #@permission_required('application.operation_model')
def deleteStudent(request,id):
    s = Student.objects.get(id=id)  #select * from Student where id = idvalue
    s.delete()
    return admissionReport(request)




@login_required
def addVendor(request):
    form = VendorForm
    vendordict = {'forms':form}

    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            p = form.cleaned_data['place']
            c = form.cleaned_data['contact']
            i = form.cleaned_data['item']


            response = render(request,'index.html')

            #response.set_cookie('name',n)
            #response.set_cookie('place',p)
            #response.set_cookie('contact',c)
            #response.set_cookie('item',i)

            request.session['name']=n
            request.session['place']=p
            request.session['contact']=c
            request.session['item']=i

        return response

    return render(request,'admissions/add vendor.html',vendordict)





class FirstClassBasedView(View):
    def get(self,request):
        return HttpResponse("<h1>Hello...Welcome to First Class Based Views!</h1>")




class TeacherList(ListView):
    model = Teacher
    #default object teacher_list will store the data retrieved from Model
    #should create a template by its default name teacher_list.html and map the url pattern



class TeacherDetail(DetailView):
    model = Teacher
    #default object teacher_detail will store the data retrieved from Model
    #should create a template by its default name teacher_detail.html and map the url pattern



class AddTeacher(CreateView):
    model = Teacher
    fields = ('name','subject','experience','contact')
    #default object teacher_form will store the data retrieved from Model
    #should create a template by its default name teacher_form.html and map the url pattern
    #define get_absolute_url in models.py to return a page by reverse function imported from django.urls



class UpdateTeacher(UpdateView):
    model = Teacher
    fields = ('name','contact')  #specify the fields only which are about to update




class DeleteTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacherlist')
