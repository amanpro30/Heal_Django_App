from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .models import *
from nurse.models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@user_passes_test(lambda u: u.is_superuser)
@login_required
def add_blog(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author= request.user
            post.save()
            return redirect("/blog")
    else:
        form=PostForm()
    return render(request, 'blog/blog_post.html', {'form':form})
           

def view_post(request, slug):
    post=get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {'post':post})

def show(request):
    post1= Post.objects.all().order_by('-created_on')
    page = request.GET.get('page', 1)

    paginator = Paginator(post1, 5)
    try:
        post2 = paginator.page(page)
    except PageNotAnInteger:
        post2 = paginator.page(1)
    except EmptyPage:
        post2 = paginator.page(paginator.num_pages)
    return render(request, "blog/index.html", {'post1':post1, 'post2':post2})


#================Nurse===================#

def nurse_detail(request, **kwargs):
    id=kwargs['id']
    nurse=get_object_or_404(Nurse, id=int(id))
    comment=Comment.objects.filter(doctor=nurse)

    rcount=0.0
    count=0
    for i in comment:
        rcount=rcount+i.review
        count=count+1
    if count == 0:
        count =count +1
    if rcount == 0:
        rcount =rcount +1
    rcount=rcount/count
    rcount = "{0:0.1f}".format(rcount)

    arg = {'nurse':nurse, 'comment':comment, 'rcount':rcount, 'count':count}
    return render(request, "blog/doctor_detail.html", arg)

def nurse_reply(request, **kwargs):
    
    id=kwargs['id']
    if request.method=="POST":
        form=request.POST
        review=form['review']
        content=form['content']
        user=User.objects.get(username=request.user)
        doctor1=Nurse.objects.get(id=int(id))
        arg={'doctor':doctor1}
        reply = Comment.objects.create(user=user, doctor=doctor1, review=review, content=content)
        reply.save()
        return redirect('/blog/nurse/'+id+"/")


    return render(request, 'blog/comment.html')

def nurse(request):
    nurse= Nurse.objects.all()
        
    return render(request, 'blog/doctor.html', {'doctor':nurse})