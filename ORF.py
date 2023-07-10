import time
start_time = time.perf_counter()
codons = {
    'GCT': 'Ala','GCC': 'Ala','GCA': 'Ala','GCG': 'Ala','CGT': 'Arg','CGC': 'Arg','CGA': 'Arg','CGG': 'Arg','AGA': 'Arg','AGG': 'Arg',
    'AAT': 'Asn','AAC': 'Asn','GAT': 'Asp','GAC': 'Asp','TGT': 'Cys','TGC': 'Cys','CAA': 'Gln','CAG': 'Gln','GAA': 'Glu','GAG': 'Glu',
    'GGT': 'Gly','GGC': 'Gly','GGA': 'Gly','GGG': 'Gly','CAT': 'His','CAC': 'His','ATT': 'Ile','ATC': 'Ile','ATA': 'Ile','TTA': 'Leu',
    'TTG': 'Leu','CTT': 'Leu','CTC': 'Leu','CTA': 'Leu','CTG': 'Leu','AAA': 'Lys','AAG': 'Lys','ATG': 'Met','TTT': 'Phe','TTC': 'Phe',
    'CCT': 'Pro','CCC': 'Pro','CCA': 'Pro','CCG': 'Pro','TCT': 'Ser','TCC': 'Ser','TCA': 'Ser','TCG': 'Ser','AGT': 'Ser','AGC': 'Ser',
    'ACT': 'Thr','ACC': 'Thr','ACA': 'Thr','ACG': 'Thr','TGG': 'Trp','TAT': 'Tyr','TAC': 'Tyr','GTT': 'Val','GTC': 'Val','GTA': 'Val',
    'GTG': 'Val','TAA': '','TAG': '','TGA': ''
}
# file = open('sequence 2.fasta','r')
# newlist=[]
# seq=''
# listtwo=[]
# for lines in file:
#     count=0
#     if '\n' in lines:
#         newlist.append(lines)
# for i in range(1,len(newlist)-1):
#     seq+=newlist[i]
# result = "".join(line.strip() for line in seq.splitlines())
results='gatgttcgggggcgcctgtgcgaagccgaatgtccttaccctggttaattgtctaagtcagttatttaacatcgtcacgggtgacacgatcgctttgagctattataagtgtcagactgccacttaccgttgatagtggtcaatgtattt'
result = results.upper()
####### functions ########
def translation(final_string):
        points=0
        translated=''
        letters=''
        final = final_string.replace(' ', '')
        for i in range(len(final)):
            letters+=final[i]
            points+=1
            if points==3:
                translated+=codons[letters]
                points=0
                letters=''
        if final_string=='':
            pass
        else:    
            return translated
def spaces(f, result):
    seq_pos = ""
    count = 0
    for i in range(f, len(result)):
        seq_pos += result[i]
        count += 1
        if count == 3:
            count = 0
            seq_pos += " "
    return seq_pos

def driver_main(count, result):
    for f in range(3):
        seq_pos = spaces(f, result)
        if count==0:
            print(f"The +{f+1} reading frame is: {seq_pos}")
        elif count==1:
            print(f"The -{f+1} reading frame is: {seq_pos}")
        orfs=[]
        point=0
        found=1
        final_string=''
        for i in range(len(seq_pos)):
            try:
                if seq_pos[i]=='A' and seq_pos[i+1]=='T' and seq_pos[i+2]=='G':
                    found+=1
                    for j in range((i+3),len(seq_pos)):
                        if seq_pos[j]=='T'and seq_pos[j+1]=='A' and seq_pos[j+2]=='G':
                            point+=1
                            break
                        elif seq_pos[j]=='T'and seq_pos[j+1]=='G' and seq_pos[j+2]=='A':
                            point+=1
                            break
                        elif seq_pos[j]=='T'and seq_pos[j+1]=='A' and seq_pos[j+2]=='A':
                            point+=1
                            break
                        else:
                            final_string+=seq_pos[j]
                    if found>1 and found%found==0:
                        orfs.append('ATG'+final_string)
                        final_string=''
            except:
                pass
        if point!=0:
            try:
                for i, orf in enumerate(orfs):
                    print(f'The ORFs {i+1} is: {orf}')
                    print()
                    print(f'The amino acid sequence for ORF{i+1} is: {translation(orf)}')
                    print()
            except:
                    print()
                    print("*******************There was an unknown error in translation at ORF, report this to dev.**********************")
                    print()
                    pass
        elif point==0:
            print("No reading frames were found")
            print()
            pass
        if 'ATG' not in seq_pos:
            print("No reading frames were found")
            print()
    return 
count=0
print(driver_main(count, result))
comp = str.maketrans("ATGC", "TACG")
complement = result.translate(comp)
count=1
print(driver_main(count, complement))
print("This is a new try commit")
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.5f} seconds")





