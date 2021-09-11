from django.shortcuts import render
from .models import table_data


def display_table(request):
    all_obj = table_data.objects.all()
    context = {'all': all_obj}
    return render(request, 'my_test_app/home.html', context)

