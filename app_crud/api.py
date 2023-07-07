from .models import Post,WineKinds
from rest_framework import viewsets,permissions
from .serializers import PostSerializer,WineKindsSerializer

class App_crudViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    
class WineKindsViewSet(viewsets.ModelViewSet):
    queryset = WineKinds.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = WineKindsSerializer