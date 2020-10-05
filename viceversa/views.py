from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    words = user_text.split()
    length = len(words)
    reversed_text = user_text[::-1]
    print(user_text)
    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext':reversed_text, 'length': length})