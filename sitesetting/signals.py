from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import SiteSetting
from utils.media_cleanup import delete_old_file_on_update, delete_file_on_delete

@receiver(pre_save, sender=SiteSetting)
def logo_image_update_cleanup(sender, instance, **kwargs):
    # Clean up old logo file before updating
    delete_old_file_on_update(instance, SiteSetting, 'logo')

@receiver(post_delete, sender=SiteSetting)
def logo_image_delete_cleanup(sender, instance, **kwargs):
    # Delete logo file after deleting the SiteSetting instance
    delete_file_on_delete(instance, 'logo')

@receiver(pre_save, sender=SiteSetting)
def favicon_image_update_cleanup(sender, instance, **kwargs):
    # Clean up old favicon file before updating
    delete_old_file_on_update(instance, SiteSetting, 'favicon')

@receiver(post_delete, sender=SiteSetting)
def favicon_image_delete_cleanup(sender, instance, **kwargs):
    # Delete favicon file after deleting the SiteSetting instance
    delete_file_on_delete(instance, 'favicon')    