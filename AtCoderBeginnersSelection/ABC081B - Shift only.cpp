#include <bits/stdc++.h>
using namespace std;

int main(){
    // 1行に１要素の場合
    int N;
    cin >> N;
    int count = 0;

    int arr[N];
    for(int i=0;i<N;i++) cin >> arr[i];

    while(true){
        for(int i=0;i<N;i++){
            if(arr[i]%2 == 0){
                arr[i] = arr[i]/2;
            }else{
                cout << count << endl;
                return 0;
            }
        }
        count++;
    }
}