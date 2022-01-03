from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from .models import Post


class Home(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context['posts'] = posts

        return context


class About(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Contact(TemplateView):
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Dashboard(TemplateView):
    template_name = 'blog/dashbord.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if request.user.is_authenticated:
            return super(TemplateView, self).render_to_response(context)
        else:
            return HttpResponseRedirect('/login/')




class Login(TemplateView):
    template_name = 'blog/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = LoginForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=uname, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully!!')
                return HttpResponseRedirect('/dashboard/')
        context['form'] = form
        return super(TemplateView, self).render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if request.user.is_authenticated:
            return HttpResponseRedirect('/dashboard/')
        else:
            return super(TemplateView, self).render_to_response(context)


class Signup(TemplateView):
    template_name = 'blog/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SignUpForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
        context['form'] = form
        return super(TemplateView, self).render_to_response(context)


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
