#include "lists.h"
/**
 * check_cycle-checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL || list->next == NULL)
		return (0);
	slow =list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
