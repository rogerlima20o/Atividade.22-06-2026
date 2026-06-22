import os

def exibir_menu():
    print("\n" + "="*30)
    print("         MENU DE OPÇÕES")
    print("="*30)
    print("1. Ler")
    print("2. Salvar")
    print("3. Sair")
    print("="*30)

def ler_arquivo():
    nome_arquivo = input("\nDigite o nome ou caminho do arquivo para ler (ex: dados.txt): ").strip()
    
    # Verifica se o arquivo realmente existe antes de tentar abrir
    if os.path.exists(nome_arquivo):
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                print("\n--- Conteúdo do Arquivo ---")
                print(conteudo)
                print("---------------------------")
        except Exception as e:
            print(f"\n[ERRO] Não foi possível ler o arquivo: {e}")
    else:
        print("\n[AVISO] Arquivo não encontrado! Verifique o nome e tente novamente.")

def salvar_arquivo():
    nome_arquivo = input("\nDigite o nome do arquivo para salvar (ex: dados.txt): ").strip()
    print("Digite o texto que deseja salvar (Pressione Enter para finalizar):")
    conteudo = input("> ")
    
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
        print(f"\n[SUCESSO] Dados gravados com sucesso no arquivo '{nome_arquivo}'!")
    except Exception as e:
        print(f"\n[ERRO] Não foi possível salvar o arquivo: {e}")

def executar_programa():
    while True:
        exibir_menu()
        opcao = input("Digite uma opção do menu (1-3): ").strip()
        
        if opcao == "1":
            ler_arquivo()
        elif opcao == "2":
            salvar_arquivo()
        elif opcao == "3":
            print("\nSaindo da aplicação. Até logo!")
            break
        else:
            print("\n[OPÇÃO INVÁLIDA] Por favor, escolha um número de 1 a 3.")

# Executa o programa principal
if __name__ == "__main__":
    executar_programa()