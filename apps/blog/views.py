from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from start.apps.blog.models import Entry
from start.apps.blog.forms import EntryForm
from start.apps.blog.decorators import user_is_entry_author


# Create your views here.
@login_required
def index(request):
    entries = Entry.objects.filter(created_by=request.user)
    return render(request, 'blog/index.html', {'entries': entries})


@login_required
def add(request):
    if request.method=='POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added!')
            return redirect(index)
    else:
        form = EntryForm()
    return render(request, 'blog/entry.html', {'form': form})

@login_required
@user_is_entry_author
def edit(request, entry_id):
    entry=get_object_or_404(Entry, pk=entry_id)
    form = EntryForm(request.POST, instance=entry)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Edited!')
        return redirect(index)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'blog/entry.html', {'form': form})


@login_required
@user_is_entry_author
def delete(request, entry_id):
    entry=get_object_or_404(Entry, pk=entry_id)
    entry.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('index')

@login_required
@user_is_entry_author
def transfer_to(request, entry_id):
    entry=get_object_or_404(Entry, pk=entry_id)
    transfer_to=request.POST.get('transfer_to')
    new_owner=User.objetcs.get(pk=transfer_to)
    entry.created_by=new_owner
    entry.save()
    messages.success(request, 'Successfully Transfered')
    return redirect('index')