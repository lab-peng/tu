from django.db import models
from django.urls import reverse

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("app_a:project_detail", kwargs={"pk": self.pk})
    

class Document(models.Model):
  file = models.FileField('Document', upload_to='project_docs/')
  project = models.ForeignKey(Project, on_delete=models.CASCADE)

  @property
  def filename(self):
     name = self.file.name.split("/")[1].replace('_',' ').replace('-',' ')
     return name

  def get_absolute_url(self):
     return reverse('app_a:project_detail', kwargs={'pk': self.project.pk})
