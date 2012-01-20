# Requirements

This Django application requires the following:

* Django 1.3.1 and above: it was built against 1.3.1, but may work with other versions of 1.3.
* Django image cropping: https://github.com/jonasundderwolf/django-image-cropping
* easy-thumbnails https://github.com/SmileyChris/easy-thumbnails
* django tiny mce http://code.google.com/p/django-tinymce/
* `django.contrib.staticfiles` https://docs.djangoproject.com/en/dev/howto/static-files/

## Settings

The following settings are required to activate this app as intended.

### settings.py

	IMAGE_CROPPING_THUMB_SIZE = (400, 400)
	IMAGE_CROPPING_SIZE = '300x300'
	IMAGE_CROPPING_SIZE_WARNING = True
	
	TINYMCE_JS_URL = '/static/tiny_mce/tiny_mce.js'
	TINYMCE_DEFAULT_CONFIG = {
		'theme' : "advanced", 
		'theme_advanced_toolbar_location' : "top",
		'theme_advanced_toolbar_align' : "left",
		'relative_urls': False,
		'theme_advanced_buttons1' : "bold,italic,separator,link,unlink",
		'theme_advanced_buttons2' : "",
		'theme_advanced_buttons3' : "",
		'plugins': "paste",
		'paste_auto_cleanup_on_paste' : True,
		'paste_remove_styles' : True,
		'paste_remove_styles_if_webkit' : True,
	    'paste_strip_class_attributes': True,
	}
	
	# the location of templates used by the cms. by default, should be inside the app's templates/cms folder.
	CMS_TEMPLATE_PATH = os.path.realpath(os.path.dirname(__file__)) + '/cms_django/templates/cms/'
	
	INSTALLED_APPS = (
        ...
        'cms_django',
        'tinymce',
        'easy_thumbnails',
	    'image_cropping',
        ...
    )