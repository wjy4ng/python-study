from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            print("로그인 성공")
            login(request, user)
        else:
            print("로그인 실패")

    return render(request, 'users/login.html')