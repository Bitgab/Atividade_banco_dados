from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
from models.usuario_models import Usuario
import os

os.system("cls || clear")

def main():
    # Criando a sessão com o banco de dados.
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        print("\nMenu:")
        print("\n1 - Adicionar usuário")
        print("\n2 - Pesquisar um usuário")
        print("\n3 - Atualizar dados de um usuário")
        print("\n4 - Excluir um usuário")
        print("\n5 - Exibir todos os usuários cadastrados")
        print("\n0 - Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Somente números.")
            continue

        match opcao: 
                case 1:
                    service.criar_usuario()
              
           
                case 2:
                    service.pesquisar_usuario()
              
           
                case 3:
                    service.atualizar_usuario()
              
           
                case 4: 
                    service.excluir_usuario()
              
           
                case 5:
                    print("Listar todos os  usuários.")
                    usuarios = service.listar_os_usuarios()
                    for usuario in usuarios:
                        print(f"ID: {usuario.id} \nNome: {usuario.nome} \nE-mail {usuario.email} \n Senha: {usuario.senha}")
           
                case 0: 
                    print("Finalizado")
                    break
           
                case _:
                    print("Opção inválida, escolha outro número.")

# Chama a função principal para iniciar o programa
if __name__ == "__main__":
    os.system("cls || clear")
    main()              
           
           
    

                        