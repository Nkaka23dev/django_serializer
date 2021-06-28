from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from posts2.models import BlogModel2 
from posts2.serializers import BlogModel2serializer

@api_view(['GET','POST'])
def blog_view(request):
    if request.method=='GET': 
        model=BlogModel2.objects.all() 
        data=BlogModel2serializer(model,many=True).data
        return Response({
            'success':True,
            'message':'GET method passed successfuly',
            'data':data
        })  
    if request.method=='POST':
        if request.data.get('title')!='':
            serializer=BlogModel2serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success':True,
                    'message':'POST method successfully passed.',
                    'data':''
                }) 
    return Response({
        'success':False,
        'message':'Failed',
        'data':''
        })

