#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

vector<int> parents(20000);

int find_parent(int vertex){
    if(parents[vertex] == -1){
        return vertex;
    }
    return parents[vertex] = find_parent(parents[vertex]); // Path Compression
}

void union_sets(int a, int b){
    a = find_parent(a);
    b = find_parent(b);

    if(a < b) swap(a, b);

    if(a != b){
        parents[b] = a;
    }
}

int kruskals(vector<pair<int, pair<int, int>>>& edgeList){
    int totalWeight = 0;

    for(auto edge : edgeList){
        int weight = edge.first;
        int source = edge.second.first;
        int destination = edge.second.second;

        if(find_parent(source) != find_parent(destination)){
            totalWeight += weight;
            union_sets(source, destination);
        }
    }

    return totalWeight;
}

int main(){
    int n;
    cin >> n;
    // set<pair<int, int>> connected;
    vector<pair<int, pair<int, int>>> edgeList;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            int temp;
            cin >> temp;
            // pair<int, int> edge = make_pair(i, j);
            // auto it = find(connected.begin(), connected.end(), edge);
            if(j >= i + 1 && j != i){ // обратываем ток верхнюю часть матрицы, потому что в андайректед графе матрица симметрична
                                        // а i != j потому что избавляемся от вертексов которые указывают на самого себя
                edgeList.push_back(make_pair(temp, make_pair(i, j)));
                // connected.insert(make_pair(i, j));
                // connected.insert(make_pair(j, i));
            }
        }
    }

    sort(edgeList.begin(), edgeList.end());
    parents.resize(n);
    // r.resize(n, 0);
    for (int i = 0; i < n; ++i) {
        parents[i] = -1;
    }

    cout << kruskals(edgeList);
}