#!/user/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gtk

class Handler():
	"""
	- Mettre tous les signaux dans une seule classe
	- NB: Dans PyGi les argements des méthodes sont des widgets intermédiaires qui héritent toutes les caractéristiques 
	  des widgets d'origine. Ceci dit, si on essaye de donner une action à un widget de type "button" nommé "button1"
	  dans la partie du code on écrit: def action(self, intermerdiare):
	  intermerdiare hérite toutes les caractéristiques de button1 et l'action sur intermerdiare est une action indirecte sur button1
	  Ceci est peut être bien expliqué en C/GTK+ vu que PyGi est en quelques sorte un porjet réecrit depuis C/GTK+.
	- Ps: Lors d'une utilisation avancée de PyGi, les signaux jouent un rôle primordial dans la création de notre Gui.
	     C'est pourquoi une maîtrise de l'utilisation des signaux est fortement récommendée et, aussi, la modification du ficher XML
	     généré par Glade3 est, aussi, récommendée.

	- Dans cet exemple, notre programme principale n'est pas mis dans une classe à part, vu sa simplicité. Mais, dans un programme
	     avancé, une bonne maîtrise de Python et de PyGi est nécessaire.
	     Glade3 ne permet que réduire le temps de création de Gui et éviter la création de l'interface à la main.
	     Cependant, ceci ne veut pas dire qu'on va oublier les manipulations manuelles pour parvenir aux résultas voulus.

	- Documentation sur Github:
	 
	    1- Toutes les méthodes Gtk.methodes (exemple: Gtk.main_quit())
	     http://lazka.github.io/pgi-docs/#Gtk-3.0/functions.html

	    2- Les méthodes supportées par Gtk.Button() {Comment interéagir avec les widgets de type Gtk.Button()}
	     http://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Button.html#Gtk.Button

	    3- Les méthodes supportées par Gtk.Entry() {Comment interéagir avec les widgets de type Gtk.Entry()}
	     http://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Entry.html#Gtk.Entry

	    4- Les méthodes supportées par Gtk.Switch() {Comment interéagir avec les widgets de type Gtk.Switch()}
	     http://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Switch.html#Gtk.Switch

	    5- Les méthodes supportées par Gtk.ComboBoxText() {Comment interéagir avec les widgets de type Gtk.ComboBoxText()}
	     http://lazka.github.io/pgi-docs/#Gtk-3.0/classes/ComboBoxText.html#Gtk.ComboBoxText

	    6- Les méthodes supportées par Gtk.ToggleButton() {Comment interéagir avec les widgets de type Gtk.ToggleButton()}
	     http://lazka.github.io/pgi-docs/#Gtk-3.0/classes/ToggleButton.html#Gtk.ToggleButton

	    7- Les méthodes supportées par Gtk.SearchEntry() {Comment interéagir avec les widgets de type Gtk.SearchEntry()}
	     http://lazka.github.io/pgi-docs/#RB-3.0/classes/SearchEntry.html#RB.SearchEntry 

	 - Pour plus d'informations: http://lazka.github.io/pgi-docs/

	"""

	def on_button(self, button):
		"""
		- Gtk.main_quit(): Est une fonction par défaut de PyGi
		          qui permet de sortir de la boucle infinie de l'interface en Gtk+ en utilisant Python 
		- La méthode utilise le mot "self" et "button" comme arguments
		- "button" joue le rôle d'un widget intermédiaire entre button1 et cette partie de code
		"""
		Gtk.main_quit()

	def on_switch_activate(self, switch, args):
		"""
		- "switch" est un widget intermédiaire entre "switch1" et cette partie de code
		       et args est l'argument passé à la méthode lors de l'appel de widget "switch1"
		- switch.get_active() : Cette méthode retourne "True" ou "False" 
		    => "True" = Le bouton (widget) est actif / "False" = Le bouton (widget) est inactif 

		"""
		if switch.get_active():
			# Bouton actif
			print("Switch activé!")
		else:
			# L'inverse 
			print("Switch désactivé!")

	def on_comboboxtext(self, combobox):
		"""
		- L'ajout des éléments à ComboBoxText est faite sous Glade3
		- Cette méthode affichera uniquement les noms stockés dans le fichier XML générée par Glade3
		- combobox.get_active_text() : Retourne le text activé de widget ComboBoxText lors de la saisie dans l'interface UI 
		     Le type de retour est une chaine de caractaire (String) et l'affiche sera sous la terminale
		"""
		# On vérifie si combobox est vide ou non.
		# S'il est vide, il n'y aura aucun affichage sinon on affiche le contenu

		if combobox.get_active_text() != None:
			print("L'élément saisi est: " + combobox.get_active_text())

	def on_toggle(self, toggle):
		"""
		- Le bouton "toggle1" affiche sur la terminale "Toggle button est activé!" ou "Toggle button est désactivé"
		- toggle.get_active() : Retourne "True" ou "False" et qui permet de vérifier l'état de widget (activé ou non)
		- L'affiche est sous la terminale
		"""
		if toggle.get_active():
			print("Toggle button est activé!")
		else: 
			print("Toggle button est désactivé")

	def on_entry_activate(self, entry):
		"""
		- Affichage du text saisi dans "entry1" et "seachentry1"
		- entry est un widget intermédiaire entre "entry1" et "seachentry1" 
		- entry.get_text(): Retourne le text entré dans "entry1" et "seachentry1"
		- L'affiche sera sur la terminale
		"""
		txt = entry.get_text()
		print(txt)


#builder est de type Gtk.Builder() : Notre constructeur du fichier XML de Glade
builder = Gtk.Builder()

# Ajouter le chemin de fichier d'interface générée par Glade
builder.add_from_file("test.glade")  

# Tous les signaus sont mis dans une classe nommée Handler()
builder.connect_signals(Handler()) 

# window est un objet qui hérite toutes les méthodes de window1
window = builder.get_object("window1") 

# Affichage de la fenêtre window = Affichage de la fenêtre window1
window.show_all()   

# Lier la fenêtre principale à un signal de destruction de la fenêtre
window.connect("delete-event",Gtk.main_quit)  

# Lancer la boucle infinie qui permettera de visualiser l'interface indéfiniment sauf s'il y aura une intervention
# de l'utilisateur ou du programme interne 
Gtk.main()  