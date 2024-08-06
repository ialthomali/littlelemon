from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from . import models
from . import serializers

# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    #permission_classes = [permissions.IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    #permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

# class BookingView(APIView):
#     def get(self, request):
#         bookings = models.Booking.objects.all()
#         serializedBookings = serializers.BookingSerializer(bookings,many=True)
#         return Response(serializedBookings.data)
#     def post(self, request):
#         serializeredBookings = serializers.BookingSerializer(data=request.data)
#         if serializeredBookings.is_valid():
#             serializeredBookings.save()
#             return Response({"message":"success",
#                              "data":serializeredBookings.data})

