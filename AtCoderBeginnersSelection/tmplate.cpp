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

    // 複数入力
    int N;
    cin >> N;

    // 複数の数字を配列（固定長）arrに
    int arr[N];
    for(int i=0;i<N;i++) cin >> arr[i];

    for(int num: arr){
        cout << num << " ";
    }

    // 複数の数字をベクトル（可変長）vecに
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

