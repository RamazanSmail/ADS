#include <iostream>
#include <vector>

using namespace std;

vector<int> parents(20000);

int find_parent(int vertex){
    // cout << "searching...." << endl;
    if(parents[vertex] == -1){
        return vertex;
    }
    return parents[vertex] = find_parent(parents[vertex]); // Path Compression
}

void union_sets(int a, int b){
    a = find_parent(a);
    b = find_parent(b);

    if(a != b){
        parents[a] = b;
    }
}

int main(){
    int n, m;
    cin >> n >> m;

    vector<vector<int>> adjList(n);

    for(int i = 0; i < m; i++){
        int v, u;
        cin >> v >> u;
        if(v > u) swap(v, u);
        v--;
        u--;
        adjList[v].push_back(u);
    }

    parents.resize(n);
    // r.resize(n, 0);
    for (int i = 0; i < n; ++i) {
        parents[i] = -1;
    }

    vector<int> res;
    int connectedComponents = 0;
    res.push_back(connectedComponents);
    for(int vertex = n - 1; vertex >= 0; vertex--){
        // cout << "Connected components: " << connectedComponents << endl;
        bool removed = false;
        for(int j = 0; j < adjList[vertex].size(); j++){
            int neighbor = adjList[vertex][j];
            if(find_parent(vertex) != find_parent(neighbor)){
                // cout << "removing" << endl;
                removed = true;
                int oldParent = find_parent(vertex);
                union_sets(vertex, neighbor);
                if(oldParent != find_parent(vertex) && oldParent != vertex){
                    connectedComponents--;
                }
            }
        }   
        if(!removed){
            connectedComponents++;
            // cout << "did not remove" << endl;
        }
        res.push_back(connectedComponents);
    }

    for(int i = res.size() - 2; i >= 0; i--){
        cout << res[i] << endl;
    }
}