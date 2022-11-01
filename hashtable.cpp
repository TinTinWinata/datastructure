#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Hashtable
{
  char name[255];
};

const int MAX_SIZE = 26;
Hashtable *HASH_ARRAY[MAX_SIZE];

Hashtable *createHashtable(char name[])
{
  Hashtable *newHashtable = (Hashtable *)malloc(sizeof(Hashtable));
  strcpy(newHashtable->name, name);
  return newHashtable;
}

int hashFunction(char str[])
{
  char character = str[0];
  if (character >= 65 && character <= 90)
  {
    return character - 65;
  }
  else
  {
    return character - 97;
  }
}

bool searchHash(char str[])
{
  int hashIdx = hashFunction(str);
  int currIdx = hashIdx;
  do
  {
    if (strcmp(str, HASH_ARRAY[currIdx]->name) == 0)
    {
      // Kalau ketemu return true
      return true;
    }
    currIdx = (currIdx + 1) % MAX_SIZE;
  } while (hashIdx != currIdx);
  return false;
}

void popHash(char str[])
{
  int hashIdx = hashFunction(str);
  int currIdx = hashIdx;
  do
  {
    // Validasi
    if (strcmp(HASH_ARRAY[currIdx]->name, str) == 0)
    {
      free(HASH_ARRAY[currIdx]);
      HASH_ARRAY[currIdx] = NULL;
    }
    currIdx = (currIdx + 1) % MAX_SIZE;
  } while (currIdx != hashIdx);
}

void insertHash(char str[])
{
  // Hashing index from function
  int idx = hashFunction(str);
  if (!HASH_ARRAY[idx])
  {
    // If null we will create new
    HASH_ARRAY[idx] = createHashtable(str);
  }
  else
  {
    // Akan terjadi collision
    // 1. Linear Probing
    printf("\nCollision Detected\n\n");

    int currIdx = idx + 1;
    while (HASH_ARRAY[currIdx])
    {
      if (currIdx == idx)
      {
        printf("Hash Table Is Full!\n\n");
        return;
      }
      currIdx = (currIdx + 1) % MAX_SIZE;
      // Kalau kosong dia akan taro di tempat ini
    }
    HASH_ARRAY[currIdx] = createHashtable(str);
  }
}

void printHashTable()
{
  for (int i = 0; i < MAX_SIZE; i++)
  {
    printf("[%d] %s\n", i, HASH_ARRAY[i]->name);
  }
}

int main()
{
  insertHash("Zebra");
  printHashTable();
  if (searchHash("asd"))
  {
    printf("FOUND");
  }
  else
  {
    printf("NOT FOUND");
  }
}