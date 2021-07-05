from django.shortcuts import render, get_object_or_404, redirect
from .models import Crud
from .forms import PostForm

# Create your views here.
def home(request):
    cruds = Crud.objects
    return render(request, 'home.html', {'cruds' : cruds})

def detail(request, crud_id):
    crud_detail = get_object_or_404(Crud, pk = crud_id)
    return render(request, 'detail.html', {'crud' : crud_detail})

def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form':form})

def edit(request):
    return render(request, 'edit.html')

def postupdate(request, crud_id):
    post = get_object_or_404(Crud, pk=crud_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', crud_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def postdelete(request, crud_id):
    post = get_object_or_404(Crud, pk=crud_id)
    post.delete()
    return redirect('home')