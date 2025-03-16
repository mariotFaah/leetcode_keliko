def infos_etudiant(nom, prenom, *args, **kwargs):
    print(f"Nom : {nom}")
    print(f"Prénom : {prenom}")

    # Affichage des notes
    if args:
        print(f"Notes : {args}")
        moyenne = sum(args) / len(args)
        print(f"Moyenne : {moyenne:.2f}")
    else:
        print("Aucune note fournie.")

    # Affichage des informations supplémentaires
    if kwargs:
        print("Informations supplémentaires :")
        for cle, valeur in kwargs.items():
            print(f"  {cle} : {valeur}")


# Test
infos_etudiant("Randria", "Tiana", 15, 18, 12, 14, filiere="Informatique", annee=2)

