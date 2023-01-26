from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Transaction
from stores.models import Store
import ipdb
from .serializers import TransactionSerializer
from stores.serializers import StoreSerializer

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

def get_stores_from_database():

    stores = Store.objects.all()

    serializer = StoreSerializer(stores, many=True)

    add_transactions_to_store_list(serializer.data)

    return serializer.data

def add_transactions_to_store_list(store_list):
    for store in store_list:
        
        # ipdb.set_trace()
        transactions = Transaction.objects.filter(store_id = store['id'])
        serializer = TransactionSerializer(transactions, many = True)
        store['transactions'] = serializer.data
        
        store['balance'] = calculate_total_value(serializer.data)

def refresh_database(file):
    
    transactions_list = get_transactions_list_from_file(file)

    for transaction in transactions_list:
        
        serializer = TransactionSerializer(data=transaction)
        serializer.is_valid(raise_exception=True)

        serializer.save()

def get_transactions_list_from_file(file):
    
    cnab_field_sizes = [1, 8, 10, 11, 12, 6, 14, 19]
    
    fields = [
        "type_transaction",
        "date",
        "value",
        "cpf",
        "card",
        "hour",
        "owner",
        "name",
    ]

    transaction_dict_list = parse_cnab_file(file, fields, cnab_field_sizes)
    
    convert_to_transaction_model(transaction_dict_list)

    return transaction_dict_list

def calculate_total_value(transactions_list):
    transaction_types = [1 , -1, -1, 1, 1, 1, 1, 1, -1]
    
    balance = 0

    for transaction in transactions_list:
        
        current_value = transaction['value']

        current_type = int(transaction['type_transaction']) - 1

        balance += transaction_types[current_type] * current_value

    return balance


def convert_to_transaction_model(list):
    for obj in list:
        store = {
            'name': obj['name'],
            'owner': obj['owner'],
        }
        obj.pop('name')
        obj.pop('owner')
        obj['store'] = store
        obj['value'] = int(obj['value'])/100

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
    # print(objects_list)
    
    return objects_list