#include <bits/stdc++.h>
#include <atcoder/all>
#include <vector>

using namespace std;
// using namespace atcoder;
using ll = long long;
const ll MOD = 1000000007LL;
// const ll MOD = 998244353LL;

const vector<pair<int, int>> dpos4 = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// const vector<pair<int, int>> dpos8 = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // endlが改行
    // endlを挟まないことにより、cdと出力される
    cout << "c"
         << "d" << endl;
    // 数値は""を使わずに出力できる
    cout << 2525 << endl;
    // C++ではインデントはプログラムの動作に影響を与えない
    // 基本的に{が出てきたら一段インデントし、}が出てきたら一段戻します。
    // また、元々一行に書いていたプログラムが長くなった場合は、改行してインデントすることがあります。
    // 四則演算はpythonと同じで+,-,*,/を使う。また剰余演算も%を使う
    // 静的型付け言語のため、割り算は下記のようになる
    cout << 7 / 3 << endl;   // 2(2.33333の小数点を切り捨てている)
    cout << 7.0 / 3 << endl; // 2.3333
    cout << -7 / 3 << endl;  // -2(-2.33333の小数点を切り捨てている)
    // 割り算/のある整数同士の計算では、切り捨てが行われるタイミングの違いで結果が異なることがあります。
    // 3÷2×4を計算する場合、書き方によって2つの計算結果が考えられます。
    // 3 / 2 * 4 → 1 * 4 → 4
    // 3 * 4 / 2 → 12 / 2 → 6
    // 多くの場合、割り算はできるだけ後の方で行うようにしたほうが正しい結果になります。
    // 剰余演算A % Bを行う時にAまたはBが負の数の場合、計算結果は以下のようになります。
    // ∣A∣,∣B∣はそれぞれの絶対値を表すとします。
    // Aが正のとき：
    // ∣A∣%∣B∣
    // Aが負のとき：
    // −(∣A∣%∣B∣)

    // 変数の宣言
    int a;
    // 変数の宣言と初期化（同時にできる）
    int a = 10;
    // 複数の変数の宣言と初期化
    int a = 10, b = 5;
    // 変数の命名の制約
    // 数字で始まる名前はできない
    // _アンダーバー以外の記号は含められない
    // 予約語は変数名にできない
    // 同じスコープ内に同じ名前の変数を宣言できない

    // 重要な3つの型
    int i = 10;
    double d = 0.5;
    string s = "Hello";

    // 型同士の代入
    int i = 10;
    double d = i; // d=10 doubleとintは互いに代入できる（小数点以下切り捨て）
    string s = "Hello";

    // i = s; // int型とstring型は互いに代入できない
    double a = 2.5;
    int b = a; // b=2 doubleとintは互いに代入できる（小数点以下切り捨て）
    // 複数の入力を受け取る
    // coutと同じように、cinも>>を繋げて入力を受け取ることができます。
    // 入力が複数ある場合は、スペースか改行で区切られていれば分解して入力してくれます。
    int a, b, c;
    cin >> a >> b >> c;
    cout << a * b * c << endl;

    // 比較演算子はPythonと同じ
    // 論理演算子はJavaと同じ
    // 否定 !(論理式)
    // 論理積AND (論理式) && (論理式)
    // 論理和OR (論理式) || (論理式)

    // if文もJavaと同じ
    // if (条件式) {
    //     処理
    // }
    // 処理が1行（セミコロン;一つだけの処理）なら、{}を省略できる
    int x = 9;
    if (x < 10)
        cout << "xは10より小さい" << endl;
    // セミコロン一つだけの処理なら省略できるので、下記は意図した通りに動かない。
    if (x < 10)
        cout << "xは10より小さい" << endl;
    cout << "終了" << endl;
    // 下記と同じである、つまり()の後のセミコロンひとつ分だけが条件分岐内に入っている
    if (x < 10)
    {
        cout << "xは10より小さい" << endl;
    }
    cout << "終了" << endl;
    // 連続した比較はできない
    // 下記はコンパイルエラーにならないが、意図した動作にならない
    // 4<xがまず比較されてxの値によって1（真）または0（偽）となる。そして0または1と、10が比較されるので、常にtrueになる
    if (4 < x < 10)
    {
        cout << "できる" << endl;
    }
    // 条件分岐のif elseはJavaと同じ
    if (x < 10)
    {
        cout << "xは10より小さい" << endl;
    }
    else if (x > 20)
    {
        cout << "xは10より小さくなくて、20より大きい" << endl;
    }
    else if (x == 15)
    {
        cout << "xは10より小さくなくて、20より大きくなくて、15である" << endl;
    }
    else
    {
        cout << "xは10より小さくなくて、20より大きくもなくて、15でもない" << endl;
    }
    // 真偽値
    // 条件式は、真の時に1に、偽のときに0になる
    // 1をtrueで、0をfalseで表す
    if (1)
    {
        cout << "hello" << endl;
    }
    // 数字なのか、真偽値を表しているのかわかりにくいので、true,falseで明示できる
    if (true)
    {
        cout << "hello" << endl;
    }
    // bool型はtrueとfalseだけが入る型
    bool a = true;
    bool b = x < 10; // xが10未満のときtrue そうでないときfalseになる
    bool c = false;
    // bool型は1,0以外の数字を入れられる。その場合、0のときだけfalse、それ以外の数値はすべてtrueになります
    bool a = 10; // 10はtrue
    bool b = 0;  // 0はfalse

// 変数のスコープ
// {}で囲った範囲をブロックと言う。あるブロックの中で宣言した変数は、それより内側のブロックでしか使えない
// 変数を宣言するブロックが異なれば、同じ名前の変数が使える
// 異なる型で同じ名前の変数が宣言されている場合、スコープが重なる。
// その場合は、最も内側で宣言されている変数が使われる
// x = x + yはx += yのように短く書ける
// x += 1はx ++と書ける（インクリメント）
// x -= 1はx --と書ける（デクリメント）

// repマクロ　forループを書きやすくするマクロ
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
// usage:rep(i,3){ processing }  i starts at 0 and increments by 1 until it reaches n.
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
    // usage:rep2(i,1,3){ processing }  i starts at s and increments by 1 until it reaches n.
#define rep3(i, s, n, inc) for (int i = (s); i < (int)(n); i += inc)
    // 多重ループ
    rep(i, 2)
    {
        rep(j, 2)
        {
            cout << "i: " << i << ", j:" << j << endl;
        }
    }
    // break,continueを使うのは同じ
    // while文
    // while (条件式)
    // {
    // 処理
    // }
    // N回処理するプログラム
    int N = 10;
    int i = 0; // カウンタ変数
    while (i < N)
    {
        // 処理
        i++;
    }
    int i = 5;
    // 逆順ループ
    while (i >= 0)
    {
        cout << i << endl;
        i--;
    }
    // for文の書き方
    // 初期化、条件式、更新
    for (int i = 0; i < N; i++)
    {
        // 処理
    }

    // 文字列 string型
    // 文字列は変数.size()で取得可能
    string str = "Hello";
    cout << str.size() << endl; // 5
    // 文字列から特定のインデックスの文字を取り出すにはat(i)
    // インデックスは０始まり
    cout << str.at(0) << endl; // H
    // 文字 char型
    char c = 'a';
    cout << c << endl;  // a
    char c = str.at(0); // char型の値が得られる
    // 文字列の一部の書き換えはchar型を使う
    str.at(0) = 'M';     // char型の'M'に書き換え
    cout << str << endl; // Mello

    if (str.at(1) == 'e')
    {
        cout << "AtCoder" << endl;
    }
    // ループと組み合わせる。下記は、Oという文字が何回出てくるか数えている
    string str;
    cin >> str;

    int count = 0;
    for (int i = 0; i < str.size(); i++)
    {
        if (str.at(i) == 'O')
        {
            count++;
        }
    }
    // stringやchar型は全角文字をうまく扱えない
    // 文字列を変数に入れず関数を使いたい場合、末尾にsをつける
    cout << "Hello"s.size() << endl; // 5（sを末尾につける）
    // C++の順序では'0'～'9'→'A'～'Z'→'a'～'z'の順になっている
    // "ABC"s < "xyz"s == true
    // 文字列は+や+=で連結できる
    string hello = "Hello";

    // +演算子による連結
    cout << hello + ", world!" << endl; // Hello, world!

    // +=演算子による連結
    hello += ", AtCoder!";
    cout << hello << endl; // Hello, AtCoder!
    // string型とchar型は比較できない
    // string型とchar型は+で連結できる
    // char型の変数にcinで入力すると、1文字ずつ変数に入れられる
    char a, b;
    cin >> a >> b;     //"OK"という入力
    cout << a << endl; // O
    cout << b << endl; // K
    // 改行を表すエスケープシーケンス \n
    cout << "こんにちは\nAtCoder";
    // こんにちは
    // AtCoder

    // 行単位での入力の受け取り
    // cinを使うと空白や改行区切りの入力を簡単に扱えますが、空白で区切らずに行単位で入力を受け取りたいこともあります。
    // その場合はgetlineを使います。
    string s, t;
    getline(cin, s); // 変数sで入力を一行受け取る
    getline(cin, t); // 変数tで入力を一行受け取る

    cout << "一行目 " << s << endl;
    cout << "二行目 " << t << endl;
    // 入力
    // I have a pen.
    // I have an apple.
    // 実行結果
    // 一行目 I have a pen.
    // 二行目 I have an apple.
    // getline関数は下記の形式で入力を受けとる
    // getline(cin, 文字列変数);

    // 配列
    vector<int> vec; // int型の配列変数vecを宣言

    vec = {25, 100, 64}; // 25, 100, 64 という整数(int)の列を代入

    cout << vec.at(0) << endl; // 1つめである25を出力

    cout << vec.size() << endl; // 配列の長さである3を出力
    // 配列の宣言
    // vector<型> 配列変数名;
    // 配列変数に値を代入する方法
    // 配列変数 = { 要素1, 要素2, ... };
    // 文字列と同様に、at()やsize()が使える

    // 配列への代入方法
    // 3個の入力を受け取れるように 3要素の配列 {0, 0, 0} で初期化
    vector<int> vec(3);

    // atを使って1つずつ入力
    cin >> vec.at(0) >> vec.at(1) >> vec.at(2);

    // 和を出力
    cout << vec.at(0) + vec.at(1) + vec.at(2) << endl;
    // 配列の初期化
    // 次のように書くと、指定した要素数で配列を初期化できます。
    // vector<型> 配列名(要素数);
    // int型なら0で、string型なら""で初期化
    // for文を使った入力
    vector<int> vec(100);

    // 100個の入力を受け取る
    for (int i = 0; i < 100; i++)
    {
        cin >> vec.at(i);
    }
    // 配列の初期値の設定
    // vector<型> 配列名(要素数, 初期値);
    vector<int> vec(3, 5); // vec = {5, 5, 5}
    // 配列の末尾に要素を追加
    // 配列変数.push_back(追加する要素)
    vec.push_back(10); // 末尾に10を追加

    // 末尾の要素の削除
    // 配列変数.popback()

    // 末尾の要素の取得 配列変数.back()
    int &x = vec.back();

    // 配列変数同士の比較==
    // ==では2つの配列の全要素が一致していたとき、条件式は真になります。
    // ただし、比較する際はどちらも「配列変数」である必要があり、vec == { 1, 2, 3 }のようには書けないことに注意しましょう。

    // 配列の初期化方法2
    // vector<型> 配列変数 = vector<型>(要素数, 初期値);
    vector<int> vec(3, 10);    // {10, 10, 10} で初期化
    vec = vector<int>(100, 2); // 100要素の配列 {2, 2, ... , 2, 2} で上書き

    // STLの関数
    // min,max,swap,sort,reverese
    // min,max,swapは引数の二数が同じ型でないといけない
    // swap(a,b) 変数a,bの値を置き換える
    // 昇順ソート
    // sort(配列名.begin(),配列名.end())
    // 降順ソート
    // sort(配列名.begin(),配列名.end(),greater<int>())
    // reverse(配列名.begin(),配列名.end())

    // あるいは、昇順ソートしてから逆順にすることで降順ソートする
    sort(vec.begin(), vec.end());    // {1, 2, 2, 5}
    reverse(vec.begin(), vec.end()); // {5, 2, 2, 1}

    // 関数の定義（Javaと同じ）
    // 返り値の型 関数名(引数1の型 引数1の名前, 引数2の型 引数2の名前, ...) {
    //   処理
    // }
    // 関数の返り値はreturn文を使ってreturn 返り値;で指定する
    // 関数の返り値が無い場合は返り値の型にvoidを指定し、return文はreturn;と書く
    // 関数の引数が不要な場合は定義と呼び出しで()だけを書く
    // 処理がreturn文の行に到達した時点で関数の処理は終了する
    // 返り値がある関数で返り値の指定を忘れた場合、どんな値が返ってくるかは決まっていない
    // 引数に渡された値は基本的にコピーされる
    // 関数は定義した以降の行でしか使用できない（コンパイルエラー）
    //      例外：プロトタイプ宣言

    // 範囲for文:配列や文字列など、コンテナに対するfor文を簡潔に書ける
    // for (配列の要素の型 変数名 : 配列変数) {
    // // 各要素に対する処理
    // }
    vector<int> example = {1, 3, 2, 5};
    for (int x : example)
    {
        cout << x << endl;
    }

    // 多重ループの抜け方
    // フラグ変数を用意して、フラグ変数の値に応じてループを抜ける
    // bool finished = false; // 外側のループを抜ける条件を満たしているかどうか(フラグ変数)

    // for (int i = 0; i < 100; i++)
    // {
    //     for (int j = 0; j < 100; j++)
    //     {

    //         /* 処理 */

    //         if (/* 2重ループを抜ける条件 */)
    //         {
    //             finished = true;
    //             break; // (＊)
    //                    // finishをtrueにしてからbreakすることで、
    //                    //   内側のループを抜けたすぐ後に外側のループも抜けることができる
    //         }
    //     }
    //     // (＊)のbreakでここに来る

    //     if (finished)
    //     {
    //         break; // (＊＊)
    //     }
    // }
    // (＊＊)のbreakでここに来る

    // あるいは、多重ループの部分を関数化し、関数の内部で使えるreturnを使って一気に抜けるという方法もあります。
    // void func(/* 処理に必要な変数 */)
    // {
    //     for (int i = 0; i < ...; i++)
    //     {
    //         for (int j = 0; j < ...; j++)
    //         {

    //             /* 処理 */

    //             if (/* 2重ループを抜ける条件 */)
    //             {
    //                 return; // 関数のreturnはループに関係なく抜けることができる
    //             }
    //         }
    //     }
    // }

    // int main()
    // {
    //     func();
    // }

    // string型の途中から抽出（切り抜き）
    // substr
    string Ex = "Hello";
    Ex.substr(3); // lo
    // string型をint型に変換 stor
    string Num = "000";
    stoi(Num);

    // 2次元配列
    // vector<vector<要素の型>> 変数名(要素数1, 初期値)
    // なお、初期値はvector<要素の型>(要素数2))で書く。すなわちまとめると、
    // vector<vector<要素の型>> 変数名(要素数1, vector<要素の型>(要素数2)))

    // 要素へのアクセス
    // 変数名.at(i)  // i番目の1次元配列
    // 変数名.at(i).at(j)  // i番目の1次元配列 のj番目の要素

    // 後から要素を追加するために、要素数0の配列をもつN行0列の配列を作る方法
    // vector<vector<型>> 変数名(N);  // 「要素数0の配列」の配列
    vector<vector<int>> data(3); // 3×0の配列

    data.at(0).push_back(1);
    data.at(0).push_back(2);
    data.at(0).push_back(3); // data.at(0)は3要素の配列

    // 注意点
    // 変数名.size()で取得できるのは1次元目の要素数

    // 要素を指定して初期化する方法
    // 2次元配列の初期化
    vector<vector<int>> data1 = {
        {7, 4, 0, 8},
        {2, 0, 3, 5},
        {6, 1, 7, 0}};

    // 2次元配列について、空白区切りで1行ずつ出力する方法
    vector<vector<char>> result(N, vector<char>(N, '-')); // resultはN行N列の2次元配列

    rep(i, N)
    {
        rep(j, N)
        {
            cout << result[i][j];
            if (j == N - 1)
            {
                cout << endl; // 末尾なら改行
            }
            else
            {
                cout << " "; // それ以外なら空白
            }
        }
    }
    // 参照
    // 参照先の型 &参照の名前 = 参照先;
    // 宣言時に参照先を指定して初期化しないといけない。また、参照先を後から変更することはできない
    int a = 123;
    int &b = a; // int型変数aへの参照

    string s = "apg4b";
    string &t = s; // string型変数sへの参照

    vector<int> v = {1, 2, 3, 4, 5};
    vector<int> &w = v; // vector<int>型変数vへの参照

    // int &c; // 参照先が指定されていないためコンパイルエラーになる

    // 参照渡しでの関数の書き方　引数を参照渡しする
    // int g(int &x)
    // {
    //     x = x * 2; // xを2倍 (参照によって"呼び出す側の変数"が変更される)
    //     return x;
    // }

    // 参照渡しの使い所
    // 1　関数の結果を複数返す
    // 配列に結果を入れて返すことで代用できるが、参照の引数をそのまま更新することで引数の数だけ結果を複数返す事ができる（厳密には、結果を返しているわけではない。引数を参照で更新して、その更新後の引数＝結果として扱っている）
    // a,b,cの最大値、最小値をそれぞれminimumの参照先、maximumの参照先に代入する
    // void min_and_max(int a, int b, int c, int &minimum, int &maximum) {
    //   minimum = min(a, min(b, c));  // 最小値をminimumの参照先に代入
    //   maximum = max(a, max(b, c));  // 最大値をmaximumの参照先に代入
    // }

    // 2　無駄なコピーを減らす
    // たとえば、配列に対してある処理をする関数Fがあるとする。要素数1000000の配列を引数に渡してFを50回呼ぶと、50回新しく要素数1000000の配列がコピーされる。
    // このコピーに時間がかかり、計算量が悪化する。
    // しかし、参照渡しだと、配列のコピーが生じず計算時間が短くなる。
    // コピーが必要ない場合は、参照渡しを用いるのがベスト。

    // 参照の書き方のバリエーション
    // 参照先の型 &参照の名前 = 参照先;  // 変数の前
    // 参照先の型& 参照の名前 = 参照先;  // 型の直後
    // 参照先の型 & 参照の名前 = 参照先;  // 中間

    // 複数の参照の宣言をしたい場合は、参照をする変数それぞれに書かないといけない。そのため、変数の前に参照を書くことを推奨
    int a = 123;
    int &b = a, &c = a; // bとcはどちらもaへの参照

    // 参照を利用した範囲for文。
    // 配列の要素を直接書き換えることができる
    vector<int> ar = {1, 3, 2, 5};
    for (int &x : ar)
    {
        x = x * 2;
    }
    // aは{2, 6, 4, 10}となる

    return 0;
}