from django.shortcuts import render,get_object_or_404,redirect
from .models import Idea
from django.utils import timezone
from .forms import IdeaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    ideas= Idea.objects
    return render(request, 'blog/home.html',{'ideas':ideas})

@login_required
def detail(request, idea_id):
    idea_detail =get_object_or_404(Idea,pk=idea_id)
    return render(request, 'blog/detail.html',{'idea':idea_detail}
)   

def idea_new(request):
    if request.method =="POST":
        form=IdeaForm(request.POST)
        if form.is_valid():
            idea=form.save(commit=False)
            idea.published_date=timezone.datetime.now()
            idea.save()
            return redirect('detail', idea_id=idea.pk)

    else:
        form=IdeaForm()
    return render(request, 'blog/idea_new.html',{'form':form})    

def idea_edit(request, idea_id):
    idea=get_object_or_404(Idea, pk=idea_id)
    if request.method=="POST":
        form =IdeaForm(request.POST ,instance=idea)
        if form .is_valid():
            idea=form.save(commit=False)
            idea.published_date=timezone.datetime.now()
            idea.save()
            return redirect('detail', idea_id=idea.pk)
    else:
        form=IdeaForm(instance=idea)
    return render(request,'blog/idea_edit.html',{'form':form}) 


def idea_delete(request, idea_id):
    idea=get_object_or_404(Idea,pk=idea_id)
    idea.delete()
    return redirect('home')
 
