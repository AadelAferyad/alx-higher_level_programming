#include "lists.h"
/**
 * check_cycle - search for a cycle in the linked list.
 * @list: pointer to head of list.
 * Return: return 0 if there is no cycle otherwise 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *c = NULL, *n = NULL;

	if (!list || !(list->next))
		return (0);
	c = list;
	n = list->next;
	while (n && n->next)
	{
		if (c == n)
			return (1);
		c = c->next;
		n = (n->next)->next;
	}
	return (0);
}
