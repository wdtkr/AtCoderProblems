#include <bits/stdc++.h>
using namespace std;

int main(){
    // 固定長の場合
    int N,Q;
    cin >> N >> Q;

    string str;
    cin >> str;
    int t,x;
    int num = 0;
    for(int i=0;i<Q;i++){
        cin >> t >> x;
        switch (t){
            case 1:
                num += x;
                break;
            case 2:
                // cout << num << endl;
                if((x-1) - num%N < 0){
                    cout << str[N + ((x-1) - num%N)]<< endl;
                }else{
                    cout << str[(x-1) - num%N]<< endl;
                }
                // ((x-num)%N+N)%N
                break;
        }
    }
}
