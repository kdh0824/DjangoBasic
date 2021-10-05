from django.shortcuts import render, redirect

from .models import User

import bcrypt


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
                password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
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

    elif request.method == 'POST':
        userid = request.POST.get('id', None)
        password = request.POST.get('password', None)

        res_data = {}

        if not (userid and password):
            res_data['error'] = '비어있는 필드가 있습니다.'
        else:
            try:
                user = User.objects.get(id=userid)

            except Exception as ex:
                print('에러발생', ex)
                res_data['error'] = '존재하지 않는 아이디 또는 비밀번호가 틀렸습니다.'
                return render(request, 'login.html', res_data)

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                print('정답')

        return render(request, 'login.html', res_data)
