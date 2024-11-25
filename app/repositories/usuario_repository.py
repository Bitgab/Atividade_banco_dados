from models.usuario_models import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()    

    def criar_usario(self, usuario: Usuario):
        # Criando um usuário.
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def atualizar_usuario(self,usuario: Usuario):
        # Atualizando usuário.
        self.session.commit()
        self.session.refresh(usuario)     

    def pesquisar_usuario_por_email(self, email: str):
        # pesquisando usuário.
        return self.session.query(Usuario).filter_by(email = email).first()

    def excluir_usuario(self, usuario):
        # Excluindo usuário.
        self.session.delete(usuario)
        self.session.commit()

    def listar_os_usuarios(self):
        # Listando todos os usuário.
        return self.session.query(Usuario).all()