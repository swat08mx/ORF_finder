import math
seq = "TACAAGCCCCCGCGGACACGCTTCGGCTTACAGGAATGGTACCAATTAACAGATTCAGTCAATAAATTGTAGCATTGCCCACTGTGCTAGTGAAACTCGATAATATTCACAGTCTGACGGTGAATGGCAACTATCACCAGTTACATAAA"
gc_content_upper = int(input("Enter the GC percentage upper limit: "))
gc_content_lower = int(input("Enter the GC percentage lower limit: "))
t_m_upper = int(input("Enter the upper Melting temperature of the seq: "))
t_m_lower = int(input("Enter the lower Melting temperature of the seq: "))

def gc_content_percentage(seq):
    gc_count=0
    calc=0
    for i in range(len(seq)):
        if seq[i] == 'G' or seq[i] == 'C':
            gc_count+=1
        calc=round(gc_count / len(seq) * 100)
    return("The GC percentage is %.0f" % calc)
result = gc_content_percentage(seq)
print(result)


def t_m_cal(seq):
    tcount=0 
    acount=0 
    gcount=0
    ccount=0
    t_m_res=0
    #Tm= 64.9 +41*(yG+zC-16.4)/(wA+xT+yG+zC)
    for letter in seq:
        if letter == 'A':
            acount+=1
        elif letter == 'T':
            tcount+=1
        elif letter == 'G':
            gcount+=1
        elif letter == 'C':
            ccount+=1
    t_m_res = 64.9 + 41 * (gcount + ccount - 16.4) / (acount + tcount + gcount + ccount)
    return("The Melting temperature is %.0f" % t_m_res)
result = t_m_cal(seq)
print(result)

temp=""
temp_gc_percentage=0
temp_t_m_cal=0
for i in range(len(seq)):
    temp += seq[i]
    for j in range(len(seq)):
        temp_gc_percentage = int(gc_content_percentage(temp))
        if temp_gc_percentage >= gc_content_lower and temp_gc_percentage <= gc_content_upper:
            pass
            temp_t_m_cal = int(t_m_cal(temp))
            if temp_t_m_cal >= t_m_lower and temp_t_m_cal <= t_m_upper:
                print(f"The primer is {temp} with a melting temp of {t_m_cal(temp)} and a GC% of {gc_content_percentage(temp)}%")
# print(temp)
# temp_gc_percentage=gc_content_percentage(temp)
# print(temp_gc_percentage)
                
            
            
    
            




    