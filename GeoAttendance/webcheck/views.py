from django.shortcuts import render 
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from webcheck.models import userData
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated      
# Create your views here.

def signUp_Page(request):
    return render(request,'signUp_Page.html')

def create_User(request):
    flag = None  # Initialize flag for both GET and POST methods
    
    if request.method == 'POST':
        userMail = request.POST.get('email')  # Email input
        userPass = request.POST.get('password')  # Password input
        usersname = request.POST.get('username')  # Username input

        # Check if user with the same email already exists
        from webcheck.models import userData
        if userData.objects.filter(userMail = userMail).first():
            print('User already exists')
            flag = True
        else:
            
            makeUser = userData(
                userName = usersname,
                userPass = make_password(userPass),
                userMail = userMail,
                userUid = f'{usersname}{userPass}'
            )
            makeUser.save()
            print(f'{usersname,userPass,userMail}')
            flag = False  # Set flag to False when user is successfully created

    # Render the signup page with the flag
    return render(request, 'signUp_page.html', {'userExist': flag})


def login_page(request):
    cord=gps()
    data = {'lat':f'{cord[0]}','long':f'{cord[1]}'}
    return render(request, 'login_Page.html',{'cord':data})

def userData(request):
    if request.method == 'POST':
        userMail = request.POST.get('USERNAME')  # Email input for login
        userPassword = request.POST.get('PASSWORD')  # Password input for login

        # Fetch the user from the database using the provided email
        from webcheck.models import userData
        user = userData.objects.filter(userMail=userMail).first()

        if check_password(userPassword, user.userPass) and user.userRole == 'admin':
            print('admin hai')
            admin = True
            data = {'admin':f'{True}'}
            return render(request, 'home_Page.html',{'Role':'admin'})
            # pass

        elif user and check_password(userPassword, user.userPass):  # Validate password
            return render(request, 'home_Page.html')  # If login is successful
        else:
            return render(request, 'login_Page.html', {'alerts': True})  # Show error if credentials are incorrect
        

def adminPortal(request):
    from webcheck.models import userData
    data = userData.objects.all()
    i = 0
    for no in data:
        i = i+1
    
    data = {'noU':i}
        
    return render(request,'admin_Portal.html',{'data':data})


def gps():

    import geocoder
    ip = geocoder.ip('me')
    latitude = ip.latlng[0] if ip.latlng else "Not Available"
    longitude = ip.latlng[1] if ip.latlng else "Not Available"
    print(latitude,longitude)
    return [latitude,longitude]

def finduser(request):
    if request.method == 'POST':
        usermail=request.POST.get('usermail')
    from .models import userData
    data = userData.objects.first
    
    return render(request,'admin_Portal.html',{'udata':data})



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import userData
# # from .serializers import userSerializer
# # from .serializers import LoginSerializer
# class userApi(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         queryset = userData.objects.all()
#         serializer = userSerializer(queryset,many = True)
#         return Response({
#             "statu": True,
#             "data":serializer.data
#         })
    

# class LoginAPI(APIView):
#     def post(self,request):
#         data = request.data
#         serializer = LoginSerializer(data= data)
#         if not serializer.is_valid():
        
#             return Response({
#             "status":False,
#             "data":serializer.errors
#         })
#         username = serializer.data['username']
#         password = serializer.data['password']
#         print(username,password)

#         user_obj = authenticate(username=username,password= password)
#         if user_obj:
#             token ,_ =Token.objects.get_or_create(user= user_obj)
#             print(token.token)
#             return Response({
#                 "status":True,
#                 "data":{'token':str(token)}
#             })

#         return Response({
#             "status":False,
#             "data":{},
#             "message":"invalid credentials"
#         })
    
