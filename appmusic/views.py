from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import View,CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate,login,logout
from .myforms import Mylogin,Register,Addalbum,Addsong
from .models import Album,Song
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    a=Album.objects.all()
    if request.user.is_authenticated:
        return render(request,'music/home1.html',{'album':a})
    else:
        return render(request,'music/home.html',{'album':a})

def detail(request,pk):
    a=get_object_or_404(Album,pk=int(pk))
    return render(request,'music/song.html',{'val':a})
class loginpage(View):
    def get(self,request):
        form=Mylogin(None)
        return render(request,'music/login.html',{'form':form})
    def post(self,request):
        form=Mylogin(request.POST)
        if form.is_valid():
            u=form.cleaned_data['username']
            p=form.cleaned_data['password']
            v=authenticate(username=u,password=p)
            n=request.GET.get('next',None)
            if v is not None:
                login(request,v)
                if n:
                    return redirect(n)
                else:
                    return redirect('appmusic:index')
            return render(request,'music/login.html',{'form':form})
class signup(CreateView):
    def get(self,request):
        form=Register(None)
        return render(request,'music/register.html',{'form':form})
    def post(self,request):
        form=Register(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            p=form.cleaned_data['password']
            data.set_password(p)
            data.save()
            return redirect('appmusic:login')
        return render(request,'music/register.html',{'form':form})
class addalbum(View):
    def get(self,request):
        form=Addalbum(None)
        return render(request,'music/addalbum.html',{'form':form})
    def post(self,request):
        form=Addalbum(request.POST,request.FILES)
        form.save()
        return redirect('appmusic:index')
class updatealbum(UpdateView):
    template_name = 'music/addalbum.html'
    model=Album
    fields = ['title','artist','genre','year','image']
    def form_valid(self, form):
        form.save()
        return redirect('appmusic:index')
class deletealbum(DeleteView):
    template_name = 'music/delete.html'
    model=Album
    success_url = reverse_lazy('appmusic:index')
def logout(request):
    logout(request)
    return redirect('appmusic:index')
class addsong(CreateView):
    template_name = 'music/addsong.html'
    context_object_name = 'form'
    model=Song
    fields = ['title','artist','genre','soundfile','image']
    def form_valid(self, form):
        i=self.kwargs.get('pk')
        a=Album.objects.get(pk=int(i))
        data=form.save(commit=False)
        data.al_id=a
        data.save()
        return redirect('appmusic:detail',a.id)
class updatesong(UpdateView):
    template_name = 'music/addsong.html'
    context_object_name = 'form'
    model = Song
    fields=['title','artist','genre','soundfile','image']
    def form_valid(self, form):
        form.save()
        a=Song.objects.get(id=int(self.kwargs.get('pk')))
        return redirect('appmusic:detail',a.al_id.id)
class deletesong(DeleteView):
    template_name = 'music/delete.html'
    model=Song
    def get_success_url(self):
        a=self.object.al_id
        return reverse_lazy('appmusic:detail',kwargs={'pk':a.id})