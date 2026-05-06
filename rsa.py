


p = 47
q = 59
n = 2773
d = 157
e = 17


letra_a_codigo = {' ': '00'}
letra_a_codigo.update({chr(i): str(i - ord('A') + 1).zfill(2) for i in range(ord('A'), ord('Z') + 1)})

codigo_a_letra = {v: k for k, v in letra_a_codigo.items()}
mensaje = "ITS ALL GREEK TO ME"
cripto = []

cadena = ''.join([letra_a_codigo[c] for c in mensaje])
bloques = [cadena[i:i+4] for i in range(0, len(cadena), 4)]


for bloque in bloques:
    M = int(bloque)
    C = pow(M, e, n)
    cripto.append(C)

dencripted = []
for c in cripto:
    D = pow(c, d, n)
    a, b = divmod(D, 100)
    dencripted.append(str(a).zfill(2))  
    dencripted.append(str(b).zfill(2))
    #dencripted.extend(divmod(D, 100))
original = []

for d in dencripted:
        original.append(codigo_a_letra[d])
print("Mensaje:", mensaje)
print("Numeros: ",bloques)
print("Numeros encriptados: ",cripto)
print("Desencriptado: ", original)
