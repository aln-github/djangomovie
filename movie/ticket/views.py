from django.shortcuts import render
from ticket.models import Movie
from ticket.forms import movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.
##    function-based
# def home(request):
#     m=Movie.objects.all()
#     return render(request,'home.html',{'m':m})

##   class-based
class HomeView(ListView):
    model=Movie
    template_name="home.html"
    context_object_name='m'

# def Detail(request,n):
#     m=Movie.objects.get(id=n)
#     return render(request,'detail.html',{'m':m})

class Detail(DetailView):
    model=Movie
    template_name = "detail.html"
    context_object_name='m'

# def Add_M(request):
#     if(request.method=="POST"):       # after form submission
#         form=movieform(request.POST,request.FILES)   # create form object with values entered by user
#         if form.is_valid():           # check validity of data
#             form.save()               # if valid form object is saved into database table book
#             return home(request)
#     form=movieform()
#     return render(request,'addmovie.html',context={'form':form})

class AddMovie(CreateView):
    model = Movie
    template_name="addmovie.html"
    fields = ['name','description','image']
    success_url = reverse_lazy('ticket:home')


# def update(request,n):
#     m = Movie.objects.get(id=n)
#     if (request.method == "POST"):  # after form submission
#         form = movieform(request.POST, request.FILES, instance=m)  # create form object with values entered by user
#         if form.is_valid():  # check validity of data
#             form.save()  # if valid form object is saved into database table book
#             return home(request)
#     form = movieform(instance=m)
#     return render(request, 'addmovie.html', context={'form': form})

class Update(UpdateView):
    model = Movie
    template_name = "addmovie.html"
    fields = ['name','description','image']
    success_url = reverse_lazy('ticket:home')


# def delete(request,n):
#     m = Movie.objects.get(id=n)
#     m.delete()
#     return home(request)

class Delete(DeleteView):
    model = Movie
    template_name = "delete.html"
    success_url = reverse_lazy('ticket:home')

