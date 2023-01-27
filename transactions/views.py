from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .functions import get_stores_from_database, refresh_database

import ipdb


def show_transactions(request):
    
    store_list = get_stores_from_database()

    return render(request, 'transactions.html', {'store_list': store_list})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # print (request.FILES['file'])
            # form.save()
            refresh_database(request.FILES['file'])

            return redirect('show_transactions')
            
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
