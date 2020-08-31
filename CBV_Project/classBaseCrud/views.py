from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # 데이터 추가

from .models import ClassBlog

# Create your views here.

class BlogView(ListView):       # html 템플릿 : 블로그 리스트를 담은 html : (소문자모델)_list.html
    template_name = 'classBaseCrud/list.html' # 원하는 template의 이름을 사용할 때 작성
    context_object_name = 'blog_list'
    model = ClassBlog

class BlogCreate(CreateView):   # html : form (입력공간)을 갖고있는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ["title", "body"]
    success_url = reverse_lazy('list')

class BlogRead(DetailView):     # html : 상세 페이지를 담은 html : (소문자모델)_detail.html
    context_object_name = 'blogpost'
    model = ClassBlog

class BlogUpdate(UpdateView):   # html : form (입력공간)을 갖고있는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ["title", "body"]
    success_url = reverse_lazy("list")

class BlogDelete(DeleteView):   # html : "이거 진짜 지울거야?" : (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy("list")