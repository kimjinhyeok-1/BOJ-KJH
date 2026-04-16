#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef long long ll;

const int MAX = 45000; // sqrt(2 * 10^9) 보다 조금 더 크게 설정
int mu[MAX + 1];

// 뫼비우스 함수 전처리
void sieve() {
    fill(mu, mu + MAX + 1, 0);
    mu[1] = 1;
    for (int i = 1; i <= MAX; i++) {
        for (int j = 2 * i; j <= MAX; j += i) {
            mu[j] -= mu[i];
        }
    }
}

// X 이하의 제곱 ㄴㄴ 수의 개수를 계산하는 함수
ll count_square_free(ll x) {
    ll count = 0;
    for (ll i = 1; i * i <= x; i++) {
        count += (ll)mu[i] * (x / (i * i));
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int k;
    cin >> k;

    sieve();

    // 이분 탐색을 통해 K번째 제곱 ㄴㄴ 수를 찾음
    ll low = 1, high = 2000000000; // K=10억일 때 결과값은 약 16억대
    ll ans = high;

    while (low <= high) {
        ll mid = low + (high - low) / 2;
        if (count_square_free(mid) >= k) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << endl;

    return 0;
}