from django.http import HttpResponse
from django.shortcuts import render, redirect
from blogpage.models import Post
from userinfo.models import contactEnquiry


def index(request):
    posts = Post.objects.all()
    print(posts)
    
    """if request.method=="GET":
        output=request.GET.get('output')"""
    if request.method=="GET":
        searchname=request.GET.get('searchname')
        if searchname!=None:
            posts = Post.objects.filter(title__icontains=searchname)
    data={
        'posts':posts,

    }        
    return render(request, 'index.html',data)

def about(request):
    
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request, 'about.html',{'output': output})

def contact(request):
    return render(request, 'contact.html')
def login(request):
    data={}
    try:
        if request.method=="POST":
            un = request.POST.get('name')
            psw = request.POST.get('psw')
            
            #finalans = n1

            data={
                'un':un,
                'psw':psw,
                
               
            }
           
            return redirect('/')
    except:
        pass    
    return render(request, 'login.html', data)

def register(request):
    #finalans = 0
    data={}
    try:
        if request.method=="POST":
            n1= request.POST.get('name')
            n2= request.POST.get('email')
            n3= request.POST.get('psw')
            n4= request.POST.get('psw-repeat')
            #finalans = n1

            data={
                'n1':n1,
                'n2':n2,
                'n3':n3,
                'n4':n4,
                #'output':finalans,
            }
           # url="/about/?output={}".format{finalans}
            return redirect('/')
    except:
        pass    

            
    return render(request, "register.html", data)

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        psw=request.POST.get('psw')
        pswrepeat=request.POST.get('pswrepeat')
        en = contactEnquiry(name=name,email=email,psw=psw,pswrepeat=pswrepeat)
        en.save()
    return render(request, 'login.html')

