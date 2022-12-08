# App para Conversão de Unidades
# Unidades - volume e massa
# SEL0456 - Desenvolvimento de Software para Sistemas Embarcados com Sistemas Operacionais
# Matheus Marques Jacobsen - 10312403


# GTK Import

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="Bem vindo ao App: Conversor de Unidades")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()

# Exemplo de aula

class TheApp:
    '''The Application Class'''

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('combo_units.glade')

        # Get Objects
        self.window = self.builder.get_object('window')
        self.liststore = Gtk.ListStore(float,float)

        units_mass = [
            ['#ID:1', 'Opção 1','Kilogram'],
            ['#ID:2', 'Opção 2', 'Oz'],
            ['#ID:3', 'Opção 3','Pounds']]

        for unit in units_mass:
            self.liststore.append(unit)

        self.combo = self.builder.get_object('combo')
        self.combo.set_model(self.liststore)

        renderer_text = Gtk.CellRendererText()
        self.combo.pack_start(renderer_text, True)

        self.combo.add_attribute(renderer_text, "text", 3)

