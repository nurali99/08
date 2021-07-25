from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser, Post
# Create your views here.

class SignUpView(CreateView):
  form_class=CustomUserCreationForm
  success_url=reverse_lazy('login')
  template_name='signup.html'
  
class HomeListView(ListView):
  model=CustomUser
  template_name='home.html'

  # bu post uchun 
  # 1)postni ekranda ko'rsatish
class PageListView(ListView):
  model=Post
  template_name='pages.html'

# 2)postni ekranda namoyish qilish
class PageDetailView(DetailView):
  model=Post
  template_name='post_detail.html'

  # yangi post qo'shish
class PageCreateView(CreateView):
  model=Post
  template_name='post_new.html'
  fields=['title', 'rasm', 'body', 'time']

  # postni tahrirlash
class PageUpdateView(UpdateView):
  model=Post
  template_name='post_edit.html'
  fields=['title', 'rasm', 'body']

  # postni o'chirish
class PageDeleteView(DeleteView):
  model=Post
  template_name='post_delete.html'
  success_url=reverse_lazy('pages')



