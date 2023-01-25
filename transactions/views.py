from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UploadFileForm
import ipdb

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # print (request.FILES['file'])
            # form.save()
            handle_uploaded_file(request.FILES['file'])
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    
    cnab_fields_sizes = [1, 8, 10, 11, 12, 6, 14, 19]    
    
    fields = [
        "tipo",
        "data",
        "valor",
        "cpf",
        "cartao",
        "hora",
        "donoLoja",
        "nomeLoja",
]
    objects = []
    while True:
    
        index_field = 0
        object = {}
        cnab_line: str = f.readline().decode()[:-1]
        
        if not cnab_line:
            break
        last_index = 0
        for field_size in cnab_fields_sizes:
            
            field_value = cnab_line[last_index:last_index + field_size]
            
            current_field = fields[index_field]
            object[current_field] = field_value
            index_field += 1
            last_index += field_size
        objects.append(object)

        # ipdb.set_trace()
    print(objects)

    

def success(request):
    return render(request, 'success.html')