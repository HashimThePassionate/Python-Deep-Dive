muhammad = {'name': 'H.A.S.H.I.M', 'born': 1999}
hashim = muhammad

# Checking if they refer to the same object
hashim is muhammad  # Output: True

# Checking their IDs
id(muhammad), id(hashim)  # Output: (ID_value, ID_value)

# Modifying the object through one alias
hashim['balance'] = 950

# Checking the original object
print(muhammad)  # Output: {'name': 'H.A.S.H.I.M', 'born': 1999, 'balance': 950}