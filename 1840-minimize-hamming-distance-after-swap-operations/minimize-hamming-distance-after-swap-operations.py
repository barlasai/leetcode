from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        parent = list(range(len(source)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Build components
        for a, b in allowedSwaps:
            union(a, b)

        # Step 2: Group indices
        groups = defaultdict(list)
        for i in range(len(source)):
            groups[find(i)].append(i)

        # Step 3 & 4: Count mismatches
        hamming = 0

        for indices in groups.values():
            count = Counter(source[i] for i in indices)

            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    hamming += 1

        return hamming