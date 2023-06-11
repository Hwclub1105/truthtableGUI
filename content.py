def binary(num):
    if num == 0: return '0'
    output = ''
    while True:
        output += str(num%2)
        if num == 1:
            return output[::-1]
        num //= 2

expression = 'B + ~B = Q'

def stringOfContents(expression):
    noSpace = expression.replace(' ','')
    stripped = noSpace.replace('~','')
    numOfInputs = int((len(stripped)-1)/2)
    statement = expression.replace('+','or').replace('*','and').replace('=','==')

    string = ''.join(x for x in expression if x.isalpha()==True)
    for i in range(2**numOfInputs):
        ans = binary(i)
        string += (numOfInputs-len(ans))*'0' + ans + ' '
    return numOfInputs,string
    

