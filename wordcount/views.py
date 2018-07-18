from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """Returns rendered web page
    Arguments:
        request {Request} -- the request to be processed
    Returns:
        HttpResponse -- The response after request has been processed
    """

    return render(request, 'home.html', {'dog': 'Mark'})


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split(' ')
    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_words = sorted(
        word_dict.items(), key=lambda value: value[1], reverse=True)

    return render(
        request, 'count.html', {
            'fulltext': fulltext,
            'count': len(word_list),
            'sorted_words': sorted_words
        })


def about(request):
    return render(request, 'about.html')