from django.shortcuts import redirect, render
from .forms import employeeForm
from Employee_Details.models import Department,Role,Employee
from django.db.models import Q
from django.views import View
from django.core.paginator import Paginator

#Start All employee data show function  And particular Filtering Data Show function
def view_all_emp (request):
    all_emp = Employee.objects.all()                                         
    page = request.GET.get('page', 1) # Start Pagination
    paginator = Paginator(all_emp, 10)

    try:
        page_obj= paginator.page(page)
    except PageotAnInteger:
        page_obj = paginator.page(1)
    except EmptPage:
        page_obj = paginator.page(paginator.num_pages) # End Pagination
            # start Filtering
    if request.method == 'GET':
        st = request.GET.get('searchname')
        if st != None:
            if st:
                all_emp = Employee.objects.filter(Q(First_Name__icontains= st) | Q(id__icontains=st))
                return render(request,'filter.html',{'all_emp': all_emp})
            # endstart Filtering
    return render(request,'view_all_emp.html',{'page_obj': page_obj})

#Add New Employee fclass/function
class add_emp_View(View):
 def get(self, request):
  form =employeeForm()
  return render(request, 'add_employee.html', {'form':form})

 def post(self, request):
  form =employeeForm(request.POST)
  if form.is_valid():
   form.save()
   return redirect('/')
  else:
   return render(request, 'add_employee.html', {'form':form})


# Delete Employee through Employee ID
def remove_emp(request,pk):
    if request.method== 'POST':
        emp_id = Employee.objects.get(id=pk)
        emp_id.delete()
    return redirect('/')
    



#Update/Edit Employee through Employee ID
def update(request,pk):
    if request.method == 'POST':
        update_id = Employee.objects.get(pk=pk)
        dataForm =employeeForm(request.POST, instance=update_id)
        if dataForm.is_valid():
            dataForm.save()
            return redirect('/')
    else:
        update_id = Employee.objects.get(pk=pk)
        dataForm =employeeForm(instance=update_id)
    return render(request,'edit.html',{'form':dataForm}) 