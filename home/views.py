from django.shortcuts import render ,HttpResponse
from  django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from datetime import  datetime
from django.contrib import messages
from django.shortcuts import redirect ,get_object_or_404
from .models import SALES_DATA ,Customer,Purchase_Data
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def index(request):
    if 'Username' in request.session:
        Username = request.session['Username']
        return render(request, "index.html", context={'Username': Username})
    else:
        return redirect("/Signinuser")

def Signinuser(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        user = authenticate(username=Username, password=Password)
        if user is not None:
            request.session['Username'] = Username
            return redirect('/index')
        else:
            messages.success(request,"Your Id or Password is wrong please try again")
            return render(request,"Signinuser.html")
    return render(request, "Signinuser.html")

def Registration(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user =User.objects.filter(username=Username).exists()

        if ( user == True):
           messages.error(request,"User already exists")
           return render(request, "Registration.html")
        else:
           user = User.objects.create_user(username=Username,email=email,password=password)
           user.save()
           messages.success(request, "User Successfully created.")
           return render(request, "Signinuser.html")
    else:
        return render(request,"Registration.html")

def logoutuser(request):
    if request.method == "POST":
        request.session['Username'] = ""
        logout(request)
        return redirect("/Signinuser")
    else:
        return render(request, "index.html")

def sales(request):
    if 'Username' in request.session:
        Username = request.session['Username']
        sales_data = SALES_DATA.objects.filter(Status=True).order_by('-id')

        paginator = Paginator(sales_data, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        f = {'Status':'True','Customer_Type':'1'}
        Customer_Data = Customer.objects.filter(**f)
        args = {'Username': Username , 'sales_data':sales_data ,'Customer_Data':Customer_Data,'page_obj':page_obj}
        if request.POST.get("Action") == "Save":
            Item_Description = request.POST.get("Item_Description")
            Item_Type =  request.POST.get("Item_Type")
            Customer_Name = request.POST.get("Customer_Name")
            Company_Name = request.POST.get("Company_Name")
            Amount = request.POST.get("Amount")
            Rate = request.POST.get("Rate")
            Status = True
            Sale_Date = datetime.now()
            User = Username
            Address = request.POST.get("Address")
            Sales=SALES_DATA(Item_Description=Item_Description,Item_Type=Item_Type,Customer_Name=Customer_Name,Company_Name=Company_Name,Amount=Amount,
                             Rate=Rate,Status=Status,Sale_Date=Sale_Date,Username=User,Address=Address)
            Sales.save()
        if request.POST.get("Action") == 'Update':
            Sales = SALES_DATA.objects.get(id=request.POST.get("Update_id"))
            Sales.Item_Description = request.POST.get("Item_Description")
            Sales.Item_Type = request.POST.get("Item_Type")
            Sales.Customer_Name = request.POST.get("Customer_Name")
            Sales.Company_Name = request.POST.get("Company_Name")
            Sales.Amount = request.POST.get("Amount")
            Sales.Rate = request.POST.get("Rate")
            Sales.Status = True
            Sales.Sale_Date = datetime.now()
            Sales.User = Username
            Sales.Address = request.POST.get("Address")
            Sales.save()
        elif request.POST.get("Action") == 'Delete':
             Sales = SALES_DATA.objects.get(id=request.POST.get("Update_id"))
             Sales.Status = False
             Sales.save()
        if request.POST.get("ActionEdit") == "Edit":
            f = {'Status': 'True', 'Customer_Type': '1'}
            Customer_Data = Customer.objects.filter(**f)
            get_Data_Bykey = SALES_DATA.objects.get(id=request.POST.get("Rec_id"))
            Update_id=request.POST.get("Rec_id")
            Customer_Data = Customer.objects.filter(Status=True)
            args = {'Username': Username, 'sales_data': sales_data ,'get_Data_Bykey':get_Data_Bykey,'Customer_Data':Customer_Data ,'Action': 'EdittoUpdate','Update_id':Update_id}

        elif request.POST.get("ActionEdit") == "Delete":
            get_Data_Bykey = SALES_DATA.objects.get(id=request.POST.get("Rec_id"))
            Update_id = request.POST.get("Rec_id")
            Customer_Data = Customer.objects.filter(Status=True)
            args = {'Username': Username, 'sales_data': sales_data, 'get_Data_Bykey': get_Data_Bykey,'Customer_Data':Customer_Data,'Action': 'EdittoDelete', 'Update_id': Update_id}
        return render(request,'Sales.html',context=args)
    else:
        return redirect("/Signinuser")

def purchase(request):
    if 'Username' in request.session:
        Username = request.session['Username']
        Purchase_Dt = Purchase_Data.objects.filter(Status=True).order_by('-id')
        paginator = Paginator(Purchase_Dt, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        f = {'Status': 'True', 'Customer_Type': '2'}
        Customer_Data = Customer.objects.filter(**f)
        args = {'Username': Username, 'Purchase_Dt': Purchase_Dt , 'Customer_Data': Customer_Data , 'page_obj': page_obj}
        if request.POST.get("Action") == "Save":
            Item_Description = request.POST.get("Item_Description")
            Item_Type = request.POST.get("Item_Type")
            Vendor_Name = request.POST.get("Customer_Name")
            Company_Name = request.POST.get("Company_Name")
            Amount = request.POST.get("Amount")
            Rate = request.POST.get("Rate")
            Status = True
            Purchase_Date = datetime.now()
            User = Username
            Address = request.POST.get("Address")
            Purchase_D = Purchase_Data(Item_Description=Item_Description, Item_Type=Item_Type, Vendor_Name=Vendor_Name,
                               Company_Name=Company_Name, Amount=Amount,
                               Rate=Rate, Status=Status, Purchase_Date=Purchase_Date, Username=User, Address=Address)
            Purchase_D.save()
        if request.POST.get("Action") == 'Update':
            Purchase_D = Purchase_Data.objects.get(id=request.POST.get("Update_id"))
            Purchase_D.Item_Description = request.POST.get("Item_Description")
            Purchase_D.Item_Type = request.POST.get("Item_Type")
            Purchase_D.Customer_Name = request.POST.get("Customer_Name")
            Purchase_D.Company_Name = request.POST.get("Company_Name")
            Purchase_D.Amount = request.POST.get("Amount")
            Purchase_D.Rate = request.POST.get("Rate")
            Purchase_D.Status = True
            Purchase_D.Purchase_Date = datetime.now()
            Purchase_D.User = Username
            Purchase_D.Address = request.POST.get("Address")
            Purchase_D.save()
        elif request.POST.get("Action") == 'Delete':
            Purchase_D = Purchase_Data.objects.get(id=request.POST.get("Update_id"))
            Purchase_D.Status = False
            Purchase_D.save()
        if request.POST.get("ActionEdit") == "Edit":
            get_Data_Bykey = Purchase_Data.objects.get(id=request.POST.get("Rec_id"))
            Update_id = request.POST.get("Rec_id")
            f = {'Status': 'True', 'Customer_Type': '2'}
            Customer_Data = Customer.objects.filter(**f)
            Purchase_D = Purchase_Data.objects.filter(Status=True)
            args = {'Username': Username,   'Purchase_D': Purchase_D,  'get_Data_Bykey': get_Data_Bykey,  'Customer_Data':Customer_Data, 'Action': 'EdittoUpdate', 'Update_id': Update_id}
        elif request.POST.get("ActionEdit") == "Delete":
            get_Data_Bykey = Purchase_Data.objects.get(id=request.POST.get("Rec_id"))
            Update_id = request.POST.get("Rec_id")
            Customer_Data = Customer.objects.filter(Status=True)
            args = {'Username': Username, 'get_Data_Bykey': get_Data_Bykey,'Customer_Data': Customer_Data, 'Action': 'EdittoDelete', 'Update_id': Update_id}

        return render(request,'purchase.html',context=args)
    else:
        return redirect("/Signinuser")

def Customer_Dropdown(request):
    Customer_Data = Customer.objects.filter(Status=True)
    return render(request,'Customer_Dropdown.html',context={'Customer_Data': Customer_Data})

def FormCreation(request):
    return render(request,"FormCreation.html")

