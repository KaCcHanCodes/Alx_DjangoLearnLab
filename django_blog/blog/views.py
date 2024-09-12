from django.shortcuts import render, redirect
from .forms import CustomUserForm, PostUpdate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/login')  
    
    form = CustomUserForm()
    context = {'form': form}
    return render(request, 'blog/register.html', context)

def customlogin(request):
    if not request.user.is_authenticated():
        print("User not authenticated. Redirecting User to login page")
        return redirect('blog/base')
     
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.authenticate(
                                    username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('blog/base')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'blog/login.html', context)

@login_required
def customlogout(request):
    logout(request)
    return redirect('blog/base')

def home(request):
    return render(request, 'blog/base.html')

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

@login_required
class posts(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_gueryset(self):
        return Post.objects.all()
    
class postdetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class postupdate(LoginRequiredMixin, UpdateView):
    form_class = PostUpdate
    template_name = 'blog/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class postcreate(LoginRequiredMixin, CreateView):
    form_class = PostUpdate
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class postdelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'