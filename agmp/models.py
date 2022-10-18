from django.db import models

# Create your models here.

######### New Models #############
class Drugagmp(models.Model):
    drug_id = models.CharField(max_length=50, null=True, blank=True)
    drug_bank_id = models.CharField(max_length=50, null=True, blank=True)
    drug_name = models.CharField(max_length=50, null=True, blank=True)
    indication = models.CharField(max_length=50, null=True, blank=True)
    iupac_name_seq = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)

class Geneagmp(models.Model):
    # gen_id = models.CharField(max_length=50, null=True, blank=True)
    # source_db = models.CharField(max_length=50, null=True, blank=True)
    chromosome = models.CharField(max_length=50, null=True, blank=True)
    function = models.CharField(max_length=50, null=True, blank=True)
    gene_name= models.CharField(max_length=50, null=True, blank=True)
    uniprot= models.CharField(max_length=50, null=True, blank=True)

class Studyagmp(models.Model):
    data_ac = models.CharField(max_length=50, null=True, blank=True)
    publication_id = models.CharField(max_length=50, null=True, blank=True)
    publication_type = models.CharField(max_length=50, null=True, blank=True)
    publication_year = models.CharField(max_length=50, null=True, blank=True)
    study_type = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)

class Phenotypeagmp(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
   

class Variantagmp(models.Model):
    allele = models.CharField(max_length=50, null=True, blank=True)
    drugagmp = models.ForeignKey(Drugagmp, on_delete=models.CASCADE, default="DRUG0",null=True, blank=True)
    source_db = models.CharField(max_length=50, null=True, blank=True)
    geneagmp = models.ForeignKey(Geneagmp, on_delete=models.CASCADE, default="GENE0",null=True, blank=True)
    studyagmp = models.ForeignKey(Studyagmp, on_delete=models.CASCADE,null=True, blank=True)
    phenotypeagmp = models.ForeignKey(Phenotypeagmp, on_delete=models.CASCADE,null=True, blank=True)


class VariantStudyagmp(models.Model):
    variantagmp = models.ForeignKey(Variantagmp, on_delete=models.CASCADE,null=True, blank=True)
    country_participant = models.CharField(max_length=50, null=True, blank=True)
    ethnicity = models.CharField(max_length=50, null=True, blank=True)
    geographical_regions = models.CharField(max_length=50, null=True, blank=True)
    notes = models.CharField(max_length=50, null=True, blank=True)
    p_value = models.CharField(max_length=50, null=True, blank=True)
  
  
# class Geneagmp(models.Model):
#     gen_id = models.CharField(max_length=50, null=True, blank=True)


######### New Models #############
