#include <bits/stdc++.h>
using namespace std;

int main(){
    // 1行に１要素の場合
    int a;
    cin >> a;
    cout << a << endl;

    // 1行にスペース区切りで複数要素の場合
    // 固定長の場合
    int A,B;
    cin >> A >> B;
    cout << A << B << endl;

    // 複数の数字をベクトル（可変調）vecに
    int N;
    cin >> N;
    vector<int> vec(N);

    // ベクトルを１要素ごとに改行して出力
    for(auto v: vec){
        cout << v << endl;
    }

    // ベクトルを１要素ごとに空白区切りで出力
    for(auto v: vec){
        cout << v << " ";
    }
}

