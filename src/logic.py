class SessaoDeEstudo:
    def __init__(self, nome, duracao_minutos):
        if not nome:
            raise ValueError("O nome da tarefa não pode estar vazio.")
        if duracao_minutos <= 0:
            raise ValueError("A duração deve ser positiva.")

        self.nome = nome
        self.duracao_minutos = duracao_minutos * 60
        self.completada = False

    def get_duracao_string(self, segundos):
        minutos, segundos = divmod(segundos, 60)
        return f"{minutos:02d}:{segundos:02d}"