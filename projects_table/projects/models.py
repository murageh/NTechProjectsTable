# Create your models here.
from django.db import models as models
from django.urls import reverse


class Projects(models.Model):
    # Fields
    project_name = models.CharField(max_length=255)
    github_link = models.URLField()
    youtube_link = models.URLField(blank=True)
    points_awarded = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    assessor_id = models.IntegerField()

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('projects_projects_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('projects_projects_update', args=(self.pk,))
