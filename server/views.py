from django.contrib.auth import authenticate, login, get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/profile/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required(login_url='/login/')
def profile_view(request):
    user_profile = request.user
    if user_profile.is_staff == 1:
        all_users = get_user_model().objects.all()
        print(all_users)
        return render(request, 'profile.html', {'users': all_users,'user_profile': user_profile})
    return render(request, 'profile.html', {'user_profile': user_profile})

def logout_view(request):
    logout(request)
    return redirect('/login/')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        role = int(request.POST.get('role'))
        

        # Create a new user
        user = get_user_model().objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname, is_staff=role)
        
        # Log the user in
        login(request, user)

        return redirect('/profile/')
    return render(request, 'signup.html')

def homepage(request):
    return redirect('/profile/')

def change_password(request):
    if request.method == 'POST':
        print(request.method)
        user = request.user
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        new_password2 = request.POST.get('new_password2')

        # Check old password
        if not user.check_password(old_password):
            return render(request, 'change_password.html', {'error': 'Old password is wrong'})
        
        # Check new password equals to old password
        if old_password == new_password:
            return render(request, 'change_password.html', {'error': 'New password cannot be the same as old password'})
        
        # Check new password equals to new password2
        if new_password != new_password2:
            return render(request, 'change_password.html', {'error': 'New password does not match'})
        
        # Change the password
        user.set_password(new_password)
        user.save()
        return redirect('/profile/')
    print("hello")
    return render(request, 'change_password.html')

@login_required(login_url='/login/')
def test_token(request):
    return JsonResponse({"message": "Token is valid."})

@login_required(login_url='/login/')
def view_profile(request):
    user_profile = request.user
    # Adjust the following line based on your UserProfile model and serializer
    profile_data = {"username": user_profile.username, "email": user_profile.email}
    return JsonResponse(profile_data)
