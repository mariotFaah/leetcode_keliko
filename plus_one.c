#include <stdio.h>
#include <stdlib.h>

int *plusOne(int *digits, int digitsSize, int *returnSize) {
  // On commence par parcourir l'array de droite à gauche
  for (int i = digitsSize - 1; i >= 0; i--) {
    // Si le chiffre est inférieur à 9, on l'incrémente et on termine
    if (digits[i] < 9) {
      digits[i]++;
      *returnSize = digitsSize; // Pas besoin de changer la taille
      return digits;
    }
    // Si le chiffre est 9, on le met à 0 et on continue avec le chiffre suivant
    digits[i] = 0;
  }

  // Si tous les chiffres étaient des 9, on doit allouer un nouvel array
  *returnSize = digitsSize + 1;
  int *result = (int *)malloc(*returnSize * sizeof(int));

  // Le premier chiffre devient 1 et tous les autres sont 0
  result[0] = 1;
  for (int i = 1; i < *returnSize; i++) {
    result[i] = 0;
  }

  return result;
}

int main() {
  // Exemple d'utilisation
  int digits[] = {9, 9, 9};
  int digitsSize = sizeof(digits) / sizeof(digits[0]);
  int returnSize;

  int *result = plusOne(digits, digitsSize, &returnSize);

  // Affichage du résultat
  for (int i = 0; i < returnSize; i++) {
    printf("%d ", result[i]);
  }
  printf("\n");

  // Libération de la mémoire
  free(result);

  return 0;
}
