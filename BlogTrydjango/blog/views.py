from django.shortcuts import render, get_object_or_404
from .models import Blogpost , Blogpostuser
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django import forms 
#from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
@login_required
def display(request, post_id=0):
    alert=""
    #obj = get_object_or_404(Blogpost, id=post_id)
    if post_id ==0:
        obj = Blogpost.objects.all()
        # obj=Blogpost.objects.filter(pk=100)
    else:
        obj = get_object_or_404(Blogpost, id=post_id)
    #try:    
    #    obj = Blogpost.objects.get(id=post_id)
    #except:
    #    raise Http404
    # alert=obj
    template = 'display.html'
    context={'object':obj, 'alert':alert}
    return render(request, template, context,)

#@staff_member_required
@login_required
def create(request):
    userform = Blogpostuser(request.POST or None)
    if userform.is_valid():
        userform.save()
        userform=Blogpostuser()
    name = "blog/create.html"
    context = {'title': "contact" , 'content': "contact", 'form':userform}
    return render(request, name, context)

@login_required
def search(request):
    alert=""
    obj=None
    tosearch=Blogpost
    #alert=request.POST['search']
    
    if request.POST['search']:
        tosearch = request.POST['search']
        obj= Blogpost.objects.filter(title=tosearch)
        if not obj:
            # alert ="there is no title in database. "
            obj= Blogpost.objects.filter(slug=tosearch)
            if not obj:
                alert +="there is no slug in database "        
    else:
        alert ="there is no title or slug to search"
    name = "display.html"
    
    context = {'title': "Update " , 'object':obj,'alert':alert}
    return render(request, name, context)



@login_required
def update(request):
    alert = ""
    obj = None
    userform=None
    if request.method == "POST":
        if "forupdate" in request.POST and request.POST['forupdate'] !="":
            toupdate = request.POST['forupdate']
            obj = Blogpost.objects.filter(title=toupdate).first()  # return the object can be 1 or more or None if does not have  not
            if obj:  # None is evaluation to false
                # if obj mean if they found one they gonna update it
                userform = Blogpostuser(None, instance=obj)
            else:
                # it is not found by using the title , we gonna slug to find object to update
                # filter return the query set list so we have to access by index , in template it is working fine since we have the loop to iterate through it
                obj = Blogpost.objects.filter(slug=toupdate).first()
                # in return of filter we get a query set list so use filter to get the first (it is only one slug is unique we use filter instead of get since if 0 it would return error
                if obj:
                    userform = Blogpostuser(None, instance=obj)
                else:
                    alert = "there is no object in database "
        else:
            if "title" in request.POST:
                obj = Blogpost.objects.filter(slug=request.POST['slug']).first()
                userform = Blogpostuser(request.POST or None, instance=obj)
                if userform.is_valid():
                    userform.save()
                    userform = None
            # does not update slug since i used to find if i cannot find with the slug i would create a new object instead
            else:
                alert = "there is no title or slug find object to update"
            # if userform:
            #     alert = userform
            # else:
            #     alert = "there is no title or slug find object to delete"

    name = "blog/update.html"
    context = {'title': "Update ", 'content': "contact", 'form': userform, 'alert': alert}
    return render(request, name, context)
    # obj= get_object_or_404(Blogpost)
    # userform=Blogpostuser
    # userform = Blogpostuser(request.POST or None, instance=obj)
    # if userform.is_valid():
    #     test= "string in the is valid"
    #     userform.save()
    # name = "blog/update.html"
    # context = {'title': "Update " , 'content': "contact",}
    # return render(request, name, context)

@login_required
def delete(request):
    alert=""
    obj=None
    delete=Blogpost
    if request.method == "POST":
        if request.POST['delete']:
            todelete = request.POST['delete']
            obj= Blogpost.objects.filter(title=todelete).first() # return the object can be 1 or more or None if does not have  not
            alert=obj
            if obj: # None is evaluation to false
                delete.title= obj.title
                delete.slug= obj.slug
                delete.content= obj.content
                obj.delete()
            else:
                obj= Blogpost.objects.filter(slug=todelete).first()
                if obj:
                    delete.title= obj.title
                    delete.slug= obj.slug
                    delete.content= obj.content
                    obj.delete()
                else:
                    alert ="there is no object in database "
        else:
            alert="there is no title or slug find object to delete"
    name = "blog/delete.html"
    context = {'title': "Update " , 'content': "contact", 'form':obj,'alert':alert}
    return render(request, name, context)