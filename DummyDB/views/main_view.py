class MainView:
    @staticmethod
    def get_command():
        return input(">>->> ")

    @staticmethod
    def show_error_msg():
        print('Nieprawidłowa komenda')
