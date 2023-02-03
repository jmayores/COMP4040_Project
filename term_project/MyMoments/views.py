from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.
def mymoments_view(request, id):
    obj = get_object_or_404(Blog, id=id)
    context ={
        'object': obj
    }
    return render(request, "mymoments.html", context)

def mymoments_list_view(request):
    queryset = Blog.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'mymoments_list.html', context)

def mymoments_create_view(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'mymoments_create.html', context)

def mymoments_update_view(request, id=id):
    obj = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'mymoments_create.html', context)

def mymoments_delete_view(request, id):
    obj = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../../')
    context = {
        'object': obj
    }
    return render(request, 'mymoments_delete.html', context)