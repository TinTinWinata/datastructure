#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <conio.h>

struct LinkedList
{
  int value;
  LinkedList *next;
};

LinkedList *HEAD = NULL;

LinkedList *createLinkedList(int value)
{
  LinkedList *newLinkedList = (LinkedList *)malloc(sizeof(LinkedList));
  newLinkedList->value = value;
  newLinkedList->next = NULL;
  return newLinkedList;
}

void pushHeadLL(int value)
{

  LinkedList *newLinkedList = createLinkedList(value);
  if (!HEAD)
  {
    HEAD = newLinkedList;
  }
  else
  {
    // Just change the head with the new one
    newLinkedList->next = HEAD;
    HEAD = newLinkedList;
  }
}

void pushTailLL(int value)
{
  LinkedList *newLinkedList = createLinkedList(value);

  // Validate if there's are no head available
  // Then new linked list will be the new head
  if (!HEAD)
  {
    HEAD = newLinkedList;
  }
  // If there's already head in the linkedlist
  else
  {
    LinkedList *curr = HEAD;

    // Search the last node(curr)
    while (curr->next)
    {
      curr = curr->next;
    }

    // Pointing last head to new node
    curr->next = newLinkedList;
  }
}

void popHeadLL()
{
  // Check the availablity of Linked List
  if (!HEAD)
  {
    printf("There's are no more Linked List!");
    return;
  }
  // Save the last head pointer
  LinkedList *lastHead = HEAD;

  // Validate if there's only 1 node in linkedlist
  // Then head will be null
  // If there's more than one node, then change head
  // with the next pointer curr

  if (lastHead->next != NULL)
    HEAD = lastHead->next;
  else
    HEAD = NULL;

  free(lastHead);
  lastHead = NULL;
}

void popTailLL()
{
  // Check Availability of Linked List
  if (!HEAD)
  {
    printf("There's are no more Linked List!");
    return;
  }
  // If there's only one node (head only)
  else if (!HEAD->next)
  {
    free(HEAD);
    HEAD = NULL;
  }
  // Node more then one
  else
  {
    LinkedList *curr = HEAD;
    // Find last 2 before last

    while (curr)
    {
      // Last Node
      if (curr->next->next == NULL)
      {
        LinkedList *last = curr->next;
        curr->next = NULL;
        free(last);
        last = NULL;
        return;
      }
      curr = curr->next;
    }
  }
}

void popMidLL(int val)
{
  // Check Availability of Linked List
  if (!HEAD)
  {
    printf("There's are no more Linked List!");
    return;
  }
  // Validate if only one head
  else if (!HEAD->next && HEAD->value == val)
  {
    popHeadLL();
    printf("Found! Deleting ...");
    return;
  }
  else
  {
    LinkedList *curr = HEAD;
    while (curr->next)
    {
      // If the same value is last node (then pop tail)
      if (curr->next->next == NULL && curr->next->value == val)
      {
        popTailLL();
        printf("Found! Deleting ...");
        return;
      }
      if (curr->next->value == val && curr->next->next != NULL)
      {
        // If next node is the value and at the center of node
        LinkedList *toBeDeleted = curr->next;
        curr->next = curr->next->next;
        free(toBeDeleted);
        toBeDeleted = NULL;
        printf("Found! Deleting ...");
        return;
      }
      curr = curr->next;
    }
  }
}

void updateLL(int val, int newVal)
{
  // Check Availability of Linked List
  if (!HEAD)
  {
    printf("There's are no more Linked List!");
    return;
  }
  LinkedList *curr = HEAD;
  while (curr)
  {
    if (curr->value == val)
    {
      curr->value = newVal;
      printf("Linked List Updated!");
      return;
    }
    curr = curr->next;
  }
  printf("Not Found!");
}

void viewLL()
{
  LinkedList *curr = HEAD;
  while (curr)
  {
    printf("%d -> ", curr->value);
    curr = curr->next;
  }
  printf("\n\n[press enter]");
  getchar();
}

void afterActionLL()
{
  cls();
  viewLL();
}

void linkedlist()
{
  cls();
  puts("1. Push Head");
  puts("2. Push Tail");
  puts("3. Pop Head");
  puts("4. Pop Tail");
  puts("5. Pop Mid");
  puts("6. Update");
  int opt = safeInput();
  switch (opt)
  {
  case 1:
  {

    printf("Input value : ");
    int val = safeInput();
    pushHeadLL(val);
    break;
  }
  case 2:
  {
    printf("Input value : ");
    int val = safeInput();
    pushTailLL(val);
    break;
  }
  case 3:
    popHeadLL();
    break;
  case 4:
    popTailLL();
    break;
  case 5:
  {
    printf("Input value : ");
    int val = safeInput();
    popMidLL(val);
    break;
  }
  case 6:
    printf("Update value for : ");
    int updtVal = safeInput();
    printf("New value : ");
    int newVal = safeInput();
    updateLL(updtVal, newVal);
    break;
  }
  afterActionLL();
  linkedlist();
}