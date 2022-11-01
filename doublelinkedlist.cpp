#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct DLinkedList
{
  int value;
  DLinkedList *next, *prev;
};

DLinkedList *HEAD_DLL, *TAIL_DLL = NULL;

DLinkedList *createDLinkedList(int value)
{
  DLinkedList *newDLinkedList = (DLinkedList *)malloc(sizeof(DLinkedList)); // allocate memory for new DLinkedList
  newDLinkedList->value = value;                                            // initialize the value of the DLinkedList to the parameter
  newDLinkedList->next = newDLinkedList->prev = NULL;                       // by default, newDLinkedList->next and newDLinkedList->prev will be NULL
  return newDLinkedList;                                                    // return the newly created DLinkedList
}

void pushHeadDLL(int value)
{                                               // insert DLinkedList at the beginning of the LL
  DLinkedList *temp = createDLinkedList(value); // create the new DLinkedList

  if (!HEAD_DLL)
  {                             // if head is NULL (LL is empty)
    HEAD_DLL = TAIL_DLL = temp; // this DLinkedList will be the first and last DLinkedList in LL
  }
  else
  {                        // if LL has >= 1 DLinkedList
    HEAD_DLL->prev = temp; // set previous of head to temp (temp <- head)
    temp->next = HEAD_DLL; // set next of temp to head (temp -><- head)
    HEAD_DLL = temp;       // temp will be the new head (first element in LL)
  }
}

void pushTailDLL(int value)
{                                               // insert node at the end of the LL
  DLinkedList *temp = createDLinkedList(value); // create the new node

  if (!HEAD_DLL)
  {                             // if head is NULL (LL is empty)
    HEAD_DLL = TAIL_DLL = temp; // this node will be the first and last node in LL
  }
  else
  {                        // if LL has >= 1 node
    TAIL_DLL->next = temp; // set next of tail to temp (temp <- tail)
    temp->prev = TAIL_DLL; // set prev of temp to tail (temp -><- tail)
    TAIL_DLL = temp;       // temp will be the new tail (last element in LL)
  }
}

void pushMidDLL(int value)
{
  if (!HEAD_DLL)
  {
    DLinkedList *temp = createDLinkedList(value); // create the new node
    HEAD_DLL = TAIL_DLL = temp;                   // this node will be the first and last node in LL
  }
  else if (value <= HEAD_DLL->value)
  {                     // if value is the smallest,
    pushHeadDLL(value); // add to the left
  }
  else if (value >= TAIL_DLL->value)
  {                     // if value is the largest,
    pushTailDLL(value); // add to the right
  }
  else
  {
    DLinkedList *newDLinkedList = createDLinkedList(value); // create the new node
    DLinkedList *curr = HEAD_DLL;                           // we will set curr to become one node behind newDLinkedList

    while (curr->value <= value)
    {                    // We will traverse until condition is FALSE
      curr = curr->next; // traverse until curr->value > value
    }

    newDLinkedList->prev = curr->prev;
    newDLinkedList->next = curr;
    curr->prev->next = newDLinkedList;
    curr->prev = newDLinkedList;
  }
}

void popHeadDLL()
{
  if (!HEAD_DLL)
  {
    printf("Double Linked List Empty\n");
  }
  else if (HEAD_DLL == TAIL_DLL)
  {
    free(HEAD_DLL);
    HEAD_DLL = NULL;
  }
  else
  {
    DLinkedList *lastHead = HEAD_DLL;
    lastHead->next->prev = NULL;
    HEAD_DLL = lastHead->next;
    free(lastHead);
    lastHead = NULL;
  }
}

void popTailDLL()
{
  if (!HEAD_DLL)
  {
    printf("Double Linked List Empty\n");
  }
  else if (HEAD_DLL == TAIL_DLL)
  {
    free(HEAD_DLL);
    HEAD_DLL = NULL;
  }
  else
  {
    DLinkedList *lastTail = TAIL_DLL;
    lastTail->prev->next = NULL;
    TAIL_DLL = lastTail->prev;
    free(lastTail);
    lastTail = NULL;
  }
}

void viewDLL()
{
  DLinkedList *curr = HEAD_DLL;
  while (curr)
  {
    printf("%d -> ", curr->value);
    curr = curr->next;
  }
  printf("\n\n[press enter]");
  getchar();
}

void doublelinkedlist()
{
  cls();
  puts("1. Push Head");
  puts("2. Push Tail");
  puts("3. Push Mid");
  puts("4. Pop Head");
  puts("5. Pop Tail");
  int opt = safeInput();
  switch (opt)
  {
  case 1:
  {
    printf("Input Value : ");
    int val = safeInput();
    pushHeadDLL(val);
    break;
  }
  case 2:
  {
    printf("Input Value : ");
    int val = safeInput();
    pushTailDLL(val);
    break;
  }
  case 3:
  {
    printf("Input Value : ");
    int val = safeInput();
    pushMidDLL(val);
    break;
  }
  case 4:
    popHeadDLL();
    break;
  case 5:
    popTailDLL();
    break;
  }
  viewDLL();
  doublelinkedlist();
}