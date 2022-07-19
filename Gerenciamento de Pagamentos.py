v=float(input('Qual é o valor do Produto? R$ '))
print('O valor do Produto é de R${:.2f} '.format(v))

f=input('Qual é a forma de pagamento?:')

v1= v-(v*10/100)
x1= v - v1
v2= v+(v*8/100)
f1= 'A vista'
f2= 'Parcelado'

if f == f1:
    print('À vista há um desconto de 5% que é igual a R$ {}.\nTendo como total à pagar de R$ {}'.format(x1,v1))


else:
    v0=float(input('Quantas vezes será o parcelamento?'))
    v3 = v / v0
    v4 = v3 + (v3 * 8 / 100)
    v5= v + (v*8/100)
    #print(v0)
    print('Para o parcelamento há um acréscimo de 5%!.\nEntão o valor total a pagar é de R$ {}\nO valor total com acréscimo é de R$ {} em {:.0f}x no cartão! '.format(v5,v4,v0))