### AJAX[¶](https://docs.djangoproject.com/en/4.0/ref/csrf/#ajax)

While the above method can be used for AJAX POST requests, it has some inconveniences: you have to remember to pass the CSRF token in as POST data with every POST request. For this reason, there is an alternative method: on each XMLHttpRequest, set a custom `X-CSRFToken` header (as specified by the [`CSRF_HEADER_NAME`](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-CSRF_HEADER_NAME) setting) to the value of the CSRF token. This is often easier because many JavaScript frameworks provide hooks that allow headers to be set on every request.

First, you must get the CSRF token. How to do that depends on whether or not the [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-CSRF_USE_SESSIONS) and [`CSRF_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-CSRF_COOKIE_HTTPONLY) settings are enabled

[vue.js与django-rest-framework进行数据的交互及Ajax和axios异步请求django后端API接口_专职的博客-CSDN博客](https://mayanan.blog.csdn.net/article/details/111991034)

这篇文章给出了 ajax 和 axios 的使用示例，本质都是通过访问 url 来进行 `GET` 和 `POST` 操作。同时这篇文章说 ajax 不会用 csrf 问题 

[Django与Ajax交互 | 大江狗的博客 (pythondjango.cn)](https://pythondjango.cn/django/basics/16-django-ajax/)

本文介绍了 django 与 ajax 的交互方式，如何通过 csrftoken 认证，并提供了两个具体示例。

[Django ajax 局部加载、异步刷新_ィふ ぬ！旧时光的博客-CSDN博客](https://blog.csdn.net/Tqq_sunshine/article/details/89501817)

这篇文章看起来是要把前端的 js 嵌在我们的模板文件中，应该没有用到前后端分离。

[Django中ajax的基本用法_Iron_Huang的博客-CSDN博客](https://blog.csdn.net/weixin_45566022/article/details/103939604?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-103939604-blog-119434877.pc_relevant_multi_platform_whitelistv2&spm=1001.2101.3001.4242.1&utm_relevant_index=2)

给出了 ajax 基本语法结构，便于后端同学理解 ajax 的用法，有参考意义。

但是这一篇文章并不是基于 restful 风格的，还是采用前后端不分离的方式进行操作。

[Django使用AJAX调用自己写的API接口__miccretti的博客-CSDN博客](https://blog.csdn.net/weixin_33798152/article/details/93283454)

drf 中用 ajax 加载页面 （没有用vue，用的 django 自己的模板写法），有比较完整的 github 项目参考

[ajax 解决csrf的3种方法，input标签的文件上传 - 谷子的 - 博客园 (cnblogs.com)](https://www.cnblogs.com/gyh04541/p/8016505.html) 这里给出了两种前端解决方案和一种后端解决方案。

总的来说，ajax 和 axios 都是通过 url 进行 get 和 post 操作。大体上是差不多的。
