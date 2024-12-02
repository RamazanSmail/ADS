#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> parents(20000);
vector<int> r(20000, 0); // rank

int find_parent(int value) {
    // cout << value << endl;

    // for(auto i : parents){
    //     cout << i << endl;
    // }

    if (parents[value] == -1)
        return value;
    return parents[value] = find_parent(parents[value]); // Path Compression
}

void union_sets(int a, int b) {
	a = find_parent (a);
	b = find_parent (b);
	if(a < b) swap(a, b);
	if (a != b)
		parents[b] = a;
}

int kruskals(vector<pair<int, pair<int, int>>>& edgeList){

    int totalWeight = 0;

    for(auto edge : edgeList){
        int weight = edge.first;
        int source = edge.second.first;
        int destination = edge.second.second;

        // cout << source << " " << destination << " " << weight << endl;

        if(find_parent(source) != find_parent(destination)){
            totalWeight += weight;
            // cout << "added!" << endl;
            union_sets(source, destination);
        }

        // cout << "looping...." << endl;
    }

    // cout << "Total weight is: " << totalWeight << endl;
    return totalWeight;
}

int main(){
    int n;
    cin >> n;

    vector<int> ducks(n);
    vector<pair<int, pair<int, int>>> edgeList; // weight, source, dest

    for(int i = 0; i < n; i++){
        cin >> ducks[i];
    }

    for(int i = 0; i < n; i++){
        int source = i;
        for(int j = 0; j < n; j++){
            int destination = j;
            int weight = ducks[i] + ducks[j];

            edgeList.push_back(make_pair(weight, make_pair(i, j)));
        }
    }

    sort(edgeList.begin(), edgeList.end());
    parents.resize(n);
    r.resize(n, 0);
    for (int i = 0; i < n; ++i) {
        parents[i] = -1;
    }

    int m = edgeList.size();
    // int totalWeight = 0;
    // for(int i = 0; i < m; i++){
    //     int weight = edgeList[i].first;
    //     int source = edgeList[i].second.first;
    //     int destination = edgeList[i].second.second;
    //     // find_parent(destination);

    //     // cout << "Source: " << source << "Destination" 

    //     if(find_parent(source) != find_parent(destination)){
    //         totalWeight += weight;
    //         union_sets(source, destination);
    //     }
    // }

    // cout << totalWeight;

    cout << kruskals(edgeList);
  
}