for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')


text = "El Niño"
encoded_text = text.encode('utf_8')
print(encoded_text)  # b'El Ni\xc3\xb1o'

decoded_text = encoded_text.decode('utf_8')
print(decoded_text)  # El Niño
