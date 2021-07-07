from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from post2.models import Blog 
from post2.serializers import BlogSerializer

@api_view(['GET','POST'])
def BlogView(request):
    if request.method=='GET':
        b1=Blog.objects.all()
        sr=BlogSerializer(b1,many=True)
        data=sr.data
        return Response({
            'success':True,
            'message':'Data retrived successful',
            'data':data
        }) 
    if request.method=='POST':
        if request.data.get('title')!='':
            serializer=BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success':True,
                    'message':'Data posted success',
                    'data':serializer.data
                }) 
            else:
                return Response({
                    'error':serializer.errors
                }) 
        else:
            return Response({
                'success':False,
                'message':'Data not posted',
                'data':serializer.data
                }) 