#include <stdbool.h>
#include <stdio.h>
bool isPalindrome(int x);

int main() {
  printf("%d \n", isPalindrome(22));
  printf("%d ", isPalindrome(-2565));

  return 0;
}

bool isPalindrome(int x) {
  if (x < 0 || x % 10 == 0 && x != 0) {
    return false;
  }
  int check = 0;
  while (x > check) {
    check = check * 10 + x % 10;
    x /= 10;
  }
  return (x == check || x == check / 10);
}
