from utils import obter_inteiro, escrever

def main():
    escrever("--- Sistema de Segurança ---")
    senha = obter_inteiro("Digite a senha de 4 dígitos: ")
    
    resultado = verificar_senha(senha)
    
    escrever(resultado)


def verificar_senha(senha_digitada):
    SENHA_CORRETA = 1234
    
    if senha_digitada == SENHA_CORRETA:
        return "ACESSO PERMITIDO"
    else:
        return "ACESSO NEGADO"


main()