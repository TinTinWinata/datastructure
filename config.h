#include <stdlib.h>
#include <stdio.h>

void cls()
{
  system("cls");
}

int safeInput()
{
  int inp;
  scanf("%d", &inp);
  getchar();
  return inp;
}