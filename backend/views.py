from django.shortcuts import render

posts = [
    {
        'author': 'ViktorS',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': '2022-09-20'
    },
    {
        'author': 'John Doe',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': '2022-09-21'
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
