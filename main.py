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

#