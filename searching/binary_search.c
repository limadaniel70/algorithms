int binary_search(int *arr, int size, int num)
{
    int start = 0;
    int end = size - 1;
    while (start <= end)
    {
        int mid = (start + end) / 2;
        int guess = arr[mid];
        if (guess == num)
        {
            return mid;
        }
        else if (guess > num)
        {
            start = mid - 1;
        }
        else
        {
            end = mid + 1;
        }
    }
    return 1;
}