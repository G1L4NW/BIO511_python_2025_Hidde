#DNA sequences in list
sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
# Define start and stop codons
start_codons = ['ATG']
stop_codons = ['TAA', 'TAG', 'TGA']
# Loop through sequences and check for start and stop codons
for sequence in sequences:
    print(f"\nAnalyzing sequence: " + sequence)
    # go through all start codons and check if they are in the sequence assign position to found codons
    for start_codon in start_codons:
        if start_codon in sequence:
            print(start_codon + " is in " + sequence)
            position_start = sequence.index(start_codon)
    if start_codon not in sequence:
        print("No start codon found in " + sequence)
    # go through all stop codons and check if they are in the sequence assign position to found codons
    for stop_codon in stop_codons:
        if stop_codon in sequence:
            print(stop_codon + " is in " + sequence)
            position_stop = sequence.index(stop_codon)
        if start_codon in sequence and stop_codon in sequence:
            print("Both start codon and " + stop_codon + " are in " + sequence)
        # Check the order of start and stop codon
            if position_start < position_stop:
                print("Start codon is before " + stop_codon + " in " + sequence)
            else:
                print("Start codon is after " + stop_codon + " in " + sequence)
    # Check if no stop codon is in sequence
    if all(stop_codon not in sequence for stop_codon in stop_codons):
        print("No stop codon found in " + sequence)
    # Check if both start and stop codon are in sequence
    