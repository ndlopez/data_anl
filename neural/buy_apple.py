from multi import *
'''
apples 2 <-- (x) 200 <-- (+) 650 <-- (x) 715 <-- all
      110        1.1         
'''
apple=100
apple_num=2
orange=150
orange_num=3
tax=1.08
mul_apple_layer=MultiLayer()#layer
mul_orange_layer=MultiLayer()
add_apple_orange_layer=AddLayer()
mul_tax_layer=MultiLayer()
apple_price=mul_apple_layer.forward(apple,apple_num)#forward
orange_price=mul_orange_layer.forward(orange,orange_num)
all_price=add_apple_orange_layer.forward(apple_price,orange_price)
price=mul_tax_layer.forward(all_price,tax)
print('Price (Tax in)',price)

dprice=1
dall_price,dtax=mul_tax_layer.backward(dprice)#backward
dapple_price,dorange_price=add_apple_orange_layer.backward(dall_price)
dorange,dorange_num=mul_orange_layer.backward(dorange_price)
dapple,dapple_num=mul_apple_layer.backward(dapple_price)
print('1 Apple',dapple_num,'??',dapple,'\n1 Orange',dorange_num,'??',dorange,'\nTax(Price w/o tax)',dtax)
