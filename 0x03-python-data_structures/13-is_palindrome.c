#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *next;

	if (!head || !(*head) || !(*head)->next)
		return (1);

	slow = *head;
	fast = *head;
	prev = NULL;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast)
		slow = slow->next;

	while (prev && (prev->n == slow->n))
	{
		slow = slow->next;
		prev = prev->next;
	}

	return (!prev);
}
