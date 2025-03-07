#include <stdbool.h>
#include <stdio.h>

bool isPalindrome(int x);

int main() {
  printf("%d \n", isPalindrome(22));    // Output: 1 (true)
  printf("%d \n", isPalindrome(-2565)); // Output: 0 (false)
  printf("%d \n", isPalindrome(121));   // Output: 1 (true)
  printf("%d \n", isPalindrome(10));    // Output: 0 (false)

  return 0;
}

bool isPalindrome(int x) {
  // Un nombre négatif ou un multiple de 10 (sauf 0) ne peut pas être un
  // palindrome
  if (x < 0 || (x % 10 == 0 && x != 0)) {
    return false;
  }

  int check = 0;
  while (x > check) {
    check = check * 10 + x % 10; // Ajoute le dernier chiffre de x à check
    x /= 10;                     // Réduit x en supprimant le dernier chiffre
  }

  // Compare la moitié originale et l'inversée
  return (x == check || x == check / 10);
}

