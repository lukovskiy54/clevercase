from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegpayCreateForm
from .models import Regpay

@login_required(login_url='login')
def regpay_page(request):
    form = RegpayCreateForm()
    regpays = Regpay.objects.filter(user=request.user)
    id = 0
    if request.method == 'POST':
        if 'save' in request.POST:
            form = RegpayCreateForm(request.POST, request=request)
            if form.is_valid():
                regpay = form.save(commit=False)
                regpay.user = request.user
                regpay.save()
                return redirect('regularpays')
        form = RegpayCreateForm()
        regpays = Regpay.objects.filter(user=request.user)
        print(regpays)
        context = {
            'form': form,
            'regpays': regpays,
        }
    elif 'delete' in request.POST:
        pk = request.POST.get('delete')
        print(pk)
        category = Regpay.objects.get(id=pk)
        category.delete()
    elif 'edit' in request.POST:
        print("hay")
        pk = request.POST.get('edit')
        regpay = Regpay.objects.get(id=pk)
        form = RegpayCreateForm(instance=regpay)
        id = pk

    context = {
        'regpays': regpays,
        'form': form,
        'id': id,
    }
    return render(request, 'regularpays.html', context)


