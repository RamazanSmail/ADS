#include <iostream>

using namespace std;

int adjMAtrix[500][500];
int added[500];
int ans[500];
bool used[500];
bool work[500];

void floydWarshall(int n) {
    int i, j, k;
    for (k = 0; k < n; k++) {
        int across = added[k];
        used[across] = true;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                adjMAtrix[i][j] = min(adjMAtrix[i][j], adjMAtrix[i][across] + adjMAtrix[across][j]);
            }
        }
        for (int i = 0; i < n; i++) {
            work[i] = used[i];
        }
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                if (!work[i] || !work[j] || i == j)
                    continue;
                ans[k] = max(adjMAtrix[i][j], ans[k]);
            }
        }
    }
}

int main() {
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> adjMAtrix[i][j];
        }
    }
    for (int i = 0; i < n; i++) {
        cin >> added[i];
        added[i]--;
    }
    floydWarshall(n);
    for (int i = 0; i < n; i++) {
        cout << ans[i] << '\n';
    }
}
