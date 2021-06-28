from rest_framework.response import Response
from rest_framework.views import APIView 
from posts2.models import BlogModel2 
from posts2.serializers import BlogModel2serializer


class BlogAPIView(APIView): 
    def get(self,request):
        b1=BlogModel2.objects.all()
        sr=BlogModel2serializer(b1,many=True)
        data=sr.data
        return Response({
            'success':True,
            'message':'Get in class basedview',
            'data':data
        }) 
    def post(self,request,*args,**kwargs):
        if request.data.get('title')!='':
            serializer=BlogModel2serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success':True,
                    'message':'Post class successfully in class based view.',
                    'data':''
                }) 

