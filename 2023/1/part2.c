#include <stdio.h> 
#include <stdlib.h>
#include <stdbool.h>

#define MAX 100
#define ONE "one"
#define TWO "two"
#define THREE "three"
#define FOUR "four"
#define FIVE "five"
#define SIX "six"
#define SEVEN "seven"
#define EIGHT "eight"
#define NINE "nine"

FILE* file_ptr;

int getNumber(char buffer[]);
bool couldBePrintNumber(char c);
char getPrintNumber(char buffer[], int index);
bool checkNumber(char buffer[], int index, char* number);

int main() {
  char buffer[MAX];
  file_ptr = fopen("./2023/1/input.txt", "r");
  int sum = 0;

  if (file_ptr == NULL) {
      perror("Error opening file");
      return -1;
  }

  while (fgets(buffer, MAX, file_ptr) != NULL) {
    int n = getNumber(buffer);
    sum += n;
  }

  printf("Sum: %d\n", sum);

  return 0;
}

int getNumber(char buffer[]) {
  char numbers[100] = "";
  int i = 0;
  int j = 0;
  while (buffer[i] != '\0') {
    if (buffer[i] >= '0' && buffer[i] <= '9') {
      numbers[j] = buffer[i];
      j++;
    } else if (couldBePrintNumber(buffer[i])) {
      char number = getPrintNumber(buffer, i);
      if (number != '\0') {
        numbers[j] = number;
        j++;
      }
    }
    i++;
  }
  if (j == 0) {
    perror("No numbers found");
    return -1;
  } else {
    char nString[3] = "";
    nString[0] = numbers[0];
    nString[1] = numbers[j-1];
    nString[2] = '\0';
    printf("Number: %s %c %c %s\n", numbers, nString[0], nString[1], nString);
    return atoi(nString);
  }
}

bool couldBePrintNumber(char c) {
  return c == 'o' || c == 't' || c == 'f' || c == 's' || c == 'e' || c == 'n';
}

char getPrintNumber(char buffer[], int index) {
  char number = '\0';
  if (checkNumber(buffer, index, ONE)) {
    return '1';
  } else if (checkNumber(buffer, index, TWO)) {
    return '2';
  } else if (checkNumber(buffer, index, THREE)) {
    return '3';
  } else if (checkNumber(buffer, index, FOUR)) {
    return '4';
  } else if (checkNumber(buffer, index, FIVE)) {
    return '5';
  } else if (checkNumber(buffer, index, SIX)) {
    return '6';
  } else if (checkNumber(buffer, index, SEVEN)) {
    return '7';
  } else if (checkNumber(buffer, index, EIGHT)) {
    return '8';
  } else if (checkNumber(buffer, index, NINE)) {
    return '9';
  }
  return '\0';
}

bool checkNumber(char buffer[], int index, char* number) {
  int i = 0;
  int j = 0;
  while (buffer[index + i] != '\0' && number[j] != '\0') {
    if (buffer[index + i] != number[j]) {
      return false;
    }
    i++;
    j++;
  }
  return true;
}