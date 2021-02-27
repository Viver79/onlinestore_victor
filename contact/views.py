from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from contact.models import UserMessages

def home(request):
    messages = UserMessages.objects.filter(is_processed=False).order_by('send_date')
    paginator = Paginator(messages, 5)
    page = request.GET.get('page')
    messages = paginator.get_page(page)
    return render(request, 'messages.html', context={'items': messages})

def update_messages(request, pk):
    UserMessages.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/messages/')
