#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// 50,000자 / 64비트 = 약 782개 워드
typedef unsigned long long uint64;
const int MAX_WORDS = 800;

uint64 S[26][MAX_WORDS];
uint64 V[MAX_WORDS];

int main() {
    // 입출력 최적화
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string A, B;
    if (!(cin >> A >> B)) return 0;

    int N = A.length();
    int M = B.length();
    int words = (N + 63) >> 6;

    // 1. 문자열 A의 각 문자 위치를 비트셋에 기록
    for (int i = 0; i < N; i++) {
        S[A[i] - 'A'][i >> 6] |= (1ULL << (i & 63));
    }

    // 2. 문자열 B를 순회하며 비트 병렬 LCS 계산
    for (int i = 0; i < M; i++) {
        int char_idx = B[i] - 'A';
        uint64 shift_in = 1;
        uint64 borrow = 0;

        for (int j = 0; j < words; j++) {
            uint64 X = V[j] | S[char_idx][j];
            uint64 W = (V[j] << 1) | shift_in;
            shift_in = V[j] >> 63;

            // 큰 수의 뺄셈 (Borrow 처리)
            uint64 sub = X - (W + borrow);
            
            // Borrow 발생 조건 판별
            if (X < W || (X == W && borrow)) borrow = 1;
            else if (X - W < borrow) borrow = 1;
            else borrow = 0;

            // 행(Row) 업데이트
            V[j] = X & (X ^ sub);
        }
    }

    // 3. 최종 비트의 개수(LCS 길이) 계산
    int ans = 0;
    for (int i = 0; i < words; i++) {
        ans += __builtin_popcountll(V[i]);
    }

    cout << ans << endl;

    return 0;
}