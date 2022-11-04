#include <stdio.h>

int main(int argc, char *argv[]) {

  int n;
  scanf("%d", &n);
  int arr[n], maxMarks = 0;
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
    maxMarks = maxMarks < arr[i]? arr[i]: maxMarks;
  }
  for (int i = 0; i < n; i++) {
    printf("%d ", maxMarks - arr[i]);
  }
  printf("\n");

  return 0;
}
