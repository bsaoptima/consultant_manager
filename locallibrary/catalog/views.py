from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User


class RegisterView(APIView):
    def post(self,request):
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response({
                'msg' : 'success'
            })
        return Response({
            'msg' : 'fail'
        })
    



class TestView(APIView):
    def post(self,request):
        user_id = request.data['user_id']
        user = User.objects.get(pk=user_id)
        s = UserSerializer(user)
        users = User.objects.all()
        s2 = UserSerializer(users,many=True)
        return Response({
            "user" : s.data,
            "all_users" :s2.data
        
        })
    
   
   
  



# Create your views here.
