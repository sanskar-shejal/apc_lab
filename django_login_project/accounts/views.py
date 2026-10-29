import re
from django.shortcuts import render

def login_view(request):
    username = ''
    error_message = None
    success_message = None

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username:
            error_message = 'Please enter a username.'
        elif not re.match(r'^[A-Za-z][A-Za-z0-9_]{2,15}$', username):
            error_message = 'Invalid username. It must start with a letter, contain only letters, numbers, and underscores, and be 3 to 16 characters long.'
        elif len(password) < 8:
            error_message = 'Password must be at least 8 characters long.'
        else:
            success_message = 'Input validation successful'

    context = {
        'username': username,
        'error_message': error_message,
        'success_message': success_message,
    }
    return render(request, 'login.html', context)

