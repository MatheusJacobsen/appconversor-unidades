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

        self.combo.set_activate(0)

        self.builder.connect_signals(self)

        self.window.show()

    def on_window_destroy(self, widget):
        '''Classical Window Close Button'''
        Gtk.main_quit()

    def on_button_clicked(self, button):
        '''Do something...'''
        print("Gostaria de converter massa? Digite 1.")
        print("Gostaria de converter volume? Digite 2.")

    def on_combo_changed(self, widget):
        '''Verify which option was selected'''
        model = widget.get_model()
        active = widget.get_active()
        if active >= 0:
            code = model[active][0]
            print('Opção selecionada: {}'.format(code))
        else:
            print('Sem opção.')


if _name_ == '_main_':
    try:
        gui = TheApp()
        Gtk.main()
    except KeyboardInterrupt:
        pass
