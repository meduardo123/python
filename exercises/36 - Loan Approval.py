#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
while True:
    price=float(input('How much does this house cost? '))
    salary=float(input('Whats your salary? '))
    yrs=int(input('In how many years do you plan to pay the house? '))
    inst=yrs*12
    print('------------------------------------')
    print('You need: ${}'.format(price))
    print('Your Salary: ${}'.format(salary))
    print('You wanna pay in {} installments'.format(inst))
    print('-------------------------------------')
    inst_price=price/inst
    limit=salary*0.3
    if inst_price>limit:
        print('unfortunately your loan was denied :(\nThe installment price is ${:.2f}, which exceeds 30 percent of your salary'. format (inst_price))
    elif inst_price==limit:
        print('Wow! Your loan was approved :)\nThe installment price is ${:.2f}, exactly 30 percent of your salary'. format (inst_price))
    else:
        print('Your loan was approved! :)\n Installment price ${:.2f}'.format(inst_price))
    print('--------------------------------------')
    
