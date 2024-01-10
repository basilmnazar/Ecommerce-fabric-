from django.shortcuts import render,redirect

#import user model
from django.contrib.auth.models import User
from myapp.models import*
#login authenticate
from django.contrib.auth import authenticate,login as auth_login,logout

# Create your views here.
def index(request):
    product = fabric.objects.all()
    return render(request, 'index.html',{'products':product})

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def products(request):
    return render(request, 'furniture.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

# def register(request):
#     return render(request, 'signup.html')

##function for register

def for_register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        phone=request.POST['phone']
        address=request.POST['address']
        user_name= request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        print(user_name)

        #check if the  username is unique

        if User.objects.filter(username=user_name):
            print('username is already exists')

            

            return render(request,'signup.html')
        else:
            if (password != cpassword):
                print('password is not match')
                return render(request,'signup.html')
            else:
                 #create a new user
                user=User.objects.create_user(first_name=first_name,
                                          last_name=last_name,
                                          email=email,
                                          password=password,
                                          username=user_name
                                          )

                user.save()

                newuser=register_user(user=user,phone=phone,address=address)
                newuser.save()
                print("success")

                auth_login(request, user)
                return redirect('index')
           

    else:
        print('not registered')
        return render(request,'signup.html')
      

##login setup

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
#function for product page(view products)

def view_product(request):
    products=fabric.objects.all()
    return render(request,'index.html',{'products':products})
   
# def cart(request):
#     return render(request,'cart.html')

def view_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = fabric.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('viewCart')

def increament(request,id):
    cartitem = CartItem.objects.get(id = id)
    cartitem.quantity =+1
    cartitem.save()
    
    return redirect('viewCart')