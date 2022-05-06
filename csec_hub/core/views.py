from django.shortcuts import render

# Create your views here.

def hompage(request):
    return render(request,'index.html',context={})

def events(request):
    return render(request,'events.html',context={})

def feeds(request):
    return render(request,'feeds.html',context={})

def about(request):
    return render(request,'about.html',context={})

def contact(request):
    return render(request,'contact.html',context={})

def faq(request):
    return render(request,'faq.html',context={})




def eventDetail(request):
        return render(request,'eventDetail.html',context={})

def feedDetail(request):
        return render(request,'feedDetail.html',context={})


