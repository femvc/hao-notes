#### 表单
----

###### HttpRequest对象

View函数中的参数request包含以下方法和属性：

- request.path 除域名以外的请求路径，以正斜杠开头 "/hello/"
- request.get_host() 主机名（比如，通常所说的域名） "127.0.0.1:8000" or "www.example.com"
- request.get_full_path() 请求路径，可能包含查询字符串 "/hello/?print=true
- request.is_secure() 如果通过HTTPS访问，则此方法返回True，否则返回False True 或者 False

**request.META**

`request.META`是一个Python字典，包含了所有本次HTTP请求的Header信息。应该用`get(key)`方法来试图获取对应的value，不建议用索引方式来获取，后者遇到不存在的Key会引发KeyError异常（此种方式可用`try/except`块来处理）。

**request.GET** & **request.POST**

类似Python的字典对象，同样具有get()、keys()和values()方法，但还包含其他特定的方法。

> 应该每次都给成功的POST请求做重定向（`django.http.HttpResponseRedirect(url)`），这是web开发的最佳实践。
> 原因是：若用户刷新一个包含POST表单的页面，那么请求将会重新发送造成重复。

###### django.forms

Django带有一个form库，称为django.forms，这个库可以提供HTML表单显示以及验证的功能。

> 当Django首次向公众发布时，它有一个复杂难懂的表单系统：django.forms。后来它被完全重写了，新的版本改叫作：django.newforms，这样人们还可以通过名称，使用旧版本。当Django 1.0发布时，旧版本django.forms就不再使用了，而django.newforms也终于可以名正言顺的叫做：django.forms。

forms库最主要的用法是，为每一个将要处理的HTML的`<Form>`定义一个forms子类，Django社区习惯创建django.forms子类`forms.py`，存放到与`views.py` 相同的目录中。

    from django import forms

    class ContactForm(forms.Form):
        subject = forms.CharField()
        email = forms.EmailField(required=False)
        message = forms.CharField()

    from books.forms import ContactForm
    f = ContactForm()
    print f
    <tr><th><label for="id_subject">Subject:</label></th><td><input type="text" name="subject" id="id_subject" /></td></tr>
    <tr><th><label for="id_email">Email:</label></th><td><input type="text" name="email" id="id_email" /></td></tr>
    <tr><th><label for="id_message">Message:</label></th><td><input type="text" name="message" id="id_message" /></td></tr>

    print f.as_ul()
    <li><label for="id_subject">Subject:</label> <input type="text" name="subject" id="id_subject" /></li>
    <li><label for="id_email">Email:</label> <input type="text" name="email" id="id_email" /></li>
    <li><label for="id_message">Message:</label> <input type="text" name="message" id="id_message" /></li>

    print f.as_p()
    <p><label for="id_subject">Subject:</label> <input type="text" name="subject" value="Hello" id="id_subject" /></p>
    <p><label for="id_email">Email:</label> <input type="text" name="email" value="adrian@example.com" id="id_email" /></p>
    <p><label for="id_message">Message:</label> <input type="text" name="message" value="Nice site!" id="id_message" /></p>


    print f['subject']
    <input type="text" name="subject" id="id_subject" />

    f = ContactForm({'subject': 'Hello', 'email': 'adrian@example.com', 'message': 'Nice site!'})
    f.is_bound
    True
    f.is_valid()
    True
    f = ContactForm({'subject': 'Hello', 'message': 'Nice site!'})
    f.is_valid()
    True
    f  = ContactForm({'subject': 'Hello'})
    f.is_valid()
    False
    f = ContactForm({'subject': 'Hello', 'email': 'adrian@example.com', 'message': 'Nice site!'})
    f.cleaned_data
    {'message': u'Nice site!', 'email': u'adrian@example.com', 'subject': u'Hello'}

    f = ContactForm({'subject': 'Hello', 'message': ''})
    f['message'].errors
    [u'This field is required.']
    f['subject'].errors
    []
    f['email'].errors
    []
    f = ContactForm({'subject': 'Hello', 'message': ''})
    f.errors
    {'message': [u'This field is required.']}

######修改forms子类的默认显示&行为###

    class ContactForm(forms.Form):
        subject = forms.CharField(max_length=100)
        email = forms.EmailField(required=False)
        message = forms.CharField(widget=forms.Textarea)

**创建forms对象时设置初始值**

    form = ContactForm(initial={'subject': 'I love your site!'})

**自定义校验规则**

    class ContactForm(forms.Form):
        subject = forms.CharField(max_length=100)
        email = forms.EmailField(required=False)
        message = forms.CharField(widget=forms.Textarea)

        # 校验规则，命名为`clean_fieldname(self)`
        # 由forms库执行于默认校验逻辑之后
        def clean_message(self):
            message = self.cleaned_data['message']
            num_words = len(message.split())
            if num_words < 4:
                raise forms.ValidationError("Not enough words!")
            return message

**指定标签**

forms表单中自动生成的标签默认是按照规则生成的：用空格代替下划线，首字母大写

    email = forms.EmailField(required=False, label='Your email address:')


