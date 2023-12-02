from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from wallet.forms import CategoryCreateForm, AddSpendings
from wallet.models import Category


@login_required(login_url='login')
def home_page(request):
    form = CategoryCreateForm()
    categories = Category.objects.filter(user=request.user)
    id = 0
    is_editing = False
    addSpendings = AddSpendings()
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            print(pk)
            if pk is None or pk == '0':
                form = CategoryCreateForm(request.POST, request=request) 
            else:
                category = Category.objects.get(id=pk)
                form = CategoryCreateForm(request.POST, instance=category, request=request,  is_editing=True)  
                is_editing = True
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
            is_editing = True
            print("hay")
            pk = request.POST.get('edit')
            category = Category.objects.get(id=pk)
            form = CategoryCreateForm(instance=category)
            id = pk
        elif 'add' in request.POST:
            is_editing = True
            pk = request.POST.get('add')
            category = Category.objects.get(id=pk)
            addSpendings = AddSpendings(category_id=pk)
            print(addSpendings.category_id)
            id = pk
        elif 'save_add' in request.POST:
            addSpendings = AddSpendings(request.POST)
            if addSpendings.is_valid():
                    print('valid')
                    pk = request.POST.get('save_add')
                    print(pk)
                    addings = addSpendings.save(commit=False)
                    addings.categoryId = pk
                    addings.user = request.user  
                    addings.save()
                    category = Category.objects.get(id=pk)
                    category.currently_spent += addings.amount
                    category.save()
                    return redirect('home')
            else:
                print(addSpendings.errors)
            
            
    context = {
        'categories': categories,
        'form': form,
        'id': id,
        'is_editing': is_editing,
        'addSpendings':addSpendings,
    }
    return render(request, 'homepage.html', context)