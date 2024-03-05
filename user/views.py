from django.shortcuts import render,HttpResponseRedirect
from django.contrib.messages import success,error
from django.contrib.auth.forms import User
from django.core.mail import send_mail
from UserManagementSystem import settings
from django.contrib import auth
from .models import UserProfile,Organization,Role, MembershipRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
def sample(request):
    return render(request,'sample.html')

@login_required(login_url='/login/')
def dashboard(request):
    user=UserProfile.objects.get(user=request.user)
    r=user.role
    if r is None:
        return HttpResponseRedirect('/sample/')
    else:
        n=r.name
        print(n)
        if n != 'Admin':
            return HttpResponseRedirect('/sample/')
        else:
            data=MembershipRequest.objects.filter(organization=user.organization,is_pending='Pending')
            return render(request, 'dashboard.html',{"data":data})

def accept(request,pk):
    m= MembershipRequest.objects.get(id=pk)
    if request.method=='POST':
        r=request.POST.get('role')
        rol= Role.objects.get(name= r, organization= m.organization)
        u=UserProfile.objects.get(user=m.user)
        u.role=rol
    m.is_accepted=True
    m.is_pending='Not pending'
    m.save()
    return render(request, 'adminForm.html', {"data":m})

def reject(request,pk):
    m = MembershipRequest.objects.get(id=pk)
    m.is_accepted = False
    m.is_pending = 'Not pending'
    m.save()
    u = UserProfile.objects.get(user=m.user)
    u.delete()
    uu= User.objects.get(username=m.user.username)
    uu.delete()
    return HttpResponseRedirect('/dashboard/')

def email_send(request,email,name):
    subject = 'Thanks '+name+' for registering to our site'
    message = ' It  means a lot to us '
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, from_email, recipient_list)

def signUp(request):
    d=Organization.objects.all()
    if(request.method=='POST'):
        uname=request.POST.get('uname')
        try:
            match = User.objects.get(username=str(uname))
            if (match):
                error(request, "Username Already Exist")
        except:
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            mail = request.POST.get('email')
            org=request.POST.get('org')
            pward = request.POST.get('pward')
            cpward = request.POST.get('cpward')

            org_name = Organization.objects.get(name=org)
            bill = org_name.billing_group
            data = UserProfile.objects.filter(organization=org_name)
            count = data.count()


            if bill=='free'and count==5:
                error(request,"Limit reached")
            elif bill=='pro'and count==100:
                error(request,"Limit reached")
            elif pward == cpward:
                User.objects.create_user(username=str(uname),
                                         first_name=str(fname),
                                         last_name=str(lname),
                                         email=mail,
                                         password=pward
                                         )


                if count==0:
                    r='Admin'
                    role=Role.objects.get(name=r,organization=org_name)
                    pro = User.objects.get(username=str(uname))
                    u = UserProfile()
                    u.organization = org_name
                    u.user=pro
                    u.role=role
                    u.save()

                else:
                    pro = User.objects.get(username=str(uname))
                    u=UserProfile()
                    u.organization=org_name
                    u.user=pro
                    m = MembershipRequest()
                    m.user = pro
                    m.organization = org_name
                    m.is_pending = 'Pending'
                    u.save()
                    m.save()
                success(request, "Account is created")

                try:
                    email_send(request, mail, fname)
                except:
                    error(request, "/login/")
                return HttpResponseRedirect('/login/')
            else:
                error(request, "Password and Confirm Password not Matched")
    return render(request,"index.html",{"data":d})

def login(request):
    if(request.method=='POST'):
        lname=request.POST.get('uname')
        lpward=request.POST.get('psw')
        user=auth.authenticate(username=lname,password=lpward)
        if(user is not None):
            auth.login(request,user)
            if(user.is_superuser):
                return HttpResponseRedirect('/dashboard/')
            else:
                return HttpResponseRedirect('/dashboard/')
        else:
            error(request,"Invalid User")
    return render(request,'userLogin.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
