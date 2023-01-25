// Problem Statement//www.hackerrank.com/contests/batch-2-course-2-lab-assignment-01/challenges/bablu-and-phone


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  int T, x, chargeNum;
  char c;
  scanf("%d", &T);
  while(T--){
    scanf("%d%c", &x, &c);
    if(x < 60){
      chargeNum = (60 - x) + 40 + 60;
    } else if (x < 80) {
      chargeNum = (80 - x) * 2 + 60;
    } else if( x >= 80 && x <= 100 ){
      chargeNum = (100 - x) * 3;
    }
    printf("%d", chargeNum);
    printf(" minutes\n");

  }

  return 0;
}
