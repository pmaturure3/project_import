from django.db import models

# Create your models here.

######### New Models #############
class Drugagmp(models.Model):
    drug_id = models.CharField(max_length=50, null=True, blank=True)

class Geneagmp(models.Model):
    gen_id = models.CharField(max_length=50, null=True, blank=True)
    source_db2 = models.CharField(max_length=50, null=True, blank=True)


class Variantagmp(models.Model):
    allele = models.CharField(max_length=50, null=True, blank=True)
    drugagmp = models.ForeignKey(Drugagmp, on_delete=models.CASCADE, default="DRUG0",null=True, blank=True)
    source_db = models.CharField(max_length=50, null=True, blank=True)
    geneagmp = models.ForeignKey(Geneagmp, on_delete=models.CASCADE, default="GENE0",null=True, blank=True)

# class Geneagmp(models.Model):
#     gen_id = models.CharField(max_length=50, null=True, blank=True)


######### New Models #############
