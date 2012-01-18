import os
import fnmatch

from django.conf import settings
from django.db import models

from image_cropping.fields import ImageRatioField, ImageCropField


class Block(models.Model):
	page = models.ForeignKey('Page')
	sort_order = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return ''

	class Meta:
		ordering = ('sort_order', )


class TextBlock(Block):
	HEADING_CHOICES = (
		(0, 'h2'),
		(1, 'h3'),
		(2, 'h4'),
		(3, 'h5'),
		(4, 'h6'),
	)
	heading = models.CharField(max_length=255, null=True, blank=True, help_text='Heading to place above the text.')
	heading_tag = models.IntegerField(choices=HEADING_CHOICES, null=True, blank=True, help_text='Heading style to use.')
	text = models.TextField(blank=False)


class ImageBlock(Block):
	image = ImageCropField(upload_to='uploads/images/%Y/%m')
	caption = models.CharField(max_length=255, blank=True)

	use_thumbnail = models.BooleanField(help_text='Crop using the thumbnail dimensions specified below, or simply crop the uploaded image.')
	thumbnail_dimensions = models.CharField(max_length=255, default=settings.IMAGE_CROPPING_SIZE, help_text='Maximum dimensions for cropped image.', blank=True)
	thumbnail = ImageRatioField('image', '0x0') # 0x0 allows users to freely transform thumbnail.

	def __unicode__(self):
		return self.image.name

# class VideoBlock(Block):
# 	pass
# 	
# class UploadVideo(VideoBlock):
# 	pass



class Page(models.Model):
	TEMPLATES = tuple([(settings.CMS_TEMPLATE_PATH + f, f) for (counter, f) in \
					enumerate(os.listdir(settings.CMS_TEMPLATE_PATH)) if fnmatch.fnmatch(f, '*.html')])
	
	template = models.CharField(max_length=255, choices=TEMPLATES)
	
	url = models.CharField(max_length=255, unique=True)
	title = models.CharField(max_length=255)

	is_live = models.BooleanField(default=True)
	
	def blocks(self):
		return Block.objects.all().filter(page=self)

	def __unicode__(self):
		return self.title
