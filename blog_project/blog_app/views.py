from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import CustomUser, BlogPost
from .serializers import BlogPostSerializer
from .forms import BlogPostForm

# 로그인 views
def login_view(request):
    # POST요청이 들어온다면
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        # 해당 유저가 존재한다면
        if user is not None:
            auth.login(request, user)
            return redirect('board_client')
        else:
            return render(request, 'registration/login.html', {'error':'ID와 password를 확인해주세요.'})
        
    return render(request, 'registration/login.html')

# 로그아웃 views
def logout_view(request):
    # 로그아웃 성공시 로그인 화면으로
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return render(request, 'registration/login.html')

# 회원가입 views

def signup_view(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirm']:
            username = request.POST['username']
            password = request.POST['password']
            password_confirm = request.POST['password_confirm']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone_number = request.POST['phone_number']

            try:
                user = CustomUser.objects.create_user(username=username, email=email, password=password)
                user.last_name = last_name
                user.first_name = first_name
                user.phone_number = phone_number
                user.save()
                return redirect('login')
            except Exception:
                return render(request, 'registration/signup.html', {'signup_error': '입력이 잘못됐습니다.'})
    return render(request, 'registration/signup.html')

def find_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        try:
            user = CustomUser.objects.get(username=username, phone_number=phone_number)
            return redirect('new_password', username=username)
        except CustomUser.DoesNotExist:
            # 사용자가 존재하지 않는 경우에 대한 처리
            return render(request, 'registration/find_password.html', {'new_error':'ID와 전화번호를 확인해주세요.'})
    return render(request, 'registration/find_password.html')

def new_password(request, username):
    user = CustomUser.objects.get(username=username)
    if request.method == 'POST':
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            user.set_password(password)
            user.save()
            return redirect('login')  # 비밀번호 재설정 후 로그인 페이지로 이동
        else:
            # 비밀번호가 일치하지 않을 때의 처리
            return render(request, 'registration/new_password.html', {'password_error':'비밀번호가 일치하지 않습니다.'})
    return render(request, 'registration/new_password.html')

def board_client(request):
    return render(request, 'blog_app/board_client.html')

def board_admin(request):
    return render(request, 'blog_app/board_admin.html')

def post(request):
    return render(request, 'blog_app/post.html')

def write(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')   
    else:
        form = BlogPostForm()
    return render(request, 'blog_app/write.html', {'form': form})


def find_password(request):
    return render(request, 'registration/find_password.html')

def new_password(request):
    return render(request, 'registration/new_password.html')