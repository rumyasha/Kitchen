from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

#тут импортни
from apps.kitchen.apps import ProposalForm
from apps.kitchen.apps import Author


def hello(request):
    return HttpResponse('Hello, world!')


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'kitchen/', {'authors': authors})


class AuthorsListView(ListView):
    model = Author
    template_name = 'kitchen/'
    context_object_name = 'authors'


def album(request):
    return render(request, 'album.html')


def create_proposal(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kitchen/')
        else:
            return render(request, 'about.html', {'form': form})
    else:
        form = ProposalForm
        return render(request, 'about.html', {'form': form})