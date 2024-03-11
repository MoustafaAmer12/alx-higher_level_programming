#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current;

	while (list != NULL)
	{
		current = list->next;
		while (current != NULL)
		{
			if (current == list)
				return 1;
			current = current->next;
		}
		list = list->next;
	}
	return 0;
}
