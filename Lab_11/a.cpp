#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> parent(200000);

int find_parent(int v) {
    return (v == parent[v]) ? v : (parent[v] = find_parent(parent[v]));
}

void union_sets(int a, int b) {
    a = find_parent(a);
    b = find_parent(b);
    if (a != b)
        parent[a] = b;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<pair<int, pair<int, int>>> edges;
    for (int i = 0; i < m; i++) {
        int l, r, c;
        cin >> l >> r >> c;
        edges.push_back({c, {l-1, r-1}});
    }

    sort(edges.begin(), edges.end());

    parent.resize(n);
    for (int i = 0; i < n; i++) parent[i] = i;

    long long total_cost = 0;
    for (int i = 0; i < edges.size(); i++) {
        int a = edges[i].second.first, b = edges[i].second.second, l = edges[i].first;
        for (int j = a; j < b, a <= b; j++, ++a)
            if (find_parent(j) != find_parent(a)) {
                total_cost += l;
                union_sets(j, a);
            }
            else {
                j = parent[a];
                a = j;
                j--;
            }
    }
    cout << total_cost;

    return 0;
}