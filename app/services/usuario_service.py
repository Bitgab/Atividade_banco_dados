from models.usuario_models import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self):
        # Função criar usuário
        try:
            nome = input("Digite seu nome: ")
            email = input("Digite seu e-mail: ")
            senha = input("Digite seu senha: ")
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastro = self.repository.pesquisar_usuario_por_email(email=usuario.email)
            if cadastro:
                print("Usuário cadastrado com sucesso.")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuario criado com sucesso")
        except TypeError as erro:
            print(f"Erro ao salvar o arquivo: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def excluir_usuario(self):
        # Função para excluir usuário
        try:
            email = input("Digite o email do usuário que deseja excluir: ")

            cadastro = self.repository.pesquisar_usuario_por_email(email)
            if cadastro:
                self.repository.excluir_usuario(cadastro)
                print("Usuário excluido com sucesso")
                return
           
            print("Usuário não encontrado")
        except TypeError as erro:
            print(f"Erro ao deletar o arquivo: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def atualizar_usuario(self):
        try:
            email = input("Digite o e-mail que deseja alterar: ")

            cadastro = self.repository.pesquisar_usuario_por_email(email)
            if cadastro:
                cadastro.nome = input("Digite o novo nome: ")
                cadastro.email = input("Digite o novo e-mail: ")
                cadastro.senha = input("Digite a nova senha: ")
                
                self.repository.atualizar_usuario(cadastro)
                print("Usuário atualizado com sucesso")
                return
            
            print("Usuário não encontrado")
        except TypeError as erro:
            print(f"Erro ao deletar o arquivo: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def pesquisar_usuario(self):
        try:
            email = input("Digite o e-mail do usuário que deseja pesquisar: ")

            cadastro = self.repository.pesquisar_usuario_por_email(email)
            if cadastro:
                print("Dados do usuário: ")
                print(f"\n Id: {cadastro.id} | Nome: {cadastro.nome} | Email: {cadastro.email}")
                return
            
            print("Usuário não encontrado.")
        except TypeError as erro:
            print(f"Erro ao excluir o arquivo: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")


    def listar_os_usuarios(self):
        return self.repository.listar_os_usuarios()