class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def power(self):
        self.ligada = not self.ligada

    def subir_canal(self):
        if self.ligada:
            self.canal += 1
        else:
            print('Televisão desligada.')

    def descer_canal(self):
        if self.ligada:
            self.canal -= 1
        else:
            print('Televisão desligada.')


# Existem algumas situações em que queremos que nosso código seja executado apenas sob condições especiais,
# é o caso dos módulos principais. Só queremos que nossa função main() seja executada se o módulo for o principal.
# Caso ele tenha sido importado, a aplicação só deverá ser executada se main() for chamado explicitamente.
if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    televisao.power()
    print(televisao.ligada)
    televisao.subir_canal()
    televisao.subir_canal()
    print(televisao.canal)
    televisao.descer_canal()
    print(televisao.canal)
