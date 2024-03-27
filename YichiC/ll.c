#include <string.h>
#include <stdio.h>
#include <stdlib.h>


struct Node {
    // static
    char type[10];     // 8 byte : type is an array of 10 char pointer
    
    // dynamic
    void* data;         // 8 byte : data is a no type pointer
    
    // dynamic
    struct Node* next;  // 8 byte : 
} node;

struct Node* newNode() {
    return (struct Node*) malloc(sizeof(struct Node));
}

struct Node* pushFront(struct Node** head, int value) {

    struct Node* nn = newNode();
    
    strcpy(nn->type, "int");
    nn->data = (char*) malloc(sizeof(int));
    nn->data = value;
    nn->next = *head;

    *head = nn;
}

void print_ll(struct Node* head) {
    struct Node* curr = head;

    while (curr != NULL) {
        printf("iaushdiuahisdhiuahisu\n");
        if (strcmp(head->type, "string") == 0) {
            printf("%s -> ", (char *)curr->data);
        } else if (strcmp(head->type, "int") == 0) {
            printf("%d -> ", (char *)curr->data);
        } else if (strcmp(head->type, "float") == 0) {
            printf("%f -> ", (char *)curr->data);
        }
        curr = curr->next;
    }
}

void free_ll(struct Node* head) {
    struct Node* curr = head;
    struct Node* prev = NULL;

    while (curr != NULL) {
        printf("%s\n", curr->data);
        if (prev != NULL) {
            free(prev); // free 前一个节点
        }

        free(curr->data); // free 内容

        if (curr->next) prev = curr->next;
        curr = curr->next;
    }

    // 处理掉最后一个节点
    if (prev != NULL) {
        free(prev); // free 前一个节点
    }
}

int main() {

    struct Node** ll_list = (struct Node**) malloc(sizeof (struct Node*) * 5);
    char* int_list = (char*) malloc(sizeof(char) * 5);

    // singly linked list
    const char* strlist[3] = {"happy dog", "happy cat", "sad dog"};
    struct Node* head = NULL;
    struct Node* tail = head;

    for (int i = 0; i < 1; ++i) {
        if (head == NULL) {
            ll_list[0] = newNode();

            strcpy(head->type, "string");
            head->data = (char*) malloc(sizeof(char) * (strlen(strlist[i]) + 1));
            strcpy(head->data, strlist[i]);

            tail = head;
        } else {
            tail->next = newNode();

            strcpy(tail->next->type, "string");
            
            tail->next->data = (char*) malloc(sizeof(char) * (strlen(strlist[i]) + 1));
            strcpy(tail->next->data, strlist[i]);

            tail = tail->next;
        }
    }

    //pushFront(&head, 10);

    print_ll(head);

    free_ll(head);

    return 0;
}