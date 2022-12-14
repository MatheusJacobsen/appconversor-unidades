# App para Conversão de Unidades
# Unidades - volume e massa
# SEL0456 - Desenvolvimento de Software para Sistemas Embarcados com Sistemas Operacionais
# Matheus Marques Jacobsen - 10312403

# GTK Import

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from os.path import abspath, dirname, join

class TheApp:
    '''The Application Class.'''

    def __init__(self):
        # Build GUI
        self.builder = Gtk.Builder()
        self.builder.add_from_file('combo_units.glade')

         # Get objects
        self.window = self.builder.get_object('window')
        self.window.set_title('Conversor de Unidades - Massa e Volume')

        # Array de 4 colunas com a primeira sendo ID e as outras as unidades e quantidades
        self.quantities_list = Gtk.ListStore(int, str)
        self.mass_units_list = Gtk.ListStore(int, str)
        self.volume_units_list = Gtk.ListStore(int, str)

        # Interface
        quantities = [
            [1, 'Massa'],
            [2, 'Volume']]

        for qty in quantities:
            self.quantities_list.append(qty)

        mass_units = [
            [1, 'Kilos (kg)'],
            [2, 'Libras (lb)'],
            [3, 'Onça (oz)']
        ]

        volume_units = [
            [1, 'Milímetros Cúbicos (mm³)'],
            [2, 'Centímetros Cúbicos (cm³)'],
            [3, 'Litros (l)']]

        for unity in mass_units:
            self.mass_units_list.append(unity)

        for unity in volume_units:
            self.volume_units_list.append(unity)

        # Associando a array (ListStore) ao ComboBox
        self.combo1 = self.builder.get_object('combo_1')
        self.combo1.set_model(self.quantities_list)

        self.unity_from = self.builder.get_object('combo_origin')
        self.unity_to = self.builder.get_object('combo_end')
        self.unity_from.set_model(self.mass_units_list)
        self.unity_to.set_model(self.mass_units_list)

        # Renbder de texto ao ComboBox
        renderer_text = Gtk.CellRendererText()
        self.combo1.pack_start(renderer_text, True)
        self.unity_from.pack_start(renderer_text, True)
        self.unity_to.pack_start(renderer_text, True)

        # Coluna a ser mostrada
        self.combo1.add_attribute(renderer_text, "text", 1)
        self.unity_from.add_attribute(renderer_text, "text", 1)
        self.unity_to.add_attribute(renderer_text, "text", 1)

        # Opção ativa default
        self.combo1.set_active(0)

        # Connect signals
        self.builder.connect_signals(self)

        # Everything is ready
        self.window.show()

    def on_window_destroy(self, widget):
        '''Classical window close button.'''
        Gtk.main_quit()

        def on_combo_1_changed(self, widget):
        '''Verify which option is selected'''
        model = widget.get_model()
        active = widget.get_active()
        option = model[active][1]
        print('Opção selecionada: {}'.format(option))
        if active == 0:
            self.unity_from.set_model(self.mass_units_list)
        if active == 1:
            self.unity_from.set_model(self.volume_units_list)