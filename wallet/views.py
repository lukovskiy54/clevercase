from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from wallet.forms import CategoryCreateForm, AddSpendings
from wallet.models import Category, Notification


@login_required(login_url='login')
def home_page(request):
    form = CategoryCreateForm()
    categories = Category.objects.filter(user=request.user)
    notifications = Notification.objects.filter(user=request.user)
    print(notifications)
    unchecked_notifications_count = notifications.filter(is_checked=False).count()
    id = 0
    is_editing = False
    addSpendings = AddSpendings()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'show_nots':
            notification = Notification.objects.filter(is_checked=False)
            notification.update(is_checked=True)
            return redirect('home')
        if action == 'clear_nots':
            notifications.delete()
            return redirect('home')
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
                    category.is_expended = False
                    if category.currently_spent >= category.the_limit:
                         category.is_expended = True
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
            addSpendings.is_expended = False
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
                    if category.currently_spent >= category.the_limit:
                         category.is_expended = True
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
        'notifications': notifications,
        'unchecked_notifications_count': unchecked_notifications_count,
    }
    return render(request, 'homepage.html', context)