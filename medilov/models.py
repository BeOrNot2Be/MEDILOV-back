from djongo import models


# main page models

class GalleryTopic(models.Model):
    title = models.CharField('topic title', max_length=30, unique=True)
    date = models.DateTimeField('last update', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'gallery topic'
        verbose_name_plural = 'gallery topics'


class Gallery(models.Model):
    title = models.CharField('gallery title', max_length=30,  unique=True)
    description = models.CharField(
        'gallery description', max_length=255, blank=True)
    date = models.DateTimeField('last update', auto_now=True)
    gallery_logo = models.CharField('img logo url', max_length=1000)
    topic = models.ForeignKey(
        GalleryTopic, models.DO_NOTHING, null=True, blank=True, related_name='galleries')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleris'


class Photo(models.Model):
    title = models.CharField('img title', max_length=30)
    url = models.CharField('img url', max_length=1000, unique=True)
    date = models.DateTimeField('last update', auto_now=True)
    gallery = models.ForeignKey(
        Gallery, models.DO_NOTHING, null=True, blank=True, related_name='photos')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


class Video(models.Model):
    title = models.CharField('video title', max_length=30)
    url = models.CharField('video url', max_length=1000, unique=True)
    preview = models.CharField('img url', max_length=1000, unique=True)
    gallery = models.ForeignKey(
        Gallery, models.DO_NOTHING, null=True, blank=True, related_name='videos')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'


# service page models

class Service(models.Model):
    title = models.CharField('service title', max_length=30)
    short_description = models.CharField(
        'short service description', max_length=350, blank=True)
    long_description = models.CharField(
        'long service description', max_length=5000)
    img_name = models.CharField('img name', max_length=30, blank=True)
    url = models.CharField('img url', max_length=1000, blank=True)
    date = models.DateTimeField('last update', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

# about page models


class AboutUnit(models.Model):
    short_description = models.CharField(
        'short post description', max_length=350, blank=True)
    phrase = models.CharField('letters for phrase', max_length=10, blank=True)
    title = models.CharField('img title', max_length=30)
    url = models.CharField('img url', max_length=1000, blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        related_name='children',
        blank=True)
    date = models.DateField()
    color = models.CharField(max_length=7, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about post'
        verbose_name_plural = 'about posts'

# contact page models
