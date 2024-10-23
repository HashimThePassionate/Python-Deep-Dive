user_data = 'User Details'

def get_user_info(**user_data):
    return f'''
User name is {user_data['name']}
User age is {user_data['age']}
User profession is {user_data['profession']}
User hobbies are {', '.join(user_data['hobbies'])}
    '''
    
def username(name):
    return f'User name is {name}'