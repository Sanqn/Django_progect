from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# def leo(request):
#     return HttpResponse('Zodiac sign Leo')
#
# def scorpio(request):
#     return HttpResponse('Zodiac sign Scorpio')
#
# def aries(request):
#     return HttpResponse('Zodiac sign Aries')
#
# def taurus(request):
#     return HttpResponse('Zodiac sign Taurus')
#
# def gemini(request):
#     return HttpResponse('Zodiac sign Gemini')
zodiac = {"aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
          "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
          "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
          "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
          "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
          "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
          "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
          "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
          "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
          "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
          "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
          "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)"
          }

types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'ears': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}

def index(request):
    zodiacs = list(zodiac)
    li_zodiac = ''
    for sign in zodiacs:
        puth_url = reverse('url_revers', args=[sign])
        li_zodiac += f"<li><a href='{puth_url}'>{sign.title()}</a></li>"
    response = f'''
    <ul>
        {li_zodiac}
    </ul>
    '''
    return HttpResponse(response)


def get_more_sigen_zodiac(request, sigen_zodiac: str):  # dynamic URLS
    description = zodiac.get(sigen_zodiac, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    # if sigen_zodiac == 'leo':
    #     return HttpResponse('Zodiac sign Leo')
    # elif sigen_zodiac == 'scorpio':
    #     return HttpResponse('Zodiac sign Scorpio')
    # elif sigen_zodiac == 'aries':
    #     return HttpResponse('Zodiac sign Aries')
    # elif sigen_zodiac == 'taurus':
    #     return HttpResponse('Zodiac sign Taurus')
    # elif sigen_zodiac == 'gemini':
    #     return HttpResponse('Zodiac sign Gemini')
    else:
        return HttpResponseNotFound(f'Unknown sign zodiac {sigen_zodiac}')

def get_more_sigen_zodiac_by_number(request, sigen_zodiac: int):
    zodiacs = list(zodiac)
    if sigen_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Unknown sign number of zodiac {sigen_zodiac}')
    name_zodiac = zodiacs[sigen_zodiac - 1]
    new_revers_url = reverse('url_revers', args=[name_zodiac])
    return HttpResponseRedirect(new_revers_url)

def type(request):
    type_sign = list(types)
    list_type_sign = ''
    for typ in type_sign:
        link_tupe_sign = reverse('url_type', args=[typ])
        list_type_sign += f"<li><a href='{link_tupe_sign}'>{typ}</a></li>"
    resource = f'''
    <ul>
        {list_type_sign}
    </ul>
    '''
    return HttpResponse(resource)

def get_type_sign(request, type_sign):
    sign_of_type = types.get(type_sign, None)
    if sign_of_type:
        list_type_one_sign = ''
        for four in sign_of_type:
            link_tupe_one_sign = reverse('url_revers', args=[four])
            list_type_one_sign += f"<li><a href='{link_tupe_one_sign}'>{four}</a></li>"
        resource = f'''
            <ul>
                {list_type_one_sign}
            </ul>
            '''
        return HttpResponse(resource)

# def get_four_digits(request, sigen_zodiac):
#     return HttpResponse(f'This is page {sigen_zodiac}')
#
#
# def get_date(request, sigen_zodiac):
#     return HttpResponse(f'This date is {sigen_zodiac}')