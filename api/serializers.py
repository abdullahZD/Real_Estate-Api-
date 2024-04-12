from rest_framework import serializers
from .models import Bulding, ContactUs, BuldingImage, RequestBulding


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class RequestBuldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestBulding
        fields = '__all__'


class BuldingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuldingImage
        fields = ("image",)



class BuldingSerializer(serializers.ModelSerializer):
    images = BuldingImageSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
    )

    class Meta:
        model = Bulding
        fields = "__all__"
        read_only_fields = ("user",)

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        building = super().create(validated_data)

        for image in uploaded_images:
            image = BuldingImage(building=building, image=image)
            image.save()
            building.images.add(image)

        return building        
