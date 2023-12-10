#include <stdio.h> 
#include <stdlib.h>

#define MAX 100

FILE* file_ptr;

int getNumber(char buffer[]);

int main() {
  char buffer[MAX];
  file_ptr = fopen("./2023/1/input.txt", "r");
  int sum = 0;

  if (file_ptr == NULL) {
      perror("Error opening file");
      return -1;
  }

  while (fgets(buffer, MAX, file_ptr) != NULL) {
    sum += getNumber(buffer);
  }

  printf("Sum: %d\n", sum);

  return 0;
}

int getNumber(char buffer[]) {
  char numbers[100];
  int i = 0;
  int j = 0;
  while (buffer[i] != '\0') {
    if (buffer[i] >= '0' && buffer[i] <= '9') {
      numbers[j] = buffer[i];
      j++;
    }
    i++;
  }
  if (j == 0) {
    perror("No numbers found");
    return -1;
  } else {
    char number[2];
    number[0] = numbers[0];
    number[1] = numbers[j-1];
    return atoi(number);
  }
}