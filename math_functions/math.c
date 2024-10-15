// Fibonnaci sequence
int ifibo(int n)
{
    int a = 0, aux = 0, b = 1;
    for (int i = 0; i < n; i++)
    {
        aux = a;
        a += b;
        b = aux;
    }
    return a;
}

int rfibo(int n)
{
    if (n < 2)
    {
        return n;
    }
    return rfibo(n - 1) + rfibo(n - 2);
}

// Factorial
int ifactorial(int n)
{
    int result = 1;
    for (int i = 0; i < n; i++)
    {
        result *= i;
    }
    return result;
}

int rfactorial(int n)
{
    // caso base
    if (n < 2)
    {
        return 1;
    }
    // caso recursivo
    return n * rfactorial(n - 1);
}

// Sum
int isum(int *arr, int size)
{
    int sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    return sum;
}

int rsum(int *arr, int size)
{
    if (size == 0)
    {
        return 0;
    }
    return arr[0] + rsum(arr + 1, size - 1);
}

// Max and min
int compare_max(int num1, int num2)
{
    if (num1 > num2)
    {
        return num1;
    }
    else
    {
        return num2;
    }
}

int compare_min(int num1, int num2)
{
    if (num1 < num2)
    {
        return num1;
    }
    else
    {
        return num2;
    }
}

int iget_max(int *arr, int size)
{
    int ref = arr[0];
    for (int i = 0; i < size; i++)
    {
        if (arr[i] > ref)
        {
            ref = arr[i];
        }
    }
    return ref;
}

int rget_max(int *arr, int size)
{
    if (size == 0)
    {
        return arr[0];
    }
    return compare_max(arr[size - 1], rget_max(arr, size - 1));
}

int iget_min(int *arr, int size)
{
    int ref = arr[0];
    for (int i = 0; i < size; i++)
    {
        if (arr[i] < ref)
        {
            ref = arr[i];
        }
    }
    return ref;
}

int rget_min(int *arr, int size)
{
    if (size == 0)
    {
        return arr[0];
    }
    return compare_min(arr[size - 1], rget_max(arr, size - 1));
}
