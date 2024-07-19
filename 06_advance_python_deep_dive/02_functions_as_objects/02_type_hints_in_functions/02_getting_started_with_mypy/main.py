def show_count(count: int, word: str) -> str:
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return f'{count_str} {word}s'

print(show_count(1, 'apple'))
print(show_count(0, 'apple'))
print(show_count(2, 'apple'))



def show_countt(count: int, singular: str, plural: str = '') -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}'

print(show_countt(3, 'mouse', 'mice'))    # Output: '3 mice'
print(show_countt(2, 'child', 'children'))
print(show_countt(1, 'child', 'children'))


# def hex2rgb(color:str) -> tuple[int, int, int]:
#     pass

