def adicionar_contato(contatos, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"\nContato '{nome}' foi adicionado com sucesso!\n")

def editar_contato(contatos):
    nome_procurado = input("Digite o nome do contato que deseja editar: ")

    for contato in contatos:
        if contato["nome"].lower() == nome_procurado.lower():
            print("\nContato encontrado! Deixe em branco se não quiser alterar o contato.")

            novo_nome = input(f"Novo nome ({contato['nome']}): ")
            novo_telefone = input(f"Novo telefone ({contato['telefone']}): ")
            novo_email = input(f"Novo email ({contato['email']}): ")

            if novo_nome != "":
                contato["nome"] = novo_nome
                
            if novo_telefone != "":
                contato["telefone"] = novo_telefone
                
            if novo_email != "":
                contato["email"] = novo_email

            print("\nContato atualizado com sucesso!")
            return
        
    print("\nContato não encontrado.")

def adicionar_favorito(contatos):
    nome_procurado = input("Digite o nome do contato que deseja adicionar aos favoritos: ")

    for contato in contatos:
        if contato["nome"].lower() == nome_procurado.lower():
            if contato["favorito"]:
                print("\nEste contato já está nos favoritos!")
            else:
                contato["favorito"] = True
                print(f"\nContato '{contato['nome']}' adicionado aos favoritos!")
            return

    print("\nContato não encontrado.")

def remover_favorito(contatos):
    nome_procurado = input("Digite o nome do contato que deseja REMOVER dos favoritos: ")

    for contato in contatos:
        if contato["nome"].lower() == nome_procurado.lower():
            if contato["favorito"]:
                contato["favorito"] = False
                print(f"\nContato '{contato['nome']}' removido dos favoritos!")
            else:
                print("\nEste contato NÃO estava marcado como favorito.")
            return

    print("\nContato não encontrado.")

def visualizar_favoritos(contatos):
    print("\nContatos favoritos:\n")

    favoritos = [c for c in contatos if c["favorito"]]

    if len(favoritos) == 0:
        print("Nenhum contato marcado como favorito.\n")
    else:
        for c in favoritos:
            print(f"Nome: {c['nome']}")
            print(f"Telefone: {c['telefone']}")
            print(f"Email: {c['email']}")
            print("_" * 30)

def apagar_contato(contatos):
    nome_procurado = input("Digite o nome do contato que deseja EXCLUIR: ")

    for contato in contatos:
        if contato["nome"].lower() == nome_procurado.lower():
            contatos.remove(contato)
            print(f"\nContato '{contato['nome']}' excluído com sucesso!")
            return

    print("\nContato não encontrado.")


contatos = []

while True:
    print("\nAgenda de contatos")
    print("1. Adicionar um contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar um contato existente")
    print("4. Adicionar contato como favorito")
    print("5. Remover contato como favorito")
    print("6. Visualizar contatos favoritos")
    print("7. Excluir contato") 
    print("8. Sair") 

    escolha = input("Digite o numero de sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome do seu contato: ")
        telefone = input("Digite o telefone do seu contato: ")
        email = input("Digite o email do seu contato: ")

        adicionar_contato(contatos, nome, telefone, email)

        input("\nPressione ENTER para voltar ao menu...")

    elif escolha == "2":
        print("\nContatos cadastrados: \n")

        if len(contatos) == 0:
            print("Nenhum contato cadastrado. \n")
        else:
            for c in contatos:
                print(f"Nome: {c['nome']}")
                print(f"Telefone: {c['telefone']}")
                print(f"Email: {c['email']}")
                print(f"Favorito: {c['favorito']}")
                print("_" *30)

        input("\nPressione ENTER para voltar ao menu...")

    elif escolha == "3":
        editar_contato(contatos)
        input("\nPressione ENTER para voltar ao menu...")

    elif escolha == "4":
        adicionar_favorito(contatos)
        input("\nPressione ENTER para voltar ao menu...")

    elif escolha == "5":
        remover_favorito(contatos)
        input("\nPressione ENTER para voltar ao menu...")

    elif escolha == "6":
        visualizar_favoritos(contatos)
        input("\nPressione ENTER para voltar ao menu...")

    elif escolha == "7":
        apagar_contato(contatos)
        input("\nPressione ENTER para voltar ao menu...")

    elif escolha == "8":
        break
print("Programa Finalizado")