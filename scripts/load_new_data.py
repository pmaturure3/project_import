import csv

from agmp.models import Variantagmp, Drugagmp, Geneagmp, Studyagmp, Phenotypeagmp, VariantStudyagmp
# python3 manage.py runscript load_data
# g is for Gene
# d is for Drug
# v is for Variant
# s is for Study
# p is for Phenotype


def run():

    fhand = open('csv/final.csv',encoding='latin-1')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Variantagmp.objects.all().delete()
    Drugagmp.objects.all().delete()
    Geneagmp.objects.all().delete()
    Studyagmp.objects.all().delete()
    Phenotypeagmp.objects.all().delete()
    VariantStudyagmp.objects.all().delete()
    


    for row in reader:
        # print(row)
        p, created = Phenotypeagmp.objects.get_or_create()
        s, created = Studyagmp.objects.get_or_create(data_ac=row[17],publication_id=row[1],publication_type=[18],publication_year=row[21],study_type=row[11],title=row[19])
        d, created = Drugagmp.objects.get_or_create(drug_bank_id=row[2], drug_name=row[3], indication=row[4], iupac_name_seq=row[5], state=row[6])
        g, created = Geneagmp.objects.get_or_create(chromosome=row[14], function=row[16], uniprot=row[15],gene_name=row[9])
        v = Variantagmp(studyagmp=s,drugagmp=d,phenotypeagmp=p, geneagmp=g,allele=row[0], source_db=row[2])
        v.save()
        vs = VariantStudyagmp(variantagmp=v)
        vs.save()

        no_of_genes = Geneagmp.objects.all().count()
        no_of_drugs = Drugagmp.objects.all().count()
        no_of_variants = Variantagmp.objects.all().count()
        no_of_studies = Studyagmp.objects.all().count()
        no_of_phenotypes = Phenotypeagmp.objects.all().count()
        no_of_varient_studies =VariantStudyagmp.objects.all().count()
    print(" ############ IMPORT JOB ENDED ############ \n")
    print(f"{no_of_varient_studies}: VARIANT STUDIES IMPORTED")
    print(f"{no_of_phenotypes}: PHENOTYPES IMPORTED")
    print(f"{no_of_studies}: Studies IMPORTED")
    print(f"{no_of_genes}: Genes IMPORTED") 
    print(f"{no_of_drugs}: DRUGS IMPORTED") 
    print(f"{no_of_variants}: VARIANTS IMPORTED \n")
    print(" ############ JOB ENDED ############ ")