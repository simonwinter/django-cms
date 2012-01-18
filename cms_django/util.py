from django.conf import settings
from django.db.models.fields.related import SingleRelatedObjectDescriptor
from django.db.models.query import QuerySet


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


class InheritanceQuerySet(QuerySet):
    def select_subclasses(self, *subclasses):
        if not subclasses:
            subclasses = [o for o in dir(self.model)
                          if isinstance(getattr(self.model, o), SingleRelatedObjectDescriptor)\
                          and issubclass(getattr(self.model,o).related.model, self.model)]
        new_qs = self.select_related(*subclasses)
        new_qs.subclasses = subclasses
        return new_qs

    def _clone(self, klass=None, setup=False, **kwargs):
        try:
            kwargs.update({'subclasses': self.subclasses})
        except AttributeError:
            pass
        return super(InheritanceQuerySet, self)._clone(klass, setup, **kwargs)
        
    def iterator(self):
        iter = super(InheritanceQuerySet, self).iterator()
        if getattr(self, 'subclasses', False):
            for obj in iter:
                obj = [getattr(obj, s) for s in self.subclasses if getattr(obj, s)] or [obj]
                yield obj[0]
        else:
            for obj in iter:
                yield obj
