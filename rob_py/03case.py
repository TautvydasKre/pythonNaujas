    # +, -, *, /, ^, saknies traukimas - &
import math;
sk1 = float(input('sk1='));
oper = input('Operacija=');

if(oper != '&'):
    sk2=float(input('sk2='));

match oper:
    case "^":
        print(f'{sk1}^ = {sk1**2}')
    case "&":
        if(sk1 > 0):
            print(f'{sk1} & = ', math.sqrt(sk1))
        else:
            print('Neigiama negalima')
    case "+":
        print(f'{sk1} + {sk2} = {sk1+sk2}')
    case "-":
        print(f'{sk1} - {sk2} = {sk1-sk2}')
    case "*":
        print(f'{sk1} * {sk2} = {sk1*sk2}')
    case "/":
        if(sk2 != 0):
            print(f'{sk1} / {sk2} = {sk1/sk2}')
        else:
            print('Dalyba is 0 negalima')
    case default:
        print('Operacija nerasta')