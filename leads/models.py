from django.db import models

class Lead(models.Model):
    name  = models.CharField(max_length=200)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=20)
    ua    = models.CharField(max_length=400, blank=True)
    ip    = models.GenericIPAddressField(null=True, blank=True)
    ts    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-ts"]

    def __str__(self):
        return f"{self.name} <{self.email}>"
