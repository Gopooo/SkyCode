import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json
import pyperclip

# Charger les données à partir du fichier JSON
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Fonction pour afficher l'ID et la variante lorsque le bouton est cliqué
def afficher_id_variant():
    nom_recherche = nom_entry.get()
    trouve = False
    for item in data:
        if item["Name"] == nom_recherche:
            id_trouve = item["Id"]
            variant_trouve = item["Variant"]
            trouve = True
            break

    if trouve:
        id_hex = hex(id_trouve)[2:].zfill(3).upper()
        variant_hex = hex(variant_trouve)[2:].zfill(4).upper()
        result = f"T0{id_hex}{variant_hex}"
        result_label.config(text=result)
    else:
        result_label.config(text="Nom non trouvé dans les données.")

# Fonction pour copier le résultat dans le presse-papiers
def copier_resultat():
    result = result_label.cget("text")
    if result:
        pyperclip.copy(result)

# Fonction pour mettre à jour la liste des suggestions d'autocomplétion
def mettre_a_jour_suggestions():
    nom_partiel = nom_entry.get().lower()
    suggestions = [item["Name"] for item in data if item["Name"].lower().startswith(nom_partiel)]
    nom_entry['values'] = suggestions

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Interface Visuelle")

# Charger une image
image = Image.open("BORNE8.png")
photo = ImageTk.PhotoImage(image)

# Afficher l'image dans un label
image_label = ttk.Label(root, image=photo)
image_label.pack()

# Créer un champ de texte pour entrer le nom
nom_label = ttk.Label(root, text="Entrez le nom :")
nom_label.pack()

# Utiliser un champ de texte avec autocomplétion
nom_entry = ttk.Combobox(root, postcommand=mettre_a_jour_suggestions)
nom_entry.pack()

# Créer un bouton pour afficher l'ID et la variante
afficher_button = ttk.Button(root, text="Afficher ID et Variant", command=afficher_id_variant)
afficher_button.pack()

# Créer un bouton pour copier le résultat
copier_button = ttk.Button(root, text="Copier le Résultat", command=copier_resultat)
copier_button.pack()

# Créer un label pour afficher le résultat
result_label = ttk.Label(root, text="")
result_label.pack()

# Démarrer la boucle Tkinter
root.mainloop()
