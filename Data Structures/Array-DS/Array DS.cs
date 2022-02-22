public static List<int> reverseArray(List<int> a)
    {
        int size = a.Count();
        int aux = 0;
        for (int i = 0; i < size / 2; i++)
        {
            aux = a[size - i - 1];
            a[size - i - 1] = a[i]; 
            a[i] = aux;
        }
        
        return a;
    }