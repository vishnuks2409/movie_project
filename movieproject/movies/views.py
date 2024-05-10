from django.shortcuts import render
from .models import Movie
from .form import Moviefrom
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

#Function based
# def home(request):
#     movies=Movie.objects.all()
#     return render(request,'home.html',{'movies':movies})

#CLass based
class Homeview(ListView):
    model=Movie
    template_name="home.html"
    context_object_name='movies'

# def add(request):
#     if(request.POST):
#         form=Moviefrom(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     else:
#         form=Moviefrom()
#     return render(request,'add.html',{'form':form})

class Addmovie(CreateView):
    model = Movie
    template_name = "add.html"
    fields = ['name','year','desc','image']
    success_url = reverse_lazy('movies:home') #after create connect to home page


# def view(request,n):
#     m=Movie.objects.get(id=n)
#     return render(request,'view.html',{'m':m})

class Detail_view(DetailView):
    model = Movie
    template_name = "view.html"
    context_object_name = 'm'


# def delete(request,n):
#     m=Movie.objects.get(id=n)
#     m.delete()
#     return home(request)

class Delete_view(DeleteView):
    model = Movie
    template_name = "delete.html"
    success_url = reverse_lazy('movies:home')


# def update(request,n):
#     b = Movie.objects.get(id=n)
#     if (request.method == 'POST'):
#         form = Moviefrom(request.POST, request.FILES, instance=b)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     else:
#         form = Moviefrom(instance=b)
#     return render(request, 'add.html', {'form': form})

class Update_view(UpdateView):
    model = Movie
    template_name = "add.html"
    fields = ['name', 'year', 'desc', 'image']
    success_url = reverse_lazy('movies:home')