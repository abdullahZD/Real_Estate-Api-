from rest_framework import status, generics, filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Bulding
from .serializers import (
    ContactUsSerializer,
    RequestBuldingSerializer,
    BuldingSerializer,
)


class ContactUsView(APIView):
    def post(self,request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)


class RequestBuldingView(APIView):
    def post(self,request):
        serializer = RequestBuldingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"status": "success"}, status=status.HTTP_201_CREATED)


class BuldingViewset(viewsets.ViewSet):
    queryset = Bulding.objects.all()
    serializer_class = BuldingSerializer
    permission_classes = (IsAuthenticated,)
    
    def create(self,request,*args,**kwargs):
        data = dict(request.data, user=request.user.id)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"status": "success"}, status=status.HTTP_201_CREATED, headers=headers
        )


class GetAllEstatesView(generics.ListAPIView):
    queryset = Bulding.objects.all()
    serializer_class = BuldingSerializer
    permission_classes = (IsAuthenticated,)



    
class GetEstateView(APIView):
    def get(self, request, pk):
        estate = Bulding.objects.get(pk=pk)
        serializer = BuldingSerializer(estate)
        return Response(serializer.data, status=status.HTTP_200_OK)