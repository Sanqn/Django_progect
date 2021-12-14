from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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

def create_day(request, new_day: str):
    week = all_day.get(new_day, None)
    if week:
        return HttpResponse(week)
    # if new_day == 'monday':
    #     return HttpResponse('Good day monday')
    # elif new_day == 'tuesday':
    #     return HttpResponse('Good day tuesday')
    else:
        return HttpResponseNotFound(f'{new_day} is not of week')

def create_day_number(request, new_day: int):
    if new_day <= 7:
        return HttpResponse(f'Today is {new_day} of the week')
    else:
        return HttpResponseNotFound(f'Unknown number day {new_day}')
