from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Transaction
import ipdb


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # print (request.FILES['file'])
            # form.save()
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'success.html')
            
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(file):
    
    cnab_field_sizes = [1, 8, 10, 11, 12, 6, 14, 19]    
    
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

    transaction_dict_list = parse_cnab_file(file, fields, cnab_field_sizes)
    
    for transaction_dict in transaction_dict_list:
        
        transaction = Transaction(**transaction_dict)
        
        transaction.save()

    



def parse_cnab_file(file, field_names_list, cnab_field_sizes_list):
    objects_list = []
    while True:
    
        index_field = 0
        object = {}

        cnab_line_str: str = file.readline().decode()[:-1]
        
        if not cnab_line_str:
            break

        last_index = 0
        for field_size in cnab_field_sizes_list:
            
            field_value = cnab_line_str[last_index : last_index + field_size]
            
            current_field = field_names_list[index_field]

            object[current_field] = field_value

            index_field += 1
            last_index += field_size

        objects_list.append(object)

        # ipdb.set_trace()
    print(objects_list)
    
    return objects_list