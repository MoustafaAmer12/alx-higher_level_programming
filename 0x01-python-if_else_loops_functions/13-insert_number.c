#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to the first element of the list
 * @number: number to be added to the list
 *
 * Return: address of the new node or Null if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *to_add = malloc(sizeof(listint_t));

	if (!to_add)
		return (NULL);
	to_add->n = number;
	to_add->next = NULL;

	if (!node || to_add->n < node->next->n)
	{
		to_add->next = node;
		return (*head = to_add);
	}
	while (node)
	{
		if (!node->next || to_add->n < node->next->n)
		{
			to_add->next = node->next;
			node->next = to_add;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
