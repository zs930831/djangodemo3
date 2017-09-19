from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe


# Create your views here.



def tlp(request):
    return render(request, "tlp.html")


list = []
for i in range(102):
    list.append(i)


def us(request):
    current_page = request.GET.get("p", 1)
    current_page = int(current_page)
    s = (current_page - 1) * 10
    e = (current_page) * 10
    data = list[s:e]
    listlen = len(list)
    l, v = divmod(listlen, 10)
    if v:
        l += 1
    page_str = []
    for i in range(1, l + 1):
        if i == current_page:
            page_str1 = '<a class="page active" href="/us/?p=%s">%s</a>' % (i, i)
        else:
            page_str1 = '<a class="page" href="/us/?p=%s">%s</a>' % (i, i)
        page_str.append(page_str1)
    page_str = mark_safe("".join(page_str))
    return render(request, "li.html", {"list": data, "page_str": page_str})


data = {
    "zs": "111",
    "zs1": "222"
}


# FBV dec
def dec(func):
    def inner(request, *args, **kwargs):
        user = request.COOKIES.get('user1')
        if not user:
            return redirect('/login')
        return func(request, *args, **kwargs)

    return inner


# cbv dec
from django.utils.decorators import method_decorator
from django import views


@method_decorator(dec, name="dispatch")
class Order(views.View):
    # @method_decorator(dec)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(Order,self).dispatch(request,*args,**kwargs)

    # @method_decorator(dec)
    def get(self, request):
        user = request.COOKIES.get('user1')
        return render(request, "index.html", {"user": user})

    # @method_decorator(dec)
    def post(self, request):
        user = request.COOKIES.get('user1')
        return render(request, "index.html", {"user": user})


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("pwd")
        pwd = data.get(u, None)
        # print(p,pwd)
        if pwd and pwd == p:
            # 不能用render
            obj = redirect('/index')
            # obj=render(request,"index.html")
            obj.set_cookie("user1", u)
            return obj
        else:
            return redirect("/login")


@dec
def index(request):
    user = request.COOKIES.get('user1')
    return render(request, "index.html", {"user": user})
