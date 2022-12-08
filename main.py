# App para Conversão de Unidades
# Unidades - volume e massa
# SEL0456 - Desenvolvimento de Software para Sistemas Embarcados com Sistemas Operacionais
# Matheus Marques Jacobsen - 10312403


# GTK Import

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="Hello World")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()

# Exemplo de aula

class TheApp:
    '''The Application Class'''

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('units.glade')

        # Get Objects
        self.window = self.builder.get_object('window')
        self.liststore = Gtk.ListStore(str,str)

        colors = [
            ['#ID:1', 'Opção 1'],
            ['#ID:2', 'Opção 2'],
            ['#ID:3', 'Opção 3']]

        for color in colors:
            self.liststore.append(color)

        self.combo = self.builder.get_object('combo')
        self.combo.set_model(self.liststore)

        renderer_text = Gtk.CellRendererText()
        self.combo.pack_start(renderer_text, True)

        self.combo.add_attribute(renderer_text, "text", 1)

        