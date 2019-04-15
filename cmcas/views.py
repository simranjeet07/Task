# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .models import Books
from .forms import LoginForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login

# Create your views here.
class DisplayBooks(ListView):
    model = Books
    context_object_name = 'objects'
    template_name = 'cmcas/list.html'

class CreateBook(CreateView):
    model = Books
    fields = '__all__'
    template_name = 'cmcas/create.html'

class UpdateBook(UpdateView):
    model = Books
    fields = '__all__'
    template_name = 'cmcas/update.html'

class DeleteBook(DeleteView):
    model = Books
    template_name = 'cmcas/delete.html'
    success_url = reverse_lazy('list')

class BookDetailView(DetailView):
    model = Books
    context_object_name = 'obj'
    template_name = 'cmcas/detail.html'

class UserLogin(View):
    template_name = 'cmcas/login.html'
    form_class = LoginForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('list')
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(self.request, user)
                return redirect('list')
            else:
                return render(request, "cmcas/login.html", {'form': form, 'error': 'invalid username or password'})
        return render(request, self.template_name, {'form':form})


def learn_custom_filters(request):
    value = "Simranjeet Singh Never Give Up Never"
    return render(request, "cmcas/custom-filter.html", {'value': value})