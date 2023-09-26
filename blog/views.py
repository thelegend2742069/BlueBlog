from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Pranav',
        'title': 'My First Post',
        'content': 'Post Number 1',
        'date_posted': 'September 26, 2023'
    },
    
    {
        'author': 'Spiderman',
        'title': 'AAAAAAAAAAAAAAAAAAAAAAA',
        'content': 'spiders are fucking terrifying\nwhy did I have to become a spider\nwhy not something nicer like a butterflys',
        'date_posted': 'September 26, 2023'
    },
]

def home(request):
    context = {'posts': posts}

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')