import gzip
import vcf

vcf_reader = vcf.Reader(open(r'C:\Users\SARIKAYA\Desktop\579-22-AA-RE_hg38.hard-filtered.vcf.gz', 'rb'))
for record in vcf_reader:
    print(record)