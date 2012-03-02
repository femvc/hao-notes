#### Django Admin
----

###### 激活Admin

1. 在settings.py中去掉`INSTALLED_APPS`中以下3项的注释：
	- django.contrib.admin
	- django.contrib.contenttypes
	- django.contrib.sessions
2. 同时去掉`MIDDLEWARE_CLASSES`中以下3项的注释：
	- django.middleware.common.CommonMiddleware
	- django.contrib.sessions.middleware.SessionMiddleware
	- django.contrib.auth.middleware.AuthenticationMiddleware
3. 运行`python manage.py syncdb`生成Admin所使用的数据库表
4. 根据需要在syncdb命令或`python manage.py createsuperuser`(INSTALLED_APPS中包含django.contrib.auth时才可用)创建超级用户，否则登录不了Admin
5. 在urls.py中打开对admin的路由：`(r'^admin/', include(admin.site.urls)),`，同时去掉`admin.autodiscover()`的注释，这使得Django的Admin自动发现各个app下`admin.py`所注册的Model子类
6. 运行`python manage.py runserver`启动Django服务器，访问localhost

        $ python manage.py syncdb
        Creating table auth_permission
        Creating table auth_group_permissions
        Creating table auth_group
        Creating table auth_user_user_permissions
        Creating table auth_user_groups
        Creating table auth_user
        Creating table auth_message
        Creating table django_content_type
        Creating table django_session
        Creating table django_site

        You just installed Django's auth system, which means you don't have any superusers defined.
        Would you like to create one now? (yes/no): no
        Installing index for auth.Permission model
        Installing index for auth.Group_permissions model
        Installing index for auth.User_user_permissions model
        Installing index for auth.User_groups model
        Installing index for auth.Message model
        No fixtures found.

###### 使用Admin

使用超级用户帐号密码登录Admin首页

**本地化**

在settings.py的MIDDLEWARE_CLASSES中添加一行`'django.middleware.locale.LocaleMiddleware',`(必须在`'django.contrib.sessions.middleware.SessionMiddleware'`*之后*，刷新Admin将变成本地语言。

**将app Model添加到Admin**

在`mysite.app_name`目录下添加`admin.py`文件，将需要的Model子类注册到admin中，然后刷新或重启服务器：

    from django.contrib import admin
    from mysite.books.models import Publisher, Author, Book

    admin.site.register(Publisher)
    admin.site.register(Author)
    admin.site.register(Book)

> **Adminr如何工作？**  

> - 当服务启动时，Django从`` url.py`` 引导URLconf，然后执行`` admin.autodiscover()`` 语句。 这个函数遍历INSTALLED_APPS配置，并且寻找相关的 admin.py文件。 如果在指定的app目录下找到admin.py，它就执行其中的代码。  

> - 在`myapp`目录下的`admin.py`文件中，每次调用`admin.site.register()`都将那个Model子类注册到Admin中。Admin只为那些明确注册了的Model显示一个编辑/修改的界面。而`django.contrib.auth`包含自身的`admin.py`，所以Users和Groups能在管理工具中自动显示。  

> - 综上所述，Admin其实就是一个Django app，包含自己的Model、Template、View和URLpatterns。 要像添加自己的视图一样，把它添加到URLconf里面。可以在Django基本代码中的`django/contrib/admin`目录下，检查它的模板、视图和URLpatterns，但不要尝试直接修改其中的任何代码，因为里面有很多地方可以让用户自定义管理工具的工作方式。（如果你确实想浏览Django管理工具的代码，请谨记它在读取关于模块的**元数据**过程中做了些不简单的工作，因此最好花些时间阅读和理解那些代码。）

**Admin页面操作相关设置**

- Model子类中定义字符串字段可为空字符串`''`，例如`email = models.EmailField(**blank=True**)`，如此在页面中显示为**非粗体**
- 对于非字符串字段，必须同时指定`**blank=True, null=True**`，表明该字段可为空`NULL`
- 字段的自定义字段标签（即页面显示）由`**verbose_name='other_name'**`属性指定
- **自定义ModelAdmin类**

**自定义ModelAdmin类**

在`admin.py`中可为指定的Model子类添加对应的`AdminModel`类，增强或改变其在Admin中的操作、显示效果。

    # coding=utf8
    from django.contrib import admin
    from testsite.books.models import Publisher, Author, Book

    class AuthorAdmin(admin.ModelAdmin):
        list_display = ('first_name', 'last_name', 'email')
        search_fields = ('first_name', 'last_name') # 增加搜索框

    class BookAdmin(admin.ModelAdmin): # 继承自adminModelAdmin类
        list_display = ('title', 'publisher', 'publication_date') # 显示顺序
        list_filter = ('publication_date',) # 右边栏增加常用过滤方式
        search_fields = ('title', 'publisher') # 增加搜索框
        date_hierarchy = 'publication_date' # 列表顶端增减日期筛选
        ordering = ('-publication_date',) # 列表排序
        fields = ('title', 'authors', 'publisher', 'publication_date') # 字段显示顺序及隐藏
        #fields = ('title', 'authors', 'publisher',) # 隐藏publication_date字段
        #filter_horizontal = ('authors', ) # 横向选择框
        filter_vertical = ('authors',) # 纵向选择框
        raw_id_fields = ('publisher',) # 多对多关系的选择框

    admin.site.register(Publisher)
    #admin.site.register(Author)
    admin.site.register(Author, AuthorAdmin) # 以AuthorAdmin类为选项重新注册
    #admin.site.register(Book)
    admin.site.register(Book, BookAdmin) # 以BookAdmin类为选项重新注册

**用户、用户组和权限**

Admin默认的权限都是定义在**Model级别上**（Model子类）的，**对象上**（Model子类的对象）的权限需要查看Django的文档。




