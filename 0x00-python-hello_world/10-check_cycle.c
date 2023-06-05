#include "lists.h"

/**
 * 
*/
int check_cycle(listint_t *list)
{
    if (!list)
        return (0);

    while (list)
    {
        if (list->n == INT_MIN)
            return (1);
        
        list->n = INT_MIN;
        list = list->next;
    }

    return (0);
}
