from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')

    class Meta:
        abstract = True

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("app_a:project_detail", kwargs={"pk": self.pk})
    

class Document(models.Model):
    file = models.FileField('Document', upload_to='app_a/project_docs/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)
    @property
    def filename(self):
        name = self.file.name.split("/")[-1].replace('_',' ').replace('-',' ')
        return name

    def get_absolute_url(self):
        return reverse('app_a:project_detail', kwargs={'pk': self.project.pk})
