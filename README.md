# Atividade.22-06-2026

# Gerenciador de Arquivos via Terminal (CLI)

Um aplicativo simples e eficiente em Python executado diretamente no terminal. O programa oferece uma interface de linha de comando (CLI) estruturada em menu para leitura e gravação de arquivos de texto de forma segura.

## 🚀 Funcionalidades

* **Menu Interativo:** Navegação simples através de opções numéricas (1 a 3).
* **Leitura Segura:** Validação de existência do arquivo antes da abertura, evitando que o programa trave caso o arquivo não seja encontrado.
* **Gravação de Dados:** Permite criar novos arquivos de texto ou sobrescrever arquivos existentes com codificação UTF-8 (garantindo compatibilidade com acentos e caracteres especiais).
* **Tratamento de Erros:** Captura e exibição amigável de exceções do sistema (como permissões negadas ou falhas de disco).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Módulo `os`:** Utilizado especificamente para a verificação de caminhos de arquivos no sistema operacional (`os.path.exists`).

---

## 📋 Pré-requisitos

Você só precisa ter o **Python 3.x** instalado em sua máquina. Nenhuma biblioteca externa adicional é necessária, pois o projeto utiliza apenas módulos nativos.

---

## 🔧 Como Executar

1. **Baixe ou clone o código** para uma pasta no seu computador.
2. Abra o terminal (ou Prompt de Comando) e **navegue até a pasta** onde o arquivo está salvo.
3. Execute o programa com o comando:
   ```bash
   python nome_do_seu_arquivo.py
