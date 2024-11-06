def decrypt(C):
  M= []
    for i in range(0, len(C), 8):  # Traiter 8 bits d'un coup
        binary_sequence = C[i:i+8]
        decryption_key={v: k for k, v in encryption_key.items()}
        symbol = decryption_key.get(binary_sequence, None)
        if symbol:
            M.append(symbol)
    return ''.join(M)
  
