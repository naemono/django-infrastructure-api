from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Cluster(models.Model):
    """ Represents a K8S Cluster """

    client_certificate_data = models.CharField(max_length=2000)
    client_key_data = models.CharField(max_length=3000)
    cloud_provider = models.ForeignKey('CloudProvider', on_delete=models.DO_NOTHING)
    completed = models.DateTimeField(blank=True, null=True)
    features = JSONField()
    settings = JSONField()
    metadata = JSONField()  # cloud-specific or product-specific data goes here
    num_master_nodes = models.IntegerField(null=False)
    num_compute_nodes = models.IntegerField(null=False)
    region = models.ForeignKey('Region', to_field="name",
                               db_column="region", on_delete=models.DO_NOTHING)
    requested = models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=128)


class Region(models.Model):
    cloud_provider = models.ForeignKey('CloudProvider', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=32, unique=True)


class CloudProvider(models.Model):
    name = models.CharField(max_length=16)


class CloudCredentials(models.Model):
    """ Cloud agnostic model for credentials.
        EC2:
            aws_access_key_id
            aws_secret_access_key
        Azure:
            secret_key
            tenant_id
            xxxx
            xxxx
        GCP:
            Unknown
        Development:
            None
    """
    cloud_provider = models.ForeignKey('CloudProvider', on_delete=models.DO_NOTHING)
    metadata = JSONField()
