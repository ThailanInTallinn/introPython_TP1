desconto_txt = '28'
desconto_decimal = float(desconto_txt)
desconto_num = desconto_decimal / 3.14
valor_final = 599.99 - desconto_num
print("{:.2f}".format(valor_final))
