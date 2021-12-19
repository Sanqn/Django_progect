from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
# zodiac = {"aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
#           "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
#           "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
#           "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
#           "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
#           "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
#           "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
#           "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
#           "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
#           "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
#           "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
#           "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)"
#           }
#
types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'ears': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}

zodiac = {
    'aries':
        {'description': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
         'types': 'fire',
         'day_start': 21,
         'month_start': 3,
         'day_finish': 20,
         'month_finish': 4,
         'si': 'aries'
         },
    'taurus':
        {'description': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
         'types': 'earth',
         'day_start': 21,
         'month_start': 4,
         'day_finish': 21,
         'month_finish': 5,
         'si': 'taurus'
         },
    'gemini':
        {'description': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
         'types': 'air',
         'day_start': 22,
         'month_start': 5,
         'day_finish': 21,
         'month_finish': 6,
         'si': 'gemini'
         },
    'cancer':
        {'description': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
         'types': 'water',
         'day_start': 22,
         'month_start': 6,
         'day_finish': 22,
         'month_finish': 7,
         'si': 'cancer'
         },
    'leo':
        {'description': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
         'types': 'fire',
         'day_start': 23,
         'month_start': 7,
         'day_finish': 21,
         'month_finish': 8,
         'si': 'leo'
         },
    'virgo':
        {'description': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
         'types': 'earth',
         'day_start': 22,
         'month_start': 8,
         'day_finish': 23,
         'month_finish': 9,
         'si': 'virgo'
         },
    'libra':
        {'description': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
         'types': 'air',
         'day_start': 24,
         'month_start': 9,
         'day_finish': 23,
         'month_finish': 10,
         'si': 'libra'
         },
    'scorpio':
        {'description': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
         'types': 'water',
         'day_start': 24,
         'month_start': 10,
         'day_finish': 22,
         'month_finish': 11,
         'si': 'scorpio'
         },
    'sagittarius':
        {'description': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
         'types': 'fire',
         'day_start': 23,
         'month_start': 11,
         'day_finish': 22,
         'month_finish': 12,
         'si': 'sagittarius'
         },
    'capricorn':
        {'description': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
         'types': 'earth',
         'day_start': 23,
         'month_start': 12,
         'day_finish': 20,
         'month_finish': 1,
         'si': 'capricorn'

         },
    'aquarius':
        {'description': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
         'types': 'air',
         'day_start': 21,
         'month_start': 1,
         'day_finish': 19,
         'month_finish': 2,
         'si': 'aquarius'
         },
    'pisces':
        {'description': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
         'types': 'water',
         'day_start': 20,
         'month_start': 2,
         'day_finish': 20,
         'month_finish': 3,
         'si': 'pisces'
         }
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


class Person:

    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    def __str__(self):
        return f'Hi, my name is {self.name} and me {self.age} years old.'


def get_more_sigen_zodiac(request, sigen_zodiac: str):  # dynamic URLS
    all = zodiac.get(sigen_zodiac, None)
    description = all.get('description', None)
    data = {'description_zodiac': description,
            'sign_of_zodiac': sigen_zodiac.title(),
            'dict_list': {'name': 'Bil', 'age': 17},
            'class_list': Person('Nick', 18)
            }
    return render(request, 'djangoweb/info_djangoweb.html', data)
    # response = render_to_string('djangoweb/info_djangoweb.html')
    # return HttpResponse(response)
    # all = zodiac.get(sigen_zodiac, None)
    # description = all.get('description', None)
    # if description:
    #     return HttpResponse(f'<h2>{description}</h2>')
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
    # else:
    #     return HttpResponseNotFound(f'Unknown sign zodiac {sigen_zodiac}')


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
        list_type_sign += f"<li><a href='{link_tupe_sign}'>{typ.title()}</a></li>"
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
            list_type_one_sign += f"<li><a href='{link_tupe_one_sign}'>{four.title()}</a></li>"
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

def check_day(request, month, day):
    if day > 31 or month > 12:
        return HttpResponseNotFound(f'<h2>This page not found</h2>')
    else:
        for i in zodiac:
            if (day >= zodiac[i]['day_start'] and month == zodiac[i]['month_start']) or (
                    day <= zodiac[i]['day_finish'] and month == zodiac[i]['month_finish']):
                return HttpResponse(f"<h2>{zodiac[i]['si']}</h2>")
