def validarsenha(s):
    if len(s) < 8:
        return 'Senha invalida, muito curta'
    
    temNumero = False
    temMaiuscula = False
    simbolos = '!@#$%&'
    temSimbolo = False
    
    for c in s:
        if c == ' ':
            return 'Senha invalida, não pode conter espaços'
        if c >= '0' and c<= '9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
            
    if not temNumero:
        return 'Senha invalida, precisa de um número no mínimo um número'
    if not temMaiuscula:
        return 'Senha invalida, precisa de no mínimo uma letra maiuscula'
    if not temSimbolo:
        return 'Senha invalida, precisa de um simbolo pelo menos'
    
    return 'Senha valida'
#main    
senha = input('Digite a senha: ')
r = validarsenha(senha)
print(r)