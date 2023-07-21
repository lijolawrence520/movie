from django.http import HttpResponse
from django.shortcuts import render,redirect
from.models import Movie
from.forms import MovieForm
from django.views.generic import ListView


# class TaskListview(ListView):
#     model=Movie
#     template_name='index.html'
#     context_object_name = 'movie'

# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={'movie_list':movie}
    return render(request,'index.html',context)


def detail(request,movie_id):
    return HttpResponse("hello is movie no %s" %movie_id)

def det(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'mo':movie})

def addm(request):
    if request.method == "POST" :
        nam=request.POST.get('name',)
        des = request.POST.get('desc',)
        yer = request.POST.get('year', )
        img = request.FILES['img']
        mo=Movie(name=nam,desc=des,year=yer,img=img)
        mo.save()

    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def dell(request,id):
   if request.method=='POST':
      movie=Movie.objects.get(id=id)
      movie.delete()
      return redirect('/')
   return render(request,'delete.html')