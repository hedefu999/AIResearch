from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    '''学习笔记的主页'''
    return render(request,'learning_logs/index.html')

@login_required #添加登录检查装饰器，需要在settings.py中设置重定向的页面
def topics(request):
    '''显示所有主题 按创建人筛选'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def about(request):
    context={}
    return render(request, 'learning_logs/about.html', context)

@login_required
def topic(request, topic_id):
    """显示单个主题及其所有条目"""
    topic = Topic.objects.get(id=topic_id)
    '''确认该topic属于当前用户'''
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
        # 未提交数据：创建一个表单
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST) #对象form包含用户提交的信息
        # 校验表单字段不可为空，类型正确。Topic model text字段限制了长度，这里也会校验
        if form.is_valid():
            # 关联请求中的user再保存
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # form.save() #save会将表单数据写入数据库
            # 用户提交数据后重定向到topics网页，redirect函数将视图 learning_logs:topics作为参数，将用户重定向到与该视图相关联的网页
            return redirect('learning_logs:topics')
    # 显示空表单或指出表单数据无效
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''在特定主题中添加新条目'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic':topic,'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 通过instance指定库里查出来的原始数据对象，通过data设置表单传入的新值
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)
