def adiconar_contato(contatos, informacoes_contato):
    contato = {"informacoes": informacoes_contato, "favoritado": False}
    contatos.append(contato)
    print(f"O contato {informacoes_contato[0]} foi adicionado com sucesso!")
    return


def visualizar_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["favoritado"] else " "
        informacoes_contato = contato["informacoes"]
        print(f"{indice}. [{status}] {informacoes_contato}")
    return


def editar_contato(contatos, indice_contato, novo_nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["informacoes"] = novo_nome_contato
        print(f"O contato {indice_contato} foi atualizado para {novo_nome_contato}")
    else:
        print("Índice de tarefa inválido!")
    return


def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favoritado"] = True
        print(f"O contato {indice_contato} foi adcionado aos favoritos!")
    else:
        print("Índice de contato inválido!")
    return


def desfavoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favoritado"] = False
        print(f"O contato {indice_contato} foi removido dos favoritos!")
    else:
        print("Índice de contato inválido!")
    return


def visualizar_contatos_favoritos(contatos):
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        informacoes_contato = contato["informacoes"]
        if contato["favoritado"] == True:
            print(f"{indice} {informacoes_contato}")
    return


def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato_deletado = contatos.pop(indice_contato_ajustado)
        print(f"O contato {contato_deletado['informacoes'][0]} foi deletado com sucesso!")
    else:
        print("Índice de contato inválido!")
    return


contatos = []

while True:
    print("\nContatos:")
    print("1. Adicionar contato")
    print("2. Visualizar contatos cadastrados")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Desfavoritar contato")
    print("6. Visualizar contatos favoritos")
    print("7. Excluir contato")
    print("8. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        informacoes_contato = input("Digite o nome do contato que deseja adicionar: "), str(input("Digite o número de telefone do contato: ")), input("Digite o email do contato: ")
        adiconar_contato(contatos, informacoes_contato)
    
    elif escolha == "2":
        visualizar_contatos(contatos)
    
    elif escolha == "3":
        visualizar_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja editar: ")
        novo_contato = input("Digite o novo nome do contato: "), input("Digite o novo telefone do contato: "), input("Digite o novo email do contato: ")
        editar_contato(contatos, indice_contato, novo_contato)
    
    elif escolha == "4":
        visualizar_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)
    
    elif escolha == "5":
        visualizar_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja desfavoritar: ")
        desfavoritar_contato(contatos, indice_contato)
    
    elif escolha == "6":
        visualizar_contatos_favoritos(contatos)
    
    elif escolha == "7":
        visualizar_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)

    elif escolha == "8":
        break
