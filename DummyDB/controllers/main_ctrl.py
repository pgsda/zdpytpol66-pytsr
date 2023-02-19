from controllers.command_ctrl import CommandCtrl
from models.files_model import FilesModel

from views.main_view import MainView


class MainCtrl:
    def __init__(self):
        self.cctrl = CommandCtrl()
        self.fmodel = FilesModel()

    def run(self):
        while True:
            command = MainView.get_command()
            operation, doc, cols = self.cctrl.analyze_command(command)

            if operation == 'CD':
                self.fmodel.create_file(doc, cols)
            else:
                MainView.show_error_msg()

