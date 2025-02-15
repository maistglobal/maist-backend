from rest_framework.response import Response
from rest_framework import status, generics
from .models import TechProvider, TechSeeker
from .serializers import TechProviderSerializer, TechSeekerSerializer

class TechProviderRegisterView(generics.CreateAPIView):
    queryset = TechProvider.objects.all()
    serializer_class = TechProviderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Tech Provider registration completed successfully!"}, status=status.HTTP_201_CREATED)

class TechSeekerRegisterView(generics.CreateAPIView):
    queryset = TechSeeker.objects.all()
    serializer_class = TechSeekerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Tech Seeker registration completed successfully!"}, status=status.HTTP_201_CREATED)