#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  int n;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    for (int j = i; j > 0; j--) {
      printf("%d ", j);
    }
    printf("\n");

  }

  return 0;
}
