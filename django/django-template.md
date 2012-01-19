
## Django 学习
---  

#### 模板

* 变量由双大括号`{{ var }}`指定
* 标签由花括号+百分号`{% if boolVar %}` `{% for i in list %}` `{% endfor/endif %}`，注意行尾无冒号
* 对变量进行**Filter**过滤器，`{{ var|filter:"para" }}`，例如将`{{orderDate|date:"F,j,Y"}}`进行格式化，过滤器可串联
* 标签块`{% block id %}` `{% endblock %}`用于模板继承，子模板第一行必须为`{% extends BASE_TEMPLATE %}`
* `{% include OTHER_TEMPLATE %}`用于包含另一模板

模板示例代码：

    <html>
    <head><title>Ordering notice</title></head>
    <body>
    <h1>Ordering notice</h1>
    <p>Dear {{ person_name }},</p>
    <p>Thanks for placing an order from {{ company }}. It's scheduled to
    ship on {{ ship_date|date:"F j, Y" }}.</p>

    <p>Here are the items you've ordered:</p>
    <ul>
    {% for item in item_list %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
    {% if ordered_warranty %}
        <p>Your warranty information will be included in the packaging.</p>
    {% else %}
        <p>You didn't order a warranty, so you're on your own when
        the products inevitably stop working.</p>
    {% endif %}
    <p>Sincerely,<br />{{ company }}</p>
    </body>
    </html>

Python中使用Django模板：

    from django import template
    t = template.Template('my name is {{ name }}.')
    ctx = template.Context({'name' : 'hao'})
    print t.render(ctx)

> 转到用`django-admin.py startproject myproject`生成的`myproject`目录下，用`python manage.py shell`，该命令会自动使用django的配置文件。  

Template.render(ctx)返回的是一个Unicode对象，在后台用正则一次性解析完成。

Django模板系统的使用步骤：

* 创建Template
* 创建Context，即字典
* 调用Template.render(Context)，返回Unicode对象

##### 变量

Django中的模板能够传入对象，用点号调用对象的**无参数**方法，例如`person.name` `[ ].2`，但不允许使用list的负数索引。

    >>> from django.template import Template, Context
    >>> class Person:
    ...     def name(self):
    ...         return 'hao'
    ... 
    >>> t = Template('name is {{ person.name }}.')
    >>> c = Context({'person': Person()})
    >>> print t.render(c)
    name is hao.

如果变量不存在，Django模板默认以空字符串来代替。
Context对象创建后可以用Python的字典方法进行操作。

##### 标签

if/else/endif

* 不支持在一个判断中同时使用and和or，因为不能用小括号()
* 不支持elif，用嵌套判断代替

ifequal/else/endifequal & ifnotequal

* 判断两个变量值是否相等
* `{% ifequal var 123/1.23/'str'/"str" %}`

for/empty/endfor

* 当列表为空，用{% empty %}标签来代替
* 不支持退出循环`break` `continue`
* 模板变量`forloop`  
  

for标签模板变量

- forloop.counter 总是一个表示当前循环的执行次数的整数计数器。 这个计数器是从1开始的，所以在第一次循环时 forloop.counter 将会被设置为1。
- forloop.counter0 类似于 forloop.counter ，但是它是从0计数的。 第一次执行循环时这个变量会被设置为0。
- forloop.revcounter 是表示循环中剩余项的整型变量。 在循环初次执行时 forloop.revcounter 将被设置为序列中项的总数。 最后一次循环执行中，这个变量将被置1。
- forloop.revcounter0 类似于 forloop.revcounter ，但它以0做为结束索引。 在第一次执行循环时，该变量会被置为序列的项的个数减1。
- forloop.first 是一个布尔值，如果该迭代是第一次执行，那么它被置为True。
- forloop.last 是一个布尔值；在最后一次执行循环时被置为True。
- forloop.parentloop 是一个指向当前循环的上一级循环的 forloop 对象的引用（在嵌套循环的情况下）。
  

#####　注释

* 单行注释`{# 注释 #}`
* 多行注释`{% comment %}` 注释 `{% endcomment %}`


##### 过滤器

模板过滤器是在变量被显示前修改它的值的一个简单方法，过滤器使用管道字符`{{ var|first|lower }}`，可串联。
过滤器的参数形式`{{ var|filter:"para" }}`
常用过滤器：

* addslashes : 添加反斜杠到任何反斜杠、单引号或者双引号前面。 这在处理包含JavaScript的文本时是非常有用的
* date : 按指定的格式字符串参数格式化 date 或者 datetime 对象`{{ pub_date|date:"F j, Y" }}`
* length : 返回变量的长度。返回列表元素的个数、返回字符串中字符的个数


##### 在视图中使用模板

1. 配置`setting.py`中的`TEMPLATE_DIRS`，进行设置
2. 必须用绝对路径，在`settings.py`中`import os.path`，用`os.path.join(os.path.dirname(__file__)).replace('\\', '/'),`达到相对路径的作用
3. 在视图中用`django.template.loader.get_template('xx.tpl')`(可用*子目录*)获得Template对象，传入Context对象进行`render(ctx)`
4. 可在视图中使用`django.shortcuts.render_to_response(path, dict)`(模板的加载与get_template()方法一样)进行更简洁的模板render
5. 在视图中用Python的内置函数`locals()`作为Context字典传入所有局部变量（包括`request`），注意局部变量名须与模板变量名一致

    **模板文件对扩展名不敏感**


##### 模板包含：include标签

允许在一个模板文件中包含其他模板，同样是在`TEMPLATE_DIRS`中进行搜索加载，被包含模板若与主模板有同名变量，该变量将在被包含模板中可用。

- `{% include 'other.tpl'%}` `{% include "other.tpl" %}`
- `{% include 'sub_dir/other.tpl' %}`
- `{% include template_path_var %}`

##### 模板继承：extends标签

模板继承用于先定义一个页面的基本框架（父模板，用`{% block name %} ... {% endblock %}`指定），而后由子模板对父模板的对应block进行重载。

- 父模板block中原有的内容是默认的，因为子模板可能不重载某些block
- 子模板与父模板不能有相同的`block id`
- 模板继承不影响Context对象，既继承树上任何模板都能访问该Context传入的模板变量
- 子模板的第一行必须是`{% extends ... %}`，此处模板路径可以是变量，其加载与`get_template()`方法一致

模板继承示例：

base.html

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
    <html lang="en">
    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        <h1>My helpful timestamp site</h1>
        {% block content %}{% endblock %}
        {% block footer %}
        <hr>
        <p>Thanks for visiting my site.</p>
        {% endblock %}
    </body>
    </html>

sub_block_1.html

    {% extends "base.html" %}

    {% block title %}The current time{% endblock %}

    {% block content %}
    <p>It is now {{ current_date }}.</p>
    {% endblock %}

sub_block_2.html

    {% extends "base.html" %}

    {% block title %}Future time{% endblock %}

    {% block content %}
    <p>In {{ hour_offset }} hour(s), it will be {{ next_time }}.</p>
    {% endblock %}

