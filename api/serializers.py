from rest_framework import serializers 
from cart.models import CartItem, Product

class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product 
        fields = ['id', 'name', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True) 
    product_id = serializers.PrimaryKeyRelatedField( queryset=Product.objects.all(), source='product', write_only=True ) 
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'added_at', 'total_price']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)