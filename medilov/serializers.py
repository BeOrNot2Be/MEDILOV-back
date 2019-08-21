from rest_framework import serializers
from .models import Photo, Gallery, GalleryTopic, Service, AboutUnit


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("title", "url", "gallery")

class GallerySerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True,  read_only=True)

    class Meta:
        model = Gallery
        fields = ("title", "description", "gallery_logo", "topic", "photos")

class GalleryTopicSerializer(serializers.ModelSerializer):
    galleries = GallerySerializer(many=True, read_only=True)
    
    class Meta:
        model = GalleryTopic
        fields = ("title", 'galleries')

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Service
        fields = ("title", 'short_description', 'long_description', 'img_name', 'url')

class AboutUnitSerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField(many=False) 

    class Meta:
        model = AboutUnit
        fields = ("title", 'short_description', 'phrase', 'parent', 'url', 'color')