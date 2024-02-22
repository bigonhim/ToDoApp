from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from.models import Task
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TaskList(LoginRequiredMixin,ListView):
    model=Task
    fields='__all__'
    template_name='remind/tasklist.html'
    context_object_name='tasks'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(complete=False).count()


        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input)
            
        return context
class UpdateTask(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']
    template_name='remind/updatetask.html'
    success_url=reverse_lazy('tasks')
class DeleteTask(LoginRequiredMixin,DeleteView):
    model=Task
    template_name='remind/delete.html'
    success_url=reverse_lazy('tasks')
class CreateTask(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description','complete']    
    template_name='remind/create.html'
    success_url=reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(CreateTask,self).form_valid(form)
    
class Login(LoginView):
    template_name='remind/login.html'
    next_page='tasks'
class Register(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='remind/register.html'
