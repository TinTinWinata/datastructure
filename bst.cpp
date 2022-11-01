
// Binary Search Tree BST

// Insert
// print/traverse tree inOrder, preOrder, postOrder
// pop

#include <stdio.h>
#include <stdlib.h> //malloc.h

struct Node
{
	int value;
	Node *left, *right;
};

Node *createNewNode(int value)
{
	Node *newNode = (Node *)malloc(sizeof(Node));
	newNode->value = value;
	newNode->left = newNode->right = NULL;
	return newNode;
}

// rekursif -> memanggil diri sendiri hingga suatu
// kondisi terpenuhi / mencapai base case

Node *insertNewNode(Node *curr, int value)
{

	// jika kosong/ketemu null
	if (curr == NULL)
	{
		return createNewNode(value);
	}

	// jika curr tidak null
	if (value > curr->value)
	{
		curr->right = insertNewNode(curr->right, value);
	}
	else if (value < curr->value)
	{
		curr->left = insertNewNode(curr->left, value);
	}

	return curr;
}

Node *inOrder(Node *curr)
{
	if (curr != NULL)
	{
		inOrder(curr->left);
		printf("%d ", curr->value);
		inOrder(curr->right);
	}
}

Node *preOrder(Node *curr)
{
	if (curr != NULL)
	{
		printf("%d ", curr->value);
		preOrder(curr->left);
		preOrder(curr->right);
	}
}

Node *postOrder(Node *curr)
{
	if (curr)
	{
		postOrder(curr->left);
		postOrder(curr->right);
		printf("%d ", curr->value);
	}
}

Node *anakKiriPalingBesar(Node *curr)
{
	Node *temp = curr;
	while (temp->right != NULL)
	{
		temp = temp->right;
	}
	return temp;
}

Node *popNode(Node *curr, int value)
{
	// base case
	if (curr == NULL)
	{
		return curr;
	}

	// ke kiri dan ke kanan berdasarkan nilai value
	if (value < curr->value)
	{
		curr->left = popNode(curr->left, value);
	}
	else if (value > curr->value)
	{
		curr->right = popNode(curr->right, value);
	}
	else
	{
		// jika value == curr->value

		// punya satu child saja
		// ada child yaitu dikanan
		if (curr->left == NULL && curr->right != NULL)
		{
			Node *temp = curr->left;
			free(curr);
			return temp;
		}

		// ada child yaitu dikiri
		else if (curr->right == NULL && curr->left != NULL)
		{
			Node *temp = curr->right;
			free(curr);
			return temp;
		}
		else if (curr->right == NULL && curr->left == NULL)
		{
			free(curr);
			return NULL;
		}
		else
		{
			// jika ada 2 children node
			Node *temp = anakKiriPalingBesar(curr->left);
			curr->value = temp->value;
			curr->left = popNode(curr->left, temp->value);
		}
	}
	return curr;
}

bool search(Node *root, int val)
{
	if (!root)
	{
		return false;
	}
	else if (root->value < val)
	{
		return search(root->right, val);
	}
	else if (root->value > val)
	{
		return search(root->left, val);
	}
	else if (root->value == val)
	{
		return true;
	}
	return false;
}

Node *update(Node *root, int val, int newVal)
{
	if (search(root, val))
	{
		root = popNode(root, val);
		root = insertNewNode(root, newVal);
	}
	else
	{
		printf("Value not found!");
		getchar();
	}
	return root;
}

Node *popAll(Node *root)
{
	if (root)
	{
		popAll(root->left);
		popAll(root->right);

		free(root);
		root = NULL;
	}
	return root;
}

int main()
{
	Node *root = NULL;

	root = insertNewNode(root, 22);
	root = insertNewNode(root, 10);
	root = insertNewNode(root, 7);
	root = popAll(root);

	printf("inOrder\n");
	inOrder(root);

	puts("\n");

	printf("preOrder\n");
	preOrder(root);

	puts("\n"); // printf() -> \n

	printf("postOrder\n");
	postOrder(root);

	puts("\n");

	return 0;
}

// memasukkan data ke bst dan berhasil mentraverse
