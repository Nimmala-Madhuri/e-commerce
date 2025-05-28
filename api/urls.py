from django.urls import path 
from .views import CartListCreateView, CartItemUpdateDeleteView, CartClearView, CartTotalView

urlpatterns = [ 
    path('cart/', CartListCreateView.as_view(), name='cart-list-create'), 
    path('cart/<int:item_id>/', CartItemUpdateDeleteView.as_view(), name='cart-item-update-delete'), 
    path('cart/clear/', CartClearView.as_view(), name='cart-clear'), 
    path('cart/total/', CartTotalView.as_view(), name='cart-total'),
    ]
