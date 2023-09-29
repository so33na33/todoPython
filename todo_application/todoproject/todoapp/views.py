from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import updateForms
from .models import Todo
# Create your view
#
# <-------usig class -->
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class todoList(ListView):
    model = Todo
    template_name = 'demo.html'
    context_object_name = 'key'

class todoDetail(DetailView):
    model = Todo
    template_name = 'next.html'
    context_object_name = 'key1'

class todoUpdate(UpdateView):
    model = Todo
    template_name = 'update.html'
    context_object_name = 'key'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:todoDetail',kwargs={'pk':self.object.id})


class todoDelete(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:todolist')
# s here
def demo(request):
    var = Todo.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        todo=Todo(name=name,priority=priority,date=date)
        todo.save()
    return render(request,"demo.html",{'key':var})

# def demo1(request):
#     var=Todo.objects.all()
#     return render(request, "next.html",{'key':var})

def delete(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=='POST':
        todo.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    todo=Todo.objects.get(id=id)
    form=updateForms(request.POST or None,instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,"update.html",{'form':form,'todo':todo})
