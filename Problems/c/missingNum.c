#include <stdio.h>

int main(int argc, char *argv[]) {
  long long int n;
  int t;
  scanf("%d", &t);

  long long int sum, a, b, c;
  while(t--){
    scanf("%lld %lld %lld %lld", &sum, &a, &b, &c);

    printf("%lld\n", sum - (a+b+c));

  }


  return 0;
}
