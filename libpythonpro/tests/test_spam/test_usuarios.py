from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Cleiton', email='cleyton_depedri@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)




def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Cleiton', email='cleyton_depedri@hotmail.com'),
        Usuario(nome='Felipe', email='cleitondepedri@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

