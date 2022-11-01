#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Node
{
  char name[255];
  Node *next;
  Node *prev;
};

const int MAX_SIZE = 26;

Node *HEADS[MAX_SIZE];
Node *TAILS[MAX_SIZE];

Node *createNode(char name[])
{
  Node *newNode = (Node *)malloc(sizeof(Node));
  strcpy(newNode->name, name);
  return newNode;
};

int hashFunction(char name[])
{
  char initial = name[0];
  if (initial >= 65 && initial <= 90)
  {
    return initial - 65;
  }
  else
  {
    return initial - 97;
  }
}

void insert(char name[])
{
  int hashIdx = hashFunction(name);

  Node *newNode = createNode(name);
  // Push Head apa bila tidak ada
  if (!HEADS[hashIdx])
  {
    HEADS[hashIdx] = TAILS[hashIdx] = newNode;
  }
  else
  {
    Node *lastTail = TAILS[hashIdx];
    TAILS[hashIdx]->next = newNode;
    TAILS[hashIdx] = newNode;
    newNode->prev = lastTail;
  }
}

void print()
{
  for (int i = 0; i < MAX_SIZE; i++)
  {
    printf("[%d] ", i);
    Node *curr = HEADS[i];
    while (curr)
    {
      printf("%s -> ", curr->name);
      curr = curr->next;
    }
    printf("\n");
  }
}

bool search(char name[])
{
  int hashIdx = hashFunction(name);
  Node *curr = HEADS[hashIdx];
  while (curr)
  {
    if (strcmp(curr->name, name) == 0)
      return true;
  }
  return false;
}

void pop(char name[])
{
  // REMOVE MEMILIKI 4 KONDISI
  int hashIdx = hashFunction(name);

  // NAMA KETEMU DAN HANYA ADA 1 DATA
  if (strcmp(HEADS[hashIdx]->name, name) == 0 && HEADS[hashIdx] == TAILS[hashIdx])
  {
    free(HEADS[hashIdx]);
    HEADS[hashIdx] = TAILS[hashIdx] = NULL;
  }
  // NAMA KETEMU TETAPI ADA DI HEAD
  else if (strcmp(HEADS[hashIdx]->name, name) == 0)
  {
    Node *lastHead = HEADS[hashIdx];
    HEADS[hashIdx] = HEADS[hashIdx]->next;
    HEADS[hashIdx]->prev = NULL;
    free(lastHead);
  }
  // NAMA KETEMU TETAPI ADA DI TAILS
  else if (strcmp(TAILS[hashIdx]->name, name) == 0)
  {
    Node *lastTail = TAILS[hashIdx];
    TAILS[hashIdx] = TAILS[hashIdx]->prev;
    TAILS[hashIdx]->next = NULL;
    free(lastTail);
  }
  // NAMA KETEMU TETAPI ADA DI TENGAH
  else
  {
    Node *curr = HEADS[hashIdx];
    while (curr)
    {
      if (strcmp(curr->name, name) == 0)
      {
        // Pop Mid
        curr->prev->next = curr->next;
        curr->next->prev = curr->prev;
        free(curr);
      }
      curr = curr->next;
    }
    printf("Name not found");
    return;
  }
}

int main()
{
  insert("Josafat");
  insert("Justine");
  insert("Jason");
  insert("TinTin");
  insert("Cindy");
  pop("Cindy");
  pop("Justine");
  print();
}