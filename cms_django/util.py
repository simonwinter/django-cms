from django.conf import settings

try:
    from easy_thumbnails.files import get_thumbnailer

    def thumbnail(image_path):
        thumbnailer = get_thumbnailer(image_path)
        thumbnail_options = {'crop': True, 'size': (160, 120), 'detail': True, 'upscale':True }
        t = thumbnailer.get_thumbnail(thumbnail_options)

        return u'<img src="%s%s" width="100" >' % (settings.MEDIA_URL, t)

except ImportError:
    def thumbnail(image_path):
        absolute_url = os.path.join(settings.MEDIA_ROOT, image_path)
        return u'<img src="%s" width="100" >' % (absolute_url)