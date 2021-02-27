from django.shortcuts import render, redirect
from contact.forms import UserMessagesForm
from bicycles.models import Bike_type


def get_main_page(request):

    index_bike_type = Bike_type.objects.filter(is_visible=True).order_by('categories_bicycles')
    if request.method == 'POST':
        form = UserMessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = UserMessagesForm()

    return render(request, 'index.html', context={'form': form,
                                                  'index_bike_type': index_bike_type,})