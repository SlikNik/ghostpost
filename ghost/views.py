  
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ghost.models import GhostPost
from ghost.forms import GhostPostForm


def index(request):
    all_post = GhostPost.objects.order_by('post_date')
    return render(request, 'index.html', {'posts': all_post, 'tab': 'active'})

def sort(request):
    '''Resource: https://stackoverflow.com/questions/981375/using-a-django-custom-model-method-property-in-order-by'''
    sorted_post = sorted(GhostPost.objects.all(), key=lambda p: p.total_votes, reverse=True)
    return render(request, 'sorted_post.html', {'posts': sorted_post, 'tab': 'active'})

def boast(request):
    boasts = GhostPost.objects.filter(type_of_post=True).order_by('post_date')
    return render(request, 'all_post.html', {'posts': boasts, 'boast': 'active', 'type': 'Boast'})

def roast(request):
    roasts = GhostPost.objects.filter(type_of_post=False).order_by('post_date')
    return render(request, 'all_post.html', {'posts': roasts, 'roast': 'active', 'type': 'Roast'})

def post(request, secret):
    current_post = GhostPost.objects.filter(secret=secret).first()
    return render(request, 'post.html', {'post': current_post})

def delete(request, id):
    current_post = GhostPost.objects.filter(id=id).first()
    current_post.delete()
    return render(request, 'delete.html', {'id': id})

def create_post(request):
    if request.method == 'POST':
        form = GhostPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.secret_key()
            key = new_post.secret
            print(key)
            new_post.save()
            form.save_m2m()
            # breakpoint()
            return render(request, 'create_post.html', {'key': key})
            # return HttpResponseRedirect(reverse('createpost', {'key': key}))
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
