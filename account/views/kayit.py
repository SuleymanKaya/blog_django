from django.shortcuts import redirect, render
from django.contrib import messages
from account.forms import KayitForm
from django.contrib.auth import login, authenticate

def kayit(request):
    if request.method == 'POST':
        form = KayitForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username'] # Her iki kullanımda geçerli
            password = form.cleaned_data.get('password1')# Her iki kullanımda geçerli
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('anasayfa')

    else:
        form = KayitForm()
    
    return render(request, 'pages/kayit.html', context={
        'form':form
    })