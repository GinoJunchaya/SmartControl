from controller.GeneralController import GeneralController

class Application:
    ''' Clase correspondiente a la aplicación '''

    def __init__(self):
        ''' Crea un objeto correspondiente al usuario que inició
            la aplicación
        '''
        pass

    @staticmethod
    def salir():
        ''' Método estatico para finalizar el programa '''
        exit()

    def iniciar(self):
        ''' Método que crea el controlador pasandole el usuario e inicia
            la vista
        '''
        controlador = GeneralController(Application.salir)
        controlador.iniciarVista()
        pass

if __name__ == "__main__":
    app = Application()
    app.iniciar()