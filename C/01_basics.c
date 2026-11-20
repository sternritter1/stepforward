#include <stdio.h>

int main(void) {
    // 1
    char name_initital = 'I';
    int age = 20;
    double height = 1.86;

    printf("Initial: %c, age: %d, height: %.2f m\n",name_initital,age,height);

    // 2

    printf("Char: %zu bytes\n", sizeof(char));
    printf("Int: %zu bytes\n", sizeof(int));
    printf("Double: %zu bytes\n", sizeof(double));

    // 3 

    int a = 17;
    int b = 5;
    
    printf("%d / %d = %d\n",a,b,(a / b));
    printf("%d %% %d = %d\n",a,b,(a % b));
    printf("Result: %.2f\n",(double)a / b);

    // 4

    double celsius = 36.6;
    double fahrenheit = celsius * 9 / 5 + 32;

    printf("%.1f C = %.1f F\n",celsius,fahrenheit);

    // 5

    int total_seconds = 7384;

    int hours = total_seconds / 3600;
    int minutes = total_seconds % 3600 / 60;
    int seconds = total_seconds % 3600 % 60;

    printf("%d s = %.02d:%.02d:%.02d\n",total_seconds,hours,minutes,seconds);

    return 0;
}