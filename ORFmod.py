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
### To put your own FASTA file into the prog, de-comment the following code and comment the 24th and 25th line ###

file = open('seve.fasta','r')
newlist=[]
seq=''
listtwo=[]
for lines in file:
    count=0
    if '\n' in lines:
        newlist.append(lines)
for i in range(1,len(newlist)-1):
    seq+=newlist[i]
result = "".join(line.strip() for line in seq.splitlines())

# results='gatgttcgggggcgcctgtgcgaagccgaatgtccttaccctggttaattgtctaagtcagttatttaacatcgtcacgggtgacacgatcgctttgagctattataagtgtcagactgccacttaccgttgatagtggtcaatgtattt'
# result = results.upper()


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

def del_spaces(seq):
    for i in range(len(seq)):
        if seq[i]==' ':
            seqnew=seq.replace(' ', '')
    return(seqnew)
    

def driver_main(count, result, number):
    for f in range(3):
        seq_pos = spaces(f, result)
        if count==0:
            print(f"The +{f+1} reading frame is: {seq_pos}\n")
        elif count==1:
            print(f"The -{f+1} reading frame is: {seq_pos}\n")
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
                            signal=1 
                            break
                        elif seq_pos[j]=='T'and seq_pos[j+1]=='G' and seq_pos[j+2]=='A':
                            point+=1
                            signal=2
                            break
                        elif seq_pos[j]=='T'and seq_pos[j+1]=='A' and seq_pos[j+2]=='A':
                            point+=1
                            signal=3
                            break
                        else:
                            final_string+=seq_pos[j]
                    if found>1:
                        orfs.append('ATG'+final_string)
                        final_string=''
            except:
                pass
        if point!=0:
            try:
                for i, orf in enumerate(orfs):
                    new_orf=del_spaces(orf)
                    if len(new_orf) > number:
                        if signal==1:
                            print(f'The ORFs {i+1} is: {orf}TAG\n')
                        elif signal==2:
                            print(f'The ORFs {i+1} is: {orf}TGA\n')
                        elif signal==3:
                            print(f'The ORFs {i+1} is: {orf}TAA\n')
                        print(f'The amino acid sequence for ORF{i+1} is: {translation(orf)}\n')
                    else:
                        continue
            except:
                    print()
                    print("*******************There was an unknown error in translation at ORF, report this to dev.**********************\n")
                    print()
                    pass
        elif point==0:
            print("No reading frames were found\n")
            pass
        if 'ATG' not in seq_pos:
            print("No reading frames were found\n")
    return " "
count=0
print("Minimal ORF length 'nt' \n 1. 30 \n 2. 75 \n 3. 150 \n 4. 300 \n 5. 600 \n")
number=int(input("Enter the value: "))
print(driver_main(count, result, number))
comp = str.maketrans("ATGC", "TACG")
complement = result.translate(comp)
count=1
print(driver_main(count, complement, number))
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.5f} seconds")
