    result = [];
    for query in queries: 
        arr = [string for string in strings if string == query]
        result.append(len(arr))
    return result