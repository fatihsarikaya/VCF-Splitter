import gzip
import vcf

vcf_reader = vcf.Reader(open(r'C:\Users\SARIKAYA\Desktop\579-22-AA-RE_hg38.hard-filtered.vcf.gz', 'rb'))
for record in vcf_reader:
    print(record)

'''
import sys
import re

def parse_vcf(vcf_file):
    ###Open your file
    with open(vcf_file, '/Users/sarikaya/Desktop/579-22-AA-RE_hg38.hard-filtered.vcf.gz') as vcf_f:
        for line in vcf_f:
            ###Skip metadata lines
            if line[0] != '#':
                ###Split the line by "tab" to keep info field (for me it's the 8th column, so choose the index = 7, I don't remember if it's always the 8th, change this if needed)
                info_field_line = line.split("\t")[7]
                ###Split the info line by ";"
                info_field_line_array = info_field_line.split(";")
                ###For each line of your VCF, create a dictionnary with this array key : info, value : value of this info
                dict_info={}
                for i in info_field_line_array:
                    ###Just looking for line with "=" character (as key = value)
                    if "=" in i:
                        ###Left from equal sign is key (CHROM, POS...)
                        key = i.split("=")[0]
                        ###Right from equal sign is value (RBL1,synonymous_SNV...)
                        value = i.split("=")[1]
                        ###Put them in a dictionnary
                        dict_info[key]=value
                ###After dictionnary creation, you can have an access to all your features (key), just by their name as follow
                my_CHROM = dict_info['CHROM']
                my_POS = dict_info['POS']
                my_REF = dict_info['REF']
                my_ALT = dict_info['ALT']

                print(my_CHROM)
                print(my_POS)
                print(my_REF)
                print(my_ALT)
                ###This is the result for the first line, you can save the data in array to use it later or process line by line as you wish

if __name__ == '__main__':
    vcf=sys.argv[1]
    parse_vcf(vcf)
'''