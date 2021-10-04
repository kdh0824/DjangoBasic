from django.shortcuts import render, redirect

from .models import User


# from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        userid = request.POST.get('id', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        email = request.POST.get('email', None)
        mobile = request.POST.get('mobile', None)
        username = request.POST.get('username', None)

        res_data = {}

        if not (userid and password and re_password and email and mobile and username):
            res_data['error'] = '비어있는 필드가 있습니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(
                id=userid,
                password=password,
                email=email,
                mobile=mobile,
                username=username
            )

            user.save()
            return redirect('/user/login')
            # return render(request, 'login.html')
        return render(request, 'register.html', res_data)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
