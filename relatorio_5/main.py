from relatorio_5.book_crud import Book


def print_menu():
    print(f"""
{"=" * 10}Books Menu{"=" * 10}

[ 1 ] Cadastrar Livro
[ 2 ] Buscar Livro pelo ID
[ 3 ] Deletar Livro pelo ID
[ 4 ] Atualizar Livro pelo ID
[ 5 ] Sair do Programa

{"".rjust(30, "=")}
        """
    )


print_menu()

book_manager = Book()

while True:
    option = input("Escolha uma opção: ")
    match option:
        case "1":
            title = input("Digite o título do livro: ")
            author = input("Digite o nome do autor do livro: ")
            year = input("Digite o ano de lançamento: ")
            price = input("Digite o preço do livro: ")

            book_manager.isert({
                "titulo": title,
                "autor": author,
                "ano": int(year),
                "preco": float(price)
            })
        case "2":
            _id = input("Digite o ID do livro: ")
            book_manager.find_by_id(_id)
        case "3":
            _id = input("Digite o ID do livro: ")
            book_manager.delete_by_id(_id)
        case "4":
            _id = input("Digite o ID do livro: ")

            title = input("Digite o título do livro: ")
            author = input("Digite o nome do autor do livro: ")
            year = input("Digite o ano de lançamento: ")
            price = input("Digite o preço do livro: ")

            book_manager.update_by_id(_id, {
                "titulo": title,
                "autor": author,
                "ano": int(year),
                "preco": float(price)
            })
        case "5":
            print("Saindo do sistema")
            exit(0)
        case _:
            print("Opção inválida saindo do sistema")
            exit(0)

