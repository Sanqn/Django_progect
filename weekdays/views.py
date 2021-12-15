from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# def monday(request):
#     return HttpResponse('Good day monday')
#
# def tuesday(request):
#     return HttpResponse('Good day tuesday')

all_day = {
    'monday': 'Nice Monday',
    'tuesday': 'Nice Tuesday',
    'wednesday': 'Nice Wednesday',
    'thursday': 'Nice Thursday',
    'friday': 'Nice Friday',
    'saturday': 'Nice Saturday, putty',
    'sunday': 'Nice Sunday, do nay stop',
}

def index(request):
    days = list(all_day)
    list_days = ''
    for day_of in days:
        redirect_days = reverse('revers_url_day', args=[day_of])
        list_days += f"<li><a href='{redirect_days}'>{day_of}</a></li>"

    click_day = f'''
    <ul>
    {list_days}
    </ul>
    '''
    return HttpResponse(click_day)

def create_day(request, new_day: str):
    week = all_day.get(new_day, None)
    if week:
        return HttpResponse(f'<h2>{week}</h2>')
    # if new_day == 'monday':
    #     return HttpResponse('Good day monday')
    # elif new_day == 'tuesday':
    #     return HttpResponse('Good day tuesday')
    else:
        return HttpResponseNotFound(f'{new_day} is not of week')


def create_day_number(request, new_day: int):
    # if new_day <= 7:
    #     return HttpResponse(f'Today is {new_day} of the week')
    # else:
    #     return HttpResponseNotFound(f'Unknown number day {new_day}')
    days = list(all_day)
    if new_day > len(days):
        return HttpResponseNotFound(f'Unknown number day {new_day}')
    name_day = days[new_day - 1]
    urls_days = reverse('revers_url_day', args=[name_day])
    return HttpResponseRedirect(urls_days)


