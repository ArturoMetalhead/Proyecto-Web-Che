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

class Pictures(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(
        upload_to="pictures", blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"
        # ordering = ['name']