from rest_framework import serializers

from women.models import Cart, CartItems, Women, WomenImage


class WomenImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomenImage
        fields = ["id", "woman", "image"]


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = WomenImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=100000, allow_empty_file=False, use_url=False
        ),
        write_only=True,
    )

    class Meta:
        model = Women
        fields = [
            "id",
            "title",
            "content",
            "images",
            "uploaded_images",
            "cat",
            "user",
        ]

    cat = serializers.StringRelatedField()

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        woman = Women.objects.create(**validated_data)
        for image in uploaded_images:
            newwoman_image = WomenImage.objects.create(woman=woman, image=image)
        return woman


class CartItemSerializer(serializers.ModelSerializer):
    product = WomenSerializer(many=False)

    class Meta:
        model = CartItems
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "items"]
