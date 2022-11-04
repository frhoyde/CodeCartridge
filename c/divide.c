#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  int n;
  scanf("%d", &n);
  int arr[n];
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }
  int k;
  scanf("%d", &k);
  int boys[n - k];
  for (int i = k, j = 0; i < n && j < n - k; i++, j++) {
    boys[j] = arr[i];
  }
  for (int i = 0; i < n - k; i++) {
    printf("%d ", boys[i]);
  }
  for (int i = 0; i < k; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
  return 0;
}
