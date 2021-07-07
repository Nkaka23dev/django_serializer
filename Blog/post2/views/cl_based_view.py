from rest_framework.views import APIView 
from rest_framework.response import Response 
from post2.models import Blog  
from post2.serializers import BlogSerializer

class BlogView2(APIView):
    def get(self,request):
        blog=Blog.objects.all() 
        sr=BlogSerializer(blog,many=True)
        data=sr.data
        return Response({
            'success':True,
            'message':'Data successfuly received',
            'data':data
        }) 
    def post(self,request):
        if request.data.get('title')!='':
            sr=BlogSerializer(data=request.data)
            if sr.is_valid():
                sr.save()
                return Response({
                    'success':True,
                    'message':'Data successfuly posted',
                    'data':sr.data
                })
            else:
                return Response({ 
                    'errors':sr.errors,
                    'success':False,
                    'message':'Data not posted',
                })
        return Response({
                    'success':False,
                    'message':'Data not submitted',
                    'data':sr.data
                }) 
    def put(self,request):
        if request.data.get('id') is not None:
            b1=Blog.objects.get(id=request.data.get('id'))
            sr=BlogSerializer(b1,data=request.data)
            if sr.is_valid():
                sr.save()
                return Response({
                    'success':True,
                    'message':'Updated successfully',
                    'data':sr.data
                }) 
            else:
                return Response({ 
                    'errors':sr.errors,
                    'success':False,
                    'message':'Data not posted',
                })

        return Response({
                    'success':False,
                    'message':'Not updated',
                    'data':sr.data
                })  
    def delete(self,request):
        if request.data.get('id') is not None:
            b1=Blog.objects.get(id=request.data.get('id'))
            if b1:
                b1.delete()
                return Response({
                    'success':True,
                    'message':'Delete successfully',
                    'data':''
                }) 
        return Response({
                    'success':True,
                    'message':'Delete failed',
                    'data':''
                })