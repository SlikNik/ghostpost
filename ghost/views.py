  
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ghost.models import GhostPost
from ghost.forms import GhostPostForm


def index(request):
    all_post = GhostPost.objects.order_by('post_date')
    return render(request, 'index.html', {'posts': all_post, 'tab': 'active'})

def boast(request):
    boasts = GhostPost.objects.filter(type_of_post=True).order_by('post_date')
    return render(request, 'post.html', {'posts': boasts, 'boast': 'active', 'type': 'Boast'})

def roast(request):
    roasts = GhostPost.objects.filter(type_of_post=False).order_by('post_date')
    return render(request, 'post.html', {'posts': roasts, 'roast': 'active', 'type': 'Roast'})

def create_post(request):
    if request.method == 'POST':
        form = GhostPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('createpost'))
    form = GhostPostForm()
    return render(request, 'create_post.html', {'form': form, 'tab': 'active'})

def up_vote(request, id):
    current_post = GhostPost.objects.get(id=id)
    current_post.up_votes += 1
    current_post.save()
    # print(current_post)
    try: 
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        return HttpResponseRedirect(reverse('homepage'))



def down_vote(request, id):
    current_post = GhostPost.objects.get(id=id)
    current_post.down_votes -= 1
    current_post.save()
    # print(current_post)
    try: 
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        return HttpResponseRedirect(reverse('homepage'))
