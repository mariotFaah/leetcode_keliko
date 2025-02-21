def two_sum(nums, target):
    i = 0
    while i < len(nums):  # Parcours des éléments
        j = i + 1
        while j < len(nums):  # Comparaison avec les autres éléments
            if nums[i] + nums[j] == target:
                return [i, j]  # On retourne les indices si la somme est correcte
            j += 1  # On avance dans la liste
        i += 1  # On passe à l'élément suivant
    return []  # Si aucune paire n'est trouvée


# Test
print(two_sum([2, 7, 11, 15], 9))  # Résultat attendu : [0, 1]

