import csv

from agmp.models import Variantagmp, Drugagmp, Geneagmp
# python3 manage.py runscript load_data

def run():

    fhand = open('csv/file.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Variantagmp.objects.all().delete()
    Drugagmp.objects.all().delete()
    Geneagmp.objects.all().delete()
    


    for row in reader:
        # print(row)

        d, created = Drugagmp.objects.get_or_create(drug_id=row[1])
        g, created = Geneagmp.objects.get_or_create(gen_id=row[1])
        v = Variantagmp(allele=row[0], drugagmp=d, geneagmp=g2,source_db=row[2])
     
        v.save()

        no_of_genes = Geneagmp.objects.all().count()
        no_of_drugs = Drugagmp.objects.all().count()
        no_of_variants = Variantagmp.objects.all().count()

    print(" ############ IMPORT JOB ENDED ############ \n")
    print(f"{no_of_genes}: Genes IMPORTED") 
    print(f"{no_of_drugs}: DRUGS IMPORTED") 
    print(f"{no_of_variants}: VARIANTS IMPORTED \n")
    print(" ############ JOB ENDED ############ ")