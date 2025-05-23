#include <iostream>
#include <vector>
using namespace std;
using ll = long long;
struct PriorityQueue {
    vector<ll> heap;

    ll parent(ll i) { return (i - 1) / 2; }
    ll left(ll i) { return (2*i + 1); }
    ll right(ll i) { return (2*i + 2); }
    
    void heapifyUp(ll i) {
        ll p = parent(i);
        if (i != 0 && heap[i] < heap[p]) {
            swap(heap[i], heap[p]);
            heapifyUp(p);
        }
    }

    void heapifyDown(ll i) {
        ll l = left(i);
        ll r = right(i);
        ll min = i;
        ll size = heap.size();
        if (l < size && heap[min] > heap[l]) min = l;
        if (r < size && heap[min] > heap[r]) min = r;
        if (min != i) {
            swap(heap[i], heap[min]);
            heapifyDown(min);
        }
    }

    ll GetSize() {
        return heap.size();
    }

    bool isEmpty() {
        return heap.empty();
    }

    void push(ll x) {
        heap.push_back(x);
        heapifyUp(heap.size() - 1);
    }

    void pop() {
        if (isEmpty()) return;
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);
    }

    ll top() {
        if (!isEmpty()) return heap.front();
    }
};

int main() {
    ll n, m; cin >> n >> m;
    PriorityQueue pq;
    for (ll i = 0; i < n; i++) {
        ll x; cin >> x;
        pq.push(x);
    }
    ll cnt = 0;
    while(pq.top() <= m ) {
        if (pq.GetSize() < 2) {
            cout << -1; return 0;
        }
        ll least = pq.top(); pq.pop();
        ll secondleast = pq.top(); pq.pop();
        pq.push(least + 2 * secondleast);
        cnt++;
    }
    cout << cnt;
    return 0;
}