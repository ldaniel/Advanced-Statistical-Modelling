cpf = "03253709663"
cpf = "03253709662"

is_empty = True if not cpf else False
is_not_11_chars = True if len(cpf) != 11 else False
is_not_only_digits = True if not cpf.isdigit() else False

if is_empty or is_not_11_chars or is_not_only_digits:
    print("formato ou tamanho inválido!")

partial_cpf = cpf[:9]

sum = 0
for i in range(0, len(partial_cpf)):
    sum += int(partial_cpf[i]) * ((int(len(partial_cpf) + 1)) - i)

num = sum % 11
if num <= 1:
    verifying_digit_1 = str(0)
else:
    verifying_digit_1 = str(11 - num)

partial_cpf = cpf[:10]
sum = 0
for i in range(0, len(partial_cpf)):
    sum += int(partial_cpf[i]) * ((int(len(partial_cpf) + 1)) - i)

num = sum % 11
if num <= 1:
    verifying_digit_2 = str(0)
else:
    verifying_digit_2 = str(11 - num)

if not (verifying_digit_1 == cpf[9] and verifying_digit_2 == cpf[10]):
    print("dígito verificador inválido!")