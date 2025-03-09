#include <stdio.h>

int mySqrt(int x) {
  if (x < 0) {
    printf("%d should be a positive number\n", x);
    return -1; // Indique une erreur
  }

  int low = 1, high = x, ans = 0;
  while (low <= high) {
    long long mid = low + (high - low) / 2;
    long long val = mid * mid;
    if (val <= x) {
      ans = mid;
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return ans;
}

int main() {

  int racine = 16;
  printf("%d \n", mySqrt(racine));
  return 0;
}
