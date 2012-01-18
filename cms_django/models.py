from django.conf import settings
from django.db import models

from image_cropping.fields import ImageRatioField, ImageCropField


class Block(models.Model):
	pass
	
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


def cropping_size():
	pass
	
class ImageBlock(Block):
	image = ImageCropField(upload_to='uploads/images/%Y/%m')
	caption = models.CharField(max_length=255, blank=True)
	
	use_thumbnail = models.BooleanField(help_text='Whether to crop to the thumbnail dimensions specified below, or simply crop the uploaded image.')
	thumbnail_dimensions = models.CharField(max_length=255, default=settings.IMAGE_CROPPING_SIZE, help_text='Maximum dimensions for cropped image.', blank=True)
	thumbnail = ImageRatioField('image', '0x0') # 0x0 allow users to freely transform thumbnail.
	
	def __unicode__(self):
		return self.image.name
