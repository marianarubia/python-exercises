#"exiba o primeiro nome do usuário e tudo minúsculo no menu do app"
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('bem vindo {}'.format(n[0].lower()))
