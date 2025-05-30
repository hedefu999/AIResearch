# 学习django的表单处理
from django import forms
from .models import Topic,Entry

'''
下面这段代码翻译成java
public class TopicForm extends ModelForm {
    // 使用内部静态类保存配置
    public static class Meta {
        public Class<?> model = Topic.class;
        public String[] fields = {"text"};
    }
}
让类本身携带额外的元信息（metadata），但又不影响实例的行为。
这类似于 Java 中使用注解（annotations）或 XML 配置文件来描述类行为的方式，只不过 Python 更倾向于用类结构本身来表达这些配置。
'''
class TopicForm(forms.ModelForm):
    # 定义嵌套内部类，存放django表单信息
    # 在 Django 中，class Meta 是一种约定俗成的写法，用于为类提供额外的配置信息，类似于 Java 中的配置类或注解，但更加简洁和灵活。
    class Meta:
        # 在 Python 中，类本身就是一种值（first-class object），可以像变量一样传递。所以这里不是model=Topic()
        # 类似java的 model=Topic.class
        model= Topic
        # Topic model中有 text\date_added 两个字段，这里声明只涉及text
        fields = ['text']
        # label会作为表单label展示
        labels = {'text':'主题名称: '}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        # 给字段指定空白标签
        labels = {'text':'请输入文本-label'}
        # 在python代码里控制html显示的表单元素，比较便捷
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

