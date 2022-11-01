#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <conio.h>
#include "config.h"
#include "linkedlist.cpp"

void menu()
{
  puts("1. Linked List (Without Tail)");
  puts("2. Double Linked List");
  puts("3. Hash Table");
  puts("4. Binary Search Tree");
  printf(">> ");
  int opt = safeInput();
  switch (opt)
  {
  case 1:
    linkedlist();
    break;
  }
}

int main()
{
  cls();
  menu();
}