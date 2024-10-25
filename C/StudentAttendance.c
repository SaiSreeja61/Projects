#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char stuName[20][30];
int presentAttendance[20] = {0};
int absentAttendance[20] = {0};
int indexNumber = 0;

void checkAttendance() {
    int i;
    printf("\nTotal Present | Total Absent\n");
    for (i = 0; i < indexNumber; i++) {
        printf("%s\t%d\t%d\n", stuName[i], presentAttendance[i], absentAttendance[i]);
    }
}

void addStudent() {
    int i, num, add;
    if (indexNumber == 0) {
        printf("Enter how many students you want to add: ");
        scanf("%d", &num);
        getchar(); 
        for (i = 0; i < num; i++) {
            printf("\nEnter %d student name to add in attendance register: ", i + 1);
            fgets(stuName[i], 30, stdin);
            size_t len = strlen(stuName[i]);
            if (len > 0 && stuName[i][len-1] == '\n') {
                stuName[i][len-1] = '\0';
            }
            indexNumber++;
        }
    } else {
        printf("Enter how many students you want to add: ");
        scanf("%d", &num);
        getchar(); 
        add = indexNumber + num;
        for (i = indexNumber; i < add; i++) {
            printf("\nEnter %d student name to add in attendance register: ", i + 1);
            fgets(stuName[i], 30, stdin);
            size_t len = strlen(stuName[i]);
            if (len > 0 && stuName[i][len-1] == '\n') {
                stuName[i][len-1] = '\0';
            }
            indexNumber++;
        }
    }
}

void removeStudent() {
    char name[30];
    printf("Enter student name to remove: ");
    getchar(); 
    fgets(name, 30, stdin);
    size_t len = strlen(name);
    if (len > 0 && name[len-1] == '\n') {
        name[len-1] = '\0';
    }
    for (int i = 0; i < indexNumber; i++) {
        if (strcmp(name, stuName[i]) == 0) {
            for (int j = i; j < indexNumber - 1; j++) {
                strcpy(stuName[j], stuName[j + 1]);
                presentAttendance[j] = presentAttendance[j + 1];
                absentAttendance[j] = absentAttendance[j + 1];
            }
            indexNumber--;
            printf("\n%s student is removed\n", name);
            break;
        } else if (i == indexNumber - 1) {
            printf("This name does not exist\n");
        }
    }
}

void takeAttendance() {
    int i;
    char ch;
    printf("\nEnter Y for present and N for absent\n");
    for (i = 0; i < indexNumber; i++) {
    repeate:
        printf("%d. %s is present: ", i + 1, stuName[i]);
        fflush(stdin);
        scanf("%c", &ch);
        if (ch == 'Y' || ch == 'y') {
            presentAttendance[i] += 1;
        } else if (ch == 'N' || ch == 'n') {
            absentAttendance[i] += 1;
        } else {
            printf("Invalid character. Try again\n");
            goto repeate;
        }
        getchar();
    }
}

int main() {
    int choose;
    do {
        printf("\n********** Main Menu **********\n");
        printf("Enter 1 to add student\n");
        printf("Enter 2 to take attendance\n");
        printf("Enter 3 to check attendance\n");
        printf("Enter 4 to remove student\n");
        printf("Enter 5 to exit\n");
        printf("Please choose any menu: ");
        fflush(stdin);
        scanf("%d", &choose);

        switch (choose) {
            case 1:
                addStudent();
                break;
            case 2:
                takeAttendance();
                break;
            case 3:
                checkAttendance();
                break;
            case 4:
                removeStudent();
                break;
            case 5:
                exit(0);
                break;
            default:
                printf("Invalid choice! Please choose a valid option.\n");
        }
    } while (choose != 5);

    return 0;
}
