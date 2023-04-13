from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm


from .models import *
from .forms import *


def change_password(request):
	success_url = reverse_lazy('change_password_success')
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return HttpResponseRedirect(success_url)
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'accounts/change_password.html', {
		'form': form
	})

def change_name(request):
	success_url = reverse_lazy('change_password_success')
	if request.method == 'POST':
		form = UserChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return HttpResponseRedirect(success_url)
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = UserChangeForm(request.user)
	return render(request, 'accounts/change_name.html', {
		'form': form
	})

def deletes(request, pk):
    post = Posts.objects.get(id=pk)
    post.delete()
    return redirect('/')

def rubric_list(request, rubric_id):
    posts =  Post.objects.filter(rubric=rubric_id)
    current_rubric = Rubric.objects.get(id=rubric_id)
    rubrics = Rubric.objects.all()
    context = {
        'rubrics':rubrics,
        'posts':posts,
        'current_rubric':current_rubric,
    }
    return render(request, 'rubric_list.html', context) 

class Register(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register-success')

	def get_success_url(self):
		if not self.success_url:
			raise ImproperlyConfigured('No URL to redirect to.')
		return str(self.success_url)

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(self.success_url)

def search(request):
	query = request.GET.get('q')
	object_list = Posts.objects.filter(Q(title__icontains=query))
	context = {
		'object_list':object_list
	}
	return render(request, 'search.html', context)

def pinterest(request):
	return render(request, 'pinterest.html')

def about_us(request):
	return render(request, 'about_us.html')

def contact(request):
	return render(request, 'contact.html')

def menu(request):
	posts = Posts.objects.all()
	rubric = Category.objects.all()
	context = {
		'posts':posts,
		'rubric':rubric,
	}
	return render(request, 'menu.html', context)

def rubrics(request, rubric_id):
	posts = Posts.objects.filter(category=rubric_id)
	rubric = Category.objects.all()
	context = {
		'posts':posts,
		'rubric':rubric,
	}
	return render(request, 'rubric.html', context)

def chanels(request):
	posts = Posts.objects.filter(user=request.user)
	context = {
		'posts':posts,
	}
	return render(request, 'chanel.html', context)



class details(DetailView, FormMixin):
    model=Posts
    template_name='detail.html'
    form_class=CommentsForm
    context_object_name='product'
    success_url= reverse_lazy('menu')

    def post(self,request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.product=self.get_object()
        self.object.save()
        return super().form_valid(form)


def create(request):
	form = PostsForm()
	if request.method == 'POST':
		form = PostsForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.save()
			return redirect('/')
	context = {
		'form':form
	}
	return render(request, 'create.html', context)

def edit(request, pk):
	pass

def delete(request, pk):
	post  = Posts.objects.get(id=pk)
	post.delete()
	return reimage.png