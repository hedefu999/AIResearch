from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    '''注册新用户'''
    if request.method != 'POST':
        # 显示空白的注册表单
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # 将用户名和密码的hash值保存到库中
            new_user = form.save()
            # 为用户创建有效会话，自动登录
            login(request, new_user)
            # 重定向到主页
            return redirect('learning_logs:index')
    # 显示空表单或指出表单无效
    context = {'form':form}
    return render(request, 'registration/register.html', context)

