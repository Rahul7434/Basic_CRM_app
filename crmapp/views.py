from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):
    record = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you Have Been Logged In !")
            return redirect('home')
        else:
            messages.success(request,"There Was An Error Logging In Please Try Again...")
            return redirect('home')
    else:
        return render(request,'crmapp/home.html',{'records':record})
 

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,"You Have Successfully Registered !")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'crmapp/signup.html',{'form':form})
    return render(request,'crmapp/signup.html',{'form':form})
   
   
   
def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request,'crmapp/record.html',{customer_record:'customer_record'})
    else:
        messages.success(request,"You Must be Logged In To View That Page")
        return redirect("home")
    

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Records Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request,"Record Added....")
                return redirect('home')
        return render(request,"crmapp/add_record.html",{'form':form})
    else:
        messages.success(request,"You must Be Logged In...")
        return redirect('home')
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form= AddRecordForm(request.POST or None, instance="")
        if form.is_valid():
            form.save()
            messages.success(request,"Record Has Been Updated")
            return redirect('home')
        return render(request, 'update_record.html',{'form':form})
    else:
        messages.success(request,"You Must Be Logged In")
        return redirect('home')
    

        