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



import hashlib
import hmac
import json
import urllib
import urllib.parse
import urllib.request
import random
#import requests
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
#from django.utils.http import urlquote
from .models import Order
from app.models import PaymentForm
from app.vnpay import vnpay


def index(request):
    return render(request, 'payment/index.html', {"title": "Danh sách demo"})


def hmacsha512(key, data):
    byteKey = key.encode('utf-8')
    byteData = data.encode('utf-8')
    return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()


def payment(request):
    if request.user.is_authenticated:
        # Lấy thông tin đơn hàng từ người dùng đăng nhập
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        get_cart_total_usd = order.get_cart_total
        exchange_rate = 24000
        get_cart_total_vnd = get_cart_total_usd * exchange_rate
        order_id = order.id
        user_not_login = "hidden"
        user_login = "show"

        # Chuẩn bị thông tin cho thanh toán
        bank_code = request.POST.get('bank_code', '')  # Lấy mã ngân hàng từ form (nếu có)
        language = request.POST.get('language', 'vn')  # Mặc định là tiếng Việt
        ipaddr = get_client_ip(request)
        order_desc = f"Thanh toán đơn hàng #{order_id} lúc {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        # Xử lý VNPAY nếu phương thức POST được gọi
        if request.method == 'POST':
            # Build URL Payment
            vnp = vnpay()
            vnp.requestData['vnp_Version'] = '2.1.0'
            vnp.requestData['vnp_Command'] = 'pay'
            vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
            vnp.requestData['vnp_Amount'] = int(get_cart_total_vnd * 100)  # Chuyển sang đơn vị phù hợp (VNPAY yêu cầu)
            vnp.requestData['vnp_CurrCode'] = 'VND'
            vnp.requestData['vnp_TxnRef'] = order_id
            vnp.requestData['vnp_OrderInfo'] = order_desc
            vnp.requestData['vnp_OrderType'] = 'billpayment'
            vnp.requestData['vnp_Locale'] = language
            vnp.requestData['vnp_CreateDate'] = datetime.now().strftime('%Y%m%d%H%M%S')
            vnp.requestData['vnp_IpAddr'] = ipaddr
            vnp.requestData['vnp_ReturnUrl'] = settings.VNPAY_RETURN_URL

            # Thêm mã ngân hàng nếu có
            if bank_code:
                vnp.requestData['vnp_BankCode'] = bank_code

            # Tạo URL thanh toán và chuyển hướng
            vnpay_payment_url = vnp.get_payment_url(settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)
            return redirect(vnpay_payment_url)
    else:
        # Trường hợp người dùng chưa đăng nhập
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        get_cart_total_vnd = 0
        order_id = None
        user_not_login = "show"
        user_login = "hidden"

    # Truyền thông tin vào template
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'get_cart_total_vnd': get_cart_total_vnd,
        'order_id': order_id,
        'user_not_login': user_not_login,
        'user_login': user_login
    }
    return render(request, 'payment/payment.html', context)




def payment_ipn(request):
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        order_id = inputData['vnp_TxnRef']
        amount = inputData['vnp_Amount']
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']
        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            # Check & Update Order Status in your Database
            # Your code here
            firstTimeUpdate = True
            totalamount = True
            if totalamount:
                if firstTimeUpdate:
                    if vnp_ResponseCode == '00':
                        print('Payment Success. Your code implement here')
                    else:
                        print('Payment Error. Your code implement here')

                    # Return VNPAY: Merchant update success
                    result = JsonResponse({'RspCode': '00', 'Message': 'Confirm Success'})
                else:
                    # Already Update
                    result = JsonResponse({'RspCode': '02', 'Message': 'Order Already Update'})
            else:
                # invalid amount
                result = JsonResponse({'RspCode': '04', 'Message': 'invalid amount'})
        else:
            # Invalid Signature
            result = JsonResponse({'RspCode': '97', 'Message': 'Invalid Signature'})
    else:
        result = JsonResponse({'RspCode': '99', 'Message': 'Invalid request'})

    return result


def payment_return(request):
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        order_id = inputData['vnp_TxnRef']
        amount = int(inputData['vnp_Amount']) / 100
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']

        payment = Payment_VNPay.objects.create(
            order_id = order_id,
            amount = amount,
            order_desc = order_desc,
            vnp_TransactionNo = vnp_TransactionNo,
            vnp_ResponseCode = vnp_ResponseCode
        )

        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            if vnp_ResponseCode == "00":
                return render(request, 'payment/payment_return.html', {"title": "Kết quả thanh toán",
                                                               "result": "Thành công", "order_id": order_id,
                                                               "amount": amount,
                                                               "order_desc": order_desc,
                                                               "vnp_TransactionNo": vnp_TransactionNo,
                                                               "vnp_ResponseCode": vnp_ResponseCode})
            else:
                return render(request, 'payment/payment_return.html', {"title": "Kết quả thanh toán",
                                                               "result": "Lỗi", "order_id": order_id,
                                                               "amount": amount,
                                                               "order_desc": order_desc,
                                                               "vnp_TransactionNo": vnp_TransactionNo,
                                                               "vnp_ResponseCode": vnp_ResponseCode})
        else:
            return render(request, 'payment/payment_return.html',
                          {"title": "Kết quả thanh toán", "result": "Lỗi", "order_id": order_id, "amount": amount,
                           "order_desc": order_desc, "vnp_TransactionNo": vnp_TransactionNo,
                           "vnp_ResponseCode": vnp_ResponseCode, "msg": "Sai checksum"})
    else:
        return render(request, 'payment/payment_return.html', {"title": "Kết quả thanh toán", "result": ""})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

n = random.randint(10**11, 10**12 - 1)
n_str = str(n)
while len(n_str) < 12:
    n_str = '0' + n_str


def query(request):
    if request.method == 'GET':
        return render(request, 'payment/query.html', {"title": "Kiểm tra kết quả giao dịch"})

    url = settings.VNPAY_API_URL
    secret_key = settings.VNPAY_HASH_SECRET_KEY
    vnp_TmnCode = settings.VNPAY_TMN_CODE
    vnp_Version = '2.1.0'

    vnp_RequestId = n_str
    vnp_Command = 'querydr'
    vnp_TxnRef = request.POST['order_id']
    vnp_OrderInfo = 'kiem tra gd'
    vnp_TransactionDate = request.POST['trans_date']
    vnp_CreateDate = datetime.now().strftime('%Y%m%d%H%M%S')
    vnp_IpAddr = get_client_ip(request)

    hash_data = "|".join([
        vnp_RequestId, vnp_Version, vnp_Command, vnp_TmnCode,
        vnp_TxnRef, vnp_TransactionDate, vnp_CreateDate,
        vnp_IpAddr, vnp_OrderInfo
    ])

    secure_hash = hmac.new(secret_key.encode(), hash_data.encode(), hashlib.sha512).hexdigest()

    data = {
        "vnp_RequestId": vnp_RequestId,
        "vnp_TmnCode": vnp_TmnCode,
        "vnp_Command": vnp_Command,
        "vnp_TxnRef": vnp_TxnRef,
        "vnp_OrderInfo": vnp_OrderInfo,
        "vnp_TransactionDate": vnp_TransactionDate,
        "vnp_CreateDate": vnp_CreateDate,
        "vnp_IpAddr": vnp_IpAddr,
        "vnp_Version": vnp_Version,
        "vnp_SecureHash": secure_hash
    }

    headers = {"Content-Type": "application/json"}

    response = request.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = json.loads(response.text)
    else:
        response_json = {"error": f"Request failed with status code: {response.status_code}"}

    return render(request, 'payment/query.html', {"title": "Kiểm tra kết quả giao dịch", "response_json": response_json})

def refund(request):
    if request.method == 'GET':
        return render(request, 'payment/refund.html', {"title": "Hoàn tiền giao dịch"})

    url = settings.VNPAY_API_URL
    secret_key = settings.VNPAY_HASH_SECRET_KEY
    vnp_TmnCode = settings.VNPAY_TMN_CODE
    vnp_RequestId = n_str
    vnp_Version = '2.1.0'
    vnp_Command = 'refund'
    vnp_TransactionType = request.POST['TransactionType']
    vnp_TxnRef = request.POST['order_id']
    vnp_Amount = request.POST['amount']
    vnp_OrderInfo = request.POST['order_desc']
    vnp_TransactionNo = '0'
    vnp_TransactionDate = request.POST['trans_date']
    vnp_CreateDate = datetime.now().strftime('%Y%m%d%H%M%S')
    vnp_CreateBy = 'user01'
    vnp_IpAddr = get_client_ip(request)

    hash_data = "|".join([
        vnp_RequestId, vnp_Version, vnp_Command, vnp_TmnCode, vnp_TransactionType, vnp_TxnRef,
        vnp_Amount, vnp_TransactionNo, vnp_TransactionDate, vnp_CreateBy, vnp_CreateDate,
        vnp_IpAddr, vnp_OrderInfo
    ])

    secure_hash = hmac.new(secret_key.encode(), hash_data.encode(), hashlib.sha512).hexdigest()

    data = {
        "vnp_RequestId": vnp_RequestId,
        "vnp_TmnCode": vnp_TmnCode,
        "vnp_Command": vnp_Command,
        "vnp_TxnRef": vnp_TxnRef,
        "vnp_Amount": vnp_Amount,
        "vnp_OrderInfo": vnp_OrderInfo,
        "vnp_TransactionDate": vnp_TransactionDate,
        "vnp_CreateDate": vnp_CreateDate,
        "vnp_IpAddr": vnp_IpAddr,
        "vnp_TransactionType": vnp_TransactionType,
        "vnp_TransactionNo": vnp_TransactionNo,
        "vnp_CreateBy": vnp_CreateBy,
        "vnp_Version": vnp_Version,
        "vnp_SecureHash": secure_hash
    }

    headers = {"Content-Type": "application/json"}

    response = request.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = json.loads(response.text)
    else:
        response_json = {"error": f"Request failed with status code: {response.status_code}"}

    return render(request, 'payment/refund.html', {"title": "Kết quả hoàn tiền giao dịch", "response_json": response_json})