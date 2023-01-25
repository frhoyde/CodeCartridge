#include <stdio.h>
#include <math.h>

int main() {
  int T, flag;
  scanf("%d", &T);
    int in;

  while(T--){
    flag = 1;
    scanf("%d", &in);
    if(in == 2 || in == 3){
      printf("Yes\n");
      continue;
    }
    if(in == 1){
      printf("No\n");
      continue;
    }
    for (int i = 2; i <= sqrt(in); i++) {
      if(in % i == 0){
        printf("No\n");
        flag = 0;
        break;
      }
    }
    if(flag){
      printf("Yes\n");
    }

  }
  return 0;
}
