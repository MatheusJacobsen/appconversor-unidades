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
