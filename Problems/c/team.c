#include <stdio.h>

int main(int argc, char *argv[]) {
  int n, k, run;
  scanf("%d %d", &n, &k);

  int count = 0;
  for (int i = 0; i < n; i++) {
    scanf("%d", &run);
    run < k? count++: 0;
  }
  printf("%d\n", count);

  return 0;
}
