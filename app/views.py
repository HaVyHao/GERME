from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def founder(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}    
        cartItems = order['get_cart_items'] 
        user_not_login = "show"
        user_login = "hidden"  
    #categories = Category.objects.filter(is_sub =False)
    sub_categories = Category.objects.filter(is_sub =True)
    context = {'sub_categories':sub_categories,'items': items,'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login} 
    return render(request,'app/founder.html',context)
def payqr(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}    
        cartItems = order['get_cart_items'] 
        user_not_login = "show"
        user_login = "hidden"  
    #categories = Category.objects.filter(is_sub =False)
    sub_categories = Category.objects.filter(is_sub =True)
    context = {'sub_categories':sub_categories,'items': items,'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login} 
    return render(request,'app/payqr.html',context)
def pay(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}    
        cartItems = order['get_cart_items'] 
        user_not_login = "show"
        user_login = "hidden"  
    #categories = Category.objects.filter(is_sub =False)
    sub_categories = Category.objects.filter(is_sub =True)
    context = {'sub_categories':sub_categories,'items': items,'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login} 
    return render(request,'app/pay.html',context)
def introduce(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}    
        cartItems = order['get_cart_items'] 
        user_not_login = "show"
        user_login = "hidden"  
    #categories = Category.objects.filter(is_sub =False)
    sub_categories = Category.objects.filter(is_sub =True)
    context = {'sub_categories':sub_categories,'items': items,'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login} 
    return render(request,'app/introduce.html',context)
def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}    
        cartItems = order['get_cart_items'] 
        user_not_login = "show"
        user_login = "hidden"  
    id = request.GET.get('id', '')
    products = Product.objects.filter(id=id)
    #categories = Category.objects.filter(is_sub =False)
    sub_categories = Category.objects.filter(is_sub =True)
    context = {'products':products,'sub_categories':sub_categories,'items': items,'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login} 
    return render(request,'app/detail.html',context)
def category(request):
    sub_categories = Category.objects.filter(is_sub =True)
    active_category = request.GET.get('category','')
    if active_category:
        products = Product.objects.filter(category__slug = active_category)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0} 
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    context = {'sub_categories':sub_categories,'items': items,'products':products,'active_category':active_category,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/category.html',context)
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0} 
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    #categories = Category.objects.filter(is_sub =False)
    sub_categories = Category.objects.filter(is_sub =True)
    products = Product.objects.all()
    return render(request,'app/search.html',{'sub_categories':sub_categories,"searched": searched,'items': items, "keys": keys,'products': products,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login})
def register(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Chưa lưu vào cơ sở dữ liệu
            password = form.cleaned_data.get('password1')
            user.set_password(password)  # Mã hóa mật khẩu
            user.save()
            return redirect('login')
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0} 
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    #categories = Category.objects.filter(is_sub =False)
    sub_categories = Category.objects.filter(is_sub =True)
    context = {'sub_categories':sub_categories,'form':form,'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/register.html',context)
def loginPage(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
        return redirect('home')
    if request.method == "POST":
        user_not_login = "hidden"
        user_login = "show"
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)           
            return redirect('home')
        else: messages.info(request,'Tên Hoặc Mật Khẩu Đăng Nhập Không Đúng!')
    else:
        user_not_login = "show"
        user_login = "hidden"
    #categories = Category.objects.filter(is_sub =False)
    sub_categories = Category.objects.filter(is_sub =True)
    context = {'sub_categories':sub_categories,'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('login')
def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0} 
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    sub_categories = Category.objects.filter(is_sub =True)
    #categories = Category.objects.filter(is_sub =False)
    products = Product.objects.all()
    context = {'sub_categories':sub_categories, 'products': products,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login,'items': items }
    return render(request,'app/home.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}    
        cartItems = order['get_cart_items'] 
        user_not_login = "show"
        user_login = "hidden"  
    #categories = Category.objects.filter(is_sub =False)
    sub_categories = Category.objects.filter(is_sub =True)
    context = {'sub_categories':sub_categories,'items': items,'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login} 
    return render(request,'app/cart.html',context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    #categories = Category.objects.filter(is_sub =False)
    sub_categories = Category.objects.filter(is_sub =True)
    context = {'sub_categories':sub_categories,'items': items,'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/checkout.html',context)
def updateitems(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer,complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product = product) 
    if action == 'add':
        orderItem.quantity +=1
    elif action == 'remove':
        orderItem.quantity -=1
    elif action == 'clear':
        orderItem.quantity =0
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('added',safe=False)

