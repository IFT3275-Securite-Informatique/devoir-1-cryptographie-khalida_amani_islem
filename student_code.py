from collections import Counter

def analyze_frequency(ciphertext):
    sequences = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]
    return Counter(sequences)

def create_correspondence(sequence_count, total_sequences):
    sorted_sequences = sorted(sequence_count.items(), key=lambda x: x[1], reverse=True)
    
    
    french_letters = [
        ('E', 17.8), ('S', 8.23), ('A', 7.68), ('N', 7.61), ('T', 7.30),
        ('I', 7.23), ('R', 6.81), ('U', 6.05), ('L', 5.89), ('O', 5.34)
    ]
    
    
    special_chars = [
        (' ', 17.00), (',', 2.50), ('.', 2.40), ("'", 1.50), ('-', 0.50), (':', 0.30)
    ]
    
    
    french_bigrams = "ES LE EN RE SU UR VE TE IT ER".split()
    
    correspondence = {}
    tolerance = 2.0 
    
    
    for seq, count in sorted_sequences:
        seq_freq = (count / total_sequences) * 100
        for letter, theo_freq in french_letters:
            if abs(seq_freq - theo_freq) <= tolerance and letter not in correspondence.values():
                correspondence[seq] = letter
                break
        if seq in correspondence:
            continue
        
        # Ensuite, essayer les caractères spéciaux
        for char, theo_freq in special_chars:
            if abs(seq_freq - theo_freq) <= tolerance and char not in correspondence.values():
                correspondence[seq] = char
                break
    
   
    for seq, _ in sorted_sequences:
        if seq not in correspondence:
            for bigram in french_bigrams:
                if bigram not in correspondence.values():
                    correspondence[seq] = bigram
                    break
    
    return correspondence


C = "11010101011011000111010011001111000011100110110011001111110011000000110111001010010111010111111011001100011011001100111101101100011000011100111100001110011011001100111111001100000011011100101001011101011111101100110001101100011101001100111100001110011011001100111100111111000100100000011000111101000100100110110011001111011011000110000110010101000011000000111001101100110011110010000011001110011000010110110001110100110011110000111001101100110011110010000011001110011000010110110011001111011011000110000111001111000011100110110011001111001111110001001000000110001111010001001001101100011111001100111101011010001011011100101011001111011011001101010111001111"


sequence_count = analyze_frequency(C)
total_sequences = len(C) // 8


correspondence = create_correspondence(sequence_count, total_sequences)

print("Correspondance entre les séquences de 8 bits et les caractères/bigrammes français:")
for cipher_seq, french_char_or_bigram in correspondence.items():
    print(f"{cipher_seq} -> {french_char_or_bigram}")


decrypted = ''.join(correspondence.get(C[i:i+8], '?') for i in range(0, len(C), 8))



print("\nSéquences les plus fréquentes dans le chiffré:")
for seq, count in sequence_count.most_common(15):
    freq = (count / total_sequences) * 100
    print(f"{seq} -> {correspondence.get(seq, '?')}: {count} ({freq:.2f}%)")


print("\nMessage déchiffré:")
print(decrypted)
  
