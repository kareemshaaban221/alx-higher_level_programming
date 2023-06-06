#include "lists.h"

/**
 * 
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = NULL, *h = *head, *pre = NULL;
    short inserted = 0;

    if (!head)
        return (NULL);

    node = malloc(sizeof(listint_t));
    if (!node)
        return (NULL);
    
    node->n = number;
    
    while (h)
    {
        if (h->n < number)
        {
            pre = h;
            h = h->next;
        }
        else
        {
            node->next = h;
            if (pre)
                pre->next = node;
            inserted = 1;
            break;
        }
    }
    
    if (!inserted)
    {
        if (pre)
            pre->next = node;
        else
            *head = node;
        node->next = NULL;
        inserted = 1;
    }

    return (node);
}