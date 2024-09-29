def process_queries(n, q, array, queries):
    results = []
    for query in queries:
        l1, r1, l2, r2 = query
        count = 0
        for element in array:
            if l1 <= element <= r1 or l2 <= element <= r2:
                count += 1
        results.append(count)
    return results


n, q = map(int, input().split())
array = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]


results = process_queries(n, q, array, queries)


for result in results:
    print(result)