from django.http import HttpResponse
from django.shortcuts import render 
from django.utils import timezone

from .models import User, Post # so we can use data in the Post table

from .forms import PostForm

def index(request):
    # render (request, template, context to be filled into the template)
    return render(request, 'instagram/index.html', {})

def viewPost(request):
    class MixContent:
        def __init__(self):
            self.text = None
            self.img = None
            
    # we want to display all the posts in this page
    items = Post.objects.all();
    post_list = []

    for x in items:
        # process multiline content first before adding them to the list
        content = x.content.split('\n')
        mixContentList = []
        for i in range(len(content)):
            mix = MixContent()
            if '<img>' in content[i]:
                mix.img = content[i][5:]
                mix.img = mix.img[0:len(mix.img) - 1]
                print('------------')
                for pp in mix.img:
                    print(pp)
                print('------------')
            else:
                mix.text = content[i]
            mixContentList.append(mix)
        x.mycontent = mixContentList

        
        post_list.append(x)
    post_list.reverse() # this function helps you to reverse a list

    # 字典，template里面什么词是什么东西
    context = {
        'post_list': post_list
    }
    
    # render (request, template, context to be filled into the template)
    return render(request, 'instagram/viewPost.html', context)

def ViewPostById(request, postId):
    # get this post
    # pk means primary key, a number to identify a post
    mypost = Post.objects.get(pk=postId)

    context = {
        'post': mypost,
    }

    # render this post with viewPostDetail template
    return render(request, 'instagram/viewPostDetail.html', context)
    

def viewUsers(request):
    # get all users from the database
    users = User.objects.all()
    user_list = []
    for x in users:
        user_list.append(x)
        print('----------')
        if x.profile_picture:
            print(x.profile_picture.pic)
    
    context = {
        'user_list': users
    }

    return render(request, 'instagram/viewAllUsers.html', context)

def viewUserById(request, userId):
    user = User.objects.get(pk=userId)

    context = {
        'user': user,
    }

    # render this post with viewPostDetail template
    return render(request, 'instagram/viewUserDetail.html', context)

def newPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Process form data here
            # For example, save data to a database
            # 1. find the user
            print(form.cleaned_data)
            user = User.objects.get(username=form.cleaned_data['user'])

            # 2. make a new post, bind this user to that post
            newP = Post(
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                timeCreated = timezone.now(),
                author = user
            )
            newP.save()
    else:
        form = PostForm()

    return render(request, 'instagram/newPost.html', {'form': form})