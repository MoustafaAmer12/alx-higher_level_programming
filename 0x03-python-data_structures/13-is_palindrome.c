#include "lists.h"

/**
 * is_palindrome - recursive palindrome
 * @head: haed of list
 *
 * Return 1 if palindrome and 0 ow
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);
	return (palindrome(head, *head));
}
/**
 * palindrome - checks if palindrome or not
 * @head: head of linked list
 * @tail: tail of linked list
 *
 * Return: 1 if palindrome 0 ow
 */
int palindrome(listint_t **head, listint_t *tail)
{
	if (!tail)
		return (1);
	if (palindrome(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
