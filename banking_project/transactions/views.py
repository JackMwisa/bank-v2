from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .crypto import SimpleCrypt
from .signature import SimpleSign

SECRET_KEY = 5  # Change this to a secure secret key

crypt = SimpleCrypt(SECRET_KEY)
sign = SimpleSign(SECRET_KEY)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Encrypt username for session
            encrypted_username = crypt.encrypt(username)
            request.session['encrypted_username'] = encrypted_username
            # Sign username for session integrity
            signature = sign.sign(encrypted_username)
            request.session['signature'] = signature
            return redirect('index')
        else:
            return HttpResponse("Invalid username or password")
    else:
        return render(request, 'accounts/login.html')

def logout_user(request):
    # Decrypt username from session
    encrypted_username = request.session.get('encrypted_username')
    if encrypted_username:
        username = crypt.decrypt(encrypted_username)
        # Verify username integrity
        signature = request.session.get('signature')
        if sign.verify(encrypted_username, signature):
            logout(request)
            return HttpResponse(f"Logged out successfully. User: {username}")
        else:
            return HttpResponse("Session integrity compromised")
    else:
        return HttpResponse("User not logged in")
