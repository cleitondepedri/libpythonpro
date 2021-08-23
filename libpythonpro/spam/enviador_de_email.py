class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido: {remetente}')
        self.qde_email_enviados += 1
        return remetente


class EmailInvalido(Exception):
    pass
