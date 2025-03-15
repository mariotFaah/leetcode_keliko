# Ecrire une fonction qui affiche toutes les differentes combinaiso de deux nombres entre 0 et 99

# cela donne quelque chose comme ca 
# 00 01, 00 02, 00 03 , ... , 00 99, 01 02 , ... 98 99

def ft_print_com2():
    i = 0
    while i<99:
        i+= 1
        x = 0
        while x < 99:
            print(i, x)
            x +=1
            
        
        
ft_print_com2()

