import json
import os

# Nome do arquivo onde os dados serão salvos
ARQUIVO_DADOS = "usuarios.json"

def carregar_dados():
    """
    Função que lê os dados do arquivo JSON.
    Se o arquivo não existir, retorna uma lista vazia.
    """
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        # Se o arquivo existir mas estiver corrompido/vazio, retorna lista vazia
        return []

def exibir_dados():
    """
    Função para a Opção 1: Lê e exibe os dados do arquivo na tela.
    """
    dados = carregar_dados()
    
    if not dados:
        print("\n[!] Nenhum registro encontrado ou arquivo vazio.")
        return

    print("\n=== REGISTROS ENCONTRADOS ===")
    for idx, pessoa in enumerate(dados, 1):
        print(f"{idx}. Nome: {pessoa['nome']} {pessoa['sobrenome']} | Idade: {pessoa['idade']} anos")
    print("=============================")

def salvar_dados():
    """
    Função para a Opção 2: Solicita os dados do usuário e grava no arquivo JSON.
    """
    print("\n--- Inserir Novo Registro ---")
    nome = input("Digite o nome: ").strip()
    sobrenome = input("Digite o sobrenome: ").strip()
    
    # Validação simples para garantir que a idade seja um número
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0:
                print("Por favor, digite uma idade válida.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números para a idade.")

    # Cria o dicionário com os novos dados
    nova_pessoa = {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade
    }

    # Carrega os dados existentes, adiciona o novo e salva de volta
    dados_existentes = carregar_dados()
    dados_existentes.append(nova_pessoa)

    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(dados_existentes, arquivo, indent=4, ensure_ascii=False)
        print(f"\n[✓] Dados de {nome} salvos com sucesso!")
    except Exception as e:
        print(f"\n[X] Erro ao salvar os dados: {e}")

def menu_principal():
    """
    Função principal que gerencia o menu e o fluxo do programa.
    """
    while True:
        print("\n" + "="*25)
        print("          MENU")
        print("="*25)
        print("1. Ler")
        print("2. Salvar")
        print("3. Sair")
        print("="*25)
        
        opcao = input("Digite uma opção do menu (1-3): ").strip()

        if opcao == "1":
            exibir_dados()
        elif opcao == "2":
            salvar_dados()
        elif opcao == "3":
            print("\nEncerrando a aplicação... Até logo!")
            break
        else:
            print("\n[!] Opção inválida! Escolha um número entre 1 e 3.")

# Garante que o programa só execute se for rodado diretamente
if __name__ == "__main__":
    menu_principal()
