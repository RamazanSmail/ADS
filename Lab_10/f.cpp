#include <iostream>
#include <vector>

using namespace std;

class UnionFind {
private:
    vector<int> parent, rank;
    
public:
    UnionFind(int size) {
        parent.resize(size + 1);
        rank.resize(size + 1, 0);
        for (int i = 1; i <= size; ++i) {
            parent[i] = i;
        }
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

int main() {
    int n, m;
    cin >> n >> m;
    
    UnionFind uf(n);
    
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        uf.unionSets(x, y);
    }
    
    int s, f;
    cin >> s >> f;
    
    if (uf.find(s) == uf.find(f)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    
    return 0;
}

