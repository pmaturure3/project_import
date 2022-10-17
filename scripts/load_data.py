import csv

from agmp.models import Variantagmp, Drugagmp, Geneagmp
# python3 manage.py runscript load_data
# g is for Gene
# d is for Drug
# v is for Variant

def run():

    fhand = open('csv/final.csv',encoding='latin-1')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Variantagmp.objects.all().delete()
    Drugagmp.objects.all().delete()
    Geneagmp.objects.all().delete()
    


    for row in reader:
        # print(row)

        d, created = Drugagmp.objects.get_or_create(drug_bank_id=row[2], drug_name=row[3], indication=row[4], iupac_name_seq=row[5], state=row[6])
        g, created = Geneagmp.objects.get_or_create(gen_id=row[1])
        v = Variantagmp(allele=row[0], drugagmp=d, geneagmp=g,source_db=row[2])
        v.save()

        no_of_genes = Geneagmp.objects.all().count()
        no_of_drugs = Drugagmp.objects.all().count()
        no_of_variants = Variantagmp.objects.all().count()

    print(" ############ IMPORT JOB ENDED ############ \n")
    print(f"{no_of_genes}: Genes IMPORTED") 
    print(f"{no_of_drugs}: DRUGS IMPORTED") 
    print(f"{no_of_variants}: VARIANTS IMPORTED \n")
    print(" ############ JOB ENDED ############ ")