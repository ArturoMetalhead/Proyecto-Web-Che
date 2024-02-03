from django.db import models

class Repository(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        # ordering = ['name']