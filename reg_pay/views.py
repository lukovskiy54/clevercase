from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegpayCreateForm
from .models import Regpay

@login_required(login_url='login')
def regpay_page(request):
    if request.method == 'POST':
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
    return render(request, 'regularpays.html', context)