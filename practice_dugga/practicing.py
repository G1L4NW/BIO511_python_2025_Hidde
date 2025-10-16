#if/elif/else clauses

integer = 1

if integer == 0:
    print("integer is zero")
if integer <= 0:
    print(f"integer is negative of value {integer}")
if integer >= 0:
    print(f"integer is positive of value {integer}")
else:
    print("number is not an integer but of type" + type(integer))

# practicing for loops

my_list = ["boem", "pats", "krak", "flats", "sleep", "slag"]

count = 0

for i in my_list:
    print(i)
    count += 1
    print(f"this is iteration {count}")
    if count == 5:
        break

# codons in sequences for and if 

sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
codons = ['ATG', 'TAG', 'TAA', 'TGA']
start = -1
stop = -1
for sequence in sequences:
    print("\nAnalysing sequence:" + sequence)
    for codon in codons:
        if codon in sequence and codon == 'ATG':
            print("sequence has start codon")
            start = sequence.index(codon)
        elif codon in sequence and codon != 'ATG':
            print(f"sequence has stop codon: {codon}")
            stop = sequence.index(codon)
            if start != -1 and stop != -1:
                print("sequence has both start and stop codon")
                if start <= (stop - 3):
                    print("whole start codon is before stop codon")
    
