path = r"C:\Users\aaaa\Desktop\Python-Deep-Dive\06_advance_python_deep_dive\04_unicode_text_versus_bytes\07_handling_text_files\cafe.txt"

# Writing to a file with UTF-8 encoding
fp = open(path, 'w', encoding='utf_8')
print(fp)  # <_io.TextIOWrapper name='cafe.txt' mode='w' encoding='utf_8'>
fp.write('café')
fp.close()

# Checking file size
import os
print(os.stat(path).st_size)  # 5 bytes

# Reading the file without specifying encoding
fp2 = open(path)
print(fp2)  # <_io.TextIOWrapper name='cafe.txt' mode='r' encoding='cp1252'>
print(fp2.encoding)  # 'cp1252'
print(fp2.read())  # 'cafÃ©'

# Reading the file with the correct encoding
fp3 = open(path, encoding='utf_8')
print(fp3)  # <_io.TextIOWrapper name='cafe.txt' mode='r' encoding='utf_8'>
print(fp3.read())  # 'café'

# Reading the file in binary mode
fp4 = open(path, 'rb')
print(fp4)  # <_io.BufferedReader name='cafe.txt'>
print(fp4.read())  # b'caf\xc3\xa9'