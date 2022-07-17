// バンダイナムコスタジオ インターン選考問題

/*
座席管理クラスを作成してください。
*/

// includeは必要に応じて追加/削除していただいて大丈夫です。
#include <iostream>
#include <list>
#include <algorithm>

// 最初から用意されているクラス名やメソッド名は変更しないでください
// メソッドやメンバ変数等は自由に追加していただいて大丈夫ですが、このファイルのみで完結させる必要があります。
class SEAT
{
public:
    std::list<int> seat_ls{0,0,0,0,0,0,0,0,0,0};
    // コンストラクタです
    SEAT()
    {
        // TODO
        // 実装してください
        seat_ls = {0,0,0,0,0,0,0,0,0,0};
        
    }

    // デストラクタです
    ~SEAT()
    {
        // 必要に応じて実装してください
    }

    // お客様の来店時に呼ばれるメソッドです
    // nはお客様の人数です。現在5名様以上の来店はご遠慮いただいておりますので、n には1～4の値が来ます。
    // 戻り値には、人数分連続して空いている、一番若いカウンター番号を返してください。
    // 人数分連続した席の確保が出来なければ-1を返してください。
    // (例)
    // 0123456789 <- カウンター番号
    // ....oo.... <- . 空き / o 使用中
    // の時に allocate(4) が呼ばれた場合 0を返してください。 6は一番若いという条件を満たしていません。
    // (例)
    // 0123456789 <- カウンター番号
    // o..oooo.o. <- . 空き / o 使用中
    // の時に allocate(4) が呼ばれた場合 -1を返してください
    int allocate(int n)
    {
        // TODO
        // 実装してください
        // bool flg = true;
        int re = -1;
        int i = 0;
        int tmp = 0;
        switch (n){
            case 1:
                for(auto itr = seat_ls.begin();itr != seat_ls.end();++itr){
                    if(*itr == 0){
                        *itr = 1;
                        re = i;
                        break;
                    }
                    i++;
                }
                break;
            
            default:
                for(auto itr = seat_ls.begin();itr != seat_ls.end();++itr){
                    if(*itr == 0 && re == -1){
                        re = i;
                        tmp = 1;
                    }else if(*itr == 0){
                        tmp++;
                    }else{
                        tmp = 0;
                        re = -1;
                    }
                    i++;

                    if(tmp == n){
                        break;
                    }
                }
                if(re != -1 && tmp == n){
                    auto itr = seat_ls.begin();
                    for(int j=0;j<re;j++){
                        ++itr;
                    }
                    for(int j=re;j<re+n;j++){
                        *itr = n;
                        ++itr;
                    }
                }else{
                    re = -1;
                }
                break;
        }

        return re;

    }

    // お客様が帰られる時に呼ばれるメソッドです
    // nはallocate時に返ってきたカウンター番号です。
    // allocate時の人数分お帰りになられます。バラバラに帰られることはありません。
    // 席の確保ができなかった時にも呼ばれることがあるので -1 が入力されても問題の無いように実装してください。
    // (例)
    // 全席空席の状態で allocate(4) を行い 0 が返ってきた時に
    // 0123456789 <- カウンター番号
    // oooo...... <- . 空き / o 使用中
    // free(0)を行うと
    // 0123456789 <- カウンター番号
    // .......... <- . 空き / o 使用中
    // 全席空席にもどしてください
    void free(int n)
    {
        // TODO
        // 実装してください
        if(n != -1){
            auto itr = seat_ls.begin();
            for(int j=0;j<n;j++){
                ++itr;
            }

            int num = *itr;
            for(int j=0;j<num;j++){
                *itr = 0;
                ++itr;
            }
        }
        
    }
};
