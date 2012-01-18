from django import forms
from django.conf import settings
from django.contrib import admin, messages

from tinymce.widgets import TinyMCE

from cms_django.models import TextBlock, ImageBlock, Page, Block, ImageBlock
from cms_django.util import thumbnail, InheritanceQuerySet


class ImageBlockAdmin(admin.ModelAdmin):
	list_display = ('_thumbnail', '_name', 'caption', 'page')
	list_display_links = ('_thumbnail', '_name',)

	fieldsets = (
		('Page', {
			'fields': ('page', )
		}),
		('Image', {
			'fields': ('image', 'caption')
		}),
		('Thumbnail', {
			'fields': ('use_thumbnail', 'thumbnail', 'thumbnail_dimensions')
		})
	)

	def _thumbnail(self, obj):
		return thumbnail(obj.image)

	_thumbnail.short_description = u'Image'
	_thumbnail.allow_tags = True
	
	def _name(self, obj):
		return obj

	_name.short_description = u'File name'
	
class TextBlockForm(forms.ModelForm):
	text = forms.CharField(widget=TinyMCE(attrs={'cols': 85, 'rows': 30}, 
							mce_attrs={'oninit': 'entryOnInit',
										'handle_event_callback' : "entryEvent"}))

	class Meta:
		model = TextBlock

class TextBlockAdmin(admin.ModelAdmin):
	form = TextBlockForm

admin.site.register(TextBlock, TextBlockAdmin)
admin.site.register(ImageBlock, ImageBlockAdmin)

class BlockInline(admin.StackedInline):
	model = Block
	extra = 0
	max_num = 0

	def queryset(self, request):
		id = int(request.META['PATH_INFO'].split('/')[-2])
		return InheritanceQuerySet(model=Block).select_subclasses().filter(page=id)

class PageAdmin(admin.ModelAdmin):
	inlines = [BlockInline, ]

admin.site.register(Page, PageAdmin)