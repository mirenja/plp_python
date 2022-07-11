
# _parenthesis = "()"
operators =  '*-*/'
_preference = {
    '*' : 1,
    '/' : 1,
    '+' : 0,
    '-' : 0,
}

def _priority(operator1,operator2):
    if _preference[operator1] > _preference[operator2]:
        print(f"{operator1} has higher priority than {operator2}")
    elif _preference[operator1] < _preference[operator2]:
        print(f"{operator2} has higher priority than {operator1}")
    else:
        print('priority is equal')
   

    
print(_priority('+','/'))
print(_priority('-','+'))
print(_priority('*','-'))
print(_priority('/','-'))