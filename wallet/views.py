from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from wallet.forms import CategoryCreateForm
from wallet.models import Category


@login_required(login_url='login')
def home_page(request):
    form = CategoryCreateForm()
    categories = Category.objects.filter(user=request.user)
    id = 0
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            print(pk)
            if pk is None or pk == '0':
                form = CategoryCreateForm(request.POST, request=request) 
            else:
                category = Category.objects.get(id=pk)
                form = CategoryCreateForm(request.POST, instance=category, request=request,  is_editing=True)  
                form.is_editing = True
            if form.is_valid():
                    category = form.save(commit=False)
                    category.user = request.user  
                    category.save()
                    return redirect('home')
            else:
                print(form.errors)
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            print(pk)
            category = Category.objects.get(id=pk)
            category.delete()
        elif 'edit' in request.POST:
            print("hay")
            pk = request.POST.get('edit')
            category = Category.objects.get(id=pk)
            form = CategoryCreateForm(instance=category)
            id = pk
            
    context = {
        'categories': categories,
        'form': form,
        'id': id,
        
    }
    return render(request, 'homepage.html', context)