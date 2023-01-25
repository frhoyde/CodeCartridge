#include <stdio.h>


int main(){
  long long int n, handshakeCount = 0;
  scanf("%lld", &n);
  for(long long int i = 1; i <= n; i++){
    handshakeCount += n - i;

  }
  printf("%lld\n", handshakeCount);
  return 0;
}
