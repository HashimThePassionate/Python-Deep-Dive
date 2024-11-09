from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'muhammad hashim' work?"""
    formatted_name = get_formatted_name('muhammad', 'hashim')
    assert formatted_name == 'Muhammad Hashim'

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'