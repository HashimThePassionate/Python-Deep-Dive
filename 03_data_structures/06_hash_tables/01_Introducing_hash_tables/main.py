# my_dict = {"Hashim": "9229012345", "Muhammad": "9229012346", "Ishaque":
#            "9229012347", "Sara": "9229012348"}

# print("Print All Keys and values")
# for x, y in my_dict.items():
#     print(f"{x}: {y}")
# print(my_dict["Hashim"])

# print(sum(map(ord,"Hashim")))

def my_hash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv += ord(ch) * mult
        mult += 1
    return hv

for item in ('hello world', 'world hello', 'gello xorld'): 
    print(f'{item}: {my_hash(item)}')

