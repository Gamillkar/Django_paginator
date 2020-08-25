from collections import Counter
from django.shortcuts import render_to_response


counter_show = Counter()
counter_click = Counter()


def index(request):

    from_type = request.GET
    if "from-landing" in from_type:
        counter_click[from_type["from-landing"]] += 1
    return render_to_response('index.html')


def landing(request):
    type_landing = request.GET.get('ab-test-arg', 'original ')
    counter_show[type_landing] += 1
    if type_landing == 'test':
        return render_to_response('landing_alternate.html')
    return render_to_response('landing.html')



def stats(request):
    try:
        ratio_original = counter_click['original']/counter_show['original']

    except:
        ratio_original = 0
    try:
        ratio_test = counter_click['test'] / counter_show['test']
    except:
        ratio_test = 0
    return render_to_response('stats.html', context={
        'test_conversion': ratio_test,
        'original_conversion': ratio_original,
    })



