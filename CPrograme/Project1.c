#include <stdio.h>
int main() {
  int userAccessLevel = 0;
  if (userAccessLevel ==1) {
    printf("Acess Grante : Root privileges active.\n");
  }else if (userAccessLevel ==2){
    printf("Acess Grante : standerd user");
  }else {
    printf("Acess Denied :unknow user");
  }
  return 0;
}