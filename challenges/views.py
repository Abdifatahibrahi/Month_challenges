from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string



month_challenge = {
    'january': 'This is January',
    'february': 'This is February',
    'march': 'This is March',
    'april': 'This is April',
    'May': 'This is May',
    'June': 'This is June coldest',
    'July': 'This is July',
    'August': 'This is August',
    'September': 'This is September',
    'October': 'This is October',
    'November': 'This is November',
    'December': None,
    

}

def index(request):
    list_item = ''
    months = list(month_challenge.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenge", args=[month])
        list_item += f"<li><a href=\"{month_path}\">{capitalized_month}</a><li>"
    
    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)





# def monthly_challenges_by_number(request, month):

#     months = list(month_challenge.keys())
#     redirected_month = months[month - 1]
#     redirected_path = reverse('monthly-challenge', args=[redirected_month])
#     return HttpResponseRedirect(redirected_path)



# def monthly_challenges(request, month):
#     try:
#         challenge_text = month_challenge[month]
#         challenge_data = f"<h1>{challenge_text}</h1>"
#         return HttpResponse(challenge_data)
        
#     except:
#         return HttpResponseNotFound("Invalid month")
    
    


def monthly_challenges(request, month):
    try:
        mymonth = month_challenge[month]
        return render(request, "challenges/challenges.html", 
        {
            'text': mymonth,
            'month_name': month
        
        })
      
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)


def monthly_challenges_by_number(request, month):
    months = list(month_challenge.keys())
    mymonth = months[month - 1]

    redirected_month = reverse("monthly-challenge", args=[mymonth])

    return HttpResponseRedirect(redirected_month)


def index(request):
    months = list(month_challenge.keys())


    

    return render(request, "challenges/index.html", {
        "months": months
    })
