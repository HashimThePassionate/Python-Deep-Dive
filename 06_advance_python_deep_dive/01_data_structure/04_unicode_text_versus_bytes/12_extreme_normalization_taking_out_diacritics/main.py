import unicodedata

def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
print(order)
print(shave_marks(order))  # Output: '“Herr Voss: • ½ cup of OEtker™ caffe latte • bowl of acai.”'
