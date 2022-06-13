"""
CPF = 168.955.350-09
-------------------------------------------------------
1 * 10 = 10             #     1 * 11 = 11 <-
8 * 8  = 64             #     6 * 10 = 60
6 * 9  = 54             #     8 * 9  = 72
9 * 7  = 63             #     9 * 8  = 72
9 * 6  = 54             #     5 * 7  = 63
5 * 5  = 25             #     5 * 6  = 30
3 * 4  = 12             #     3 * 5  = 15
5 * 3  = 15             #     5 * 4  = 20
0 * 2  = 0              #     0 * 3  = 0
                        #  -> 0 * 2  = 0
        297             #              343
11 - (297 % 11) = 11    #     11 - (343 % 11)= 9
11 > 9 = 0              #
Digito 1 = 0            #    Digito 2 = 9
"""

cpf = '16899535009'
nCPF = cpf[:9]
calculo = 0
total = 0

print(nCPF)

for divcpf, desc in zip(nCPF, range(10, 1, -1)):
    # print(f'{divcpf} * {desc} = {int(divcpf) * desc}')
    calculo += int(divcpf) * desc

total = 11 - (calculo % 11)

if total > 9:
    nCPF = nCPF + str(0)
else:
    nCPF = nCPF + str(total)

print(f'{nCPF} - Com 1º digito acrescido')

calculo = 0
total = 0
for divcpf, desc in zip(nCPF, range(11, 1, -1)):
    # print(f'{divcpf} * {desc} = {int(divcpf) * desc}')
    calculo += int(divcpf) * desc

total = 11 - (calculo % 11)

if total > 9:
    nCPF = nCPF + str(0)
else:
    nCPF = nCPF + str(total)

print(f'{nCPF} - Com 2º digito acrescido')

if cpf == nCPF:
    print('CPF é válido')
else:
    print('CPF é inválido')
