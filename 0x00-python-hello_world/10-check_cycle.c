#include "lists.h"
/**
 * check_cycle - checks if a single list has a cycle
 * @list: pointer to the firs telement of the SLL
 *
 * Return: 0 if has no cycle and if it has
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *current_2 = list;

	while (current_2 != NULL && current_2->next)
	{
		current = current->next;
		current_2 = current_2->next->next;
		if (current_2 == current_2)
			return (1);
	}
	return (0);
}
