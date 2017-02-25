from django.shortcuts import render, HttpResponse
import requests



def index(request):
    return HttpResponse('Hello World')

def test(request):
    return HttpResponse('My second view!')

def profile(request):
    parseddata = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonlist = []
        jsonlist.append(req.json())
        userdata = {}
        for data in jsonlist:
            userdata['name'] = data['name']
            userdata['blog'] = data['blog']
            userdata['email'] = data['email']
            userdata['public_gists'] = data['public_gists']
            userdata['public_repos'] = data['public_repos']
            userdata['avatar_url'] = data['avatar_url']
            userdata['followers'] = data['followers']
            userdata['following'] = data['following']
        parseddata.append(userdata)
    return render(request, 'app/profile.html', {'data': parseddata})
