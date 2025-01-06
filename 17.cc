#include "iostream"
#include "vector"
using namespace std;

template <typename ... Params>
void print(const Params &... args) {
    ( (std::cout << args << ' '), ... ) << '\n';
}

int p1(int, int);
int p2(int, int, int);

int main(){
    int N = 2017, n2 = 50000000;
    int step = 371;
    //int res1sim = p1(3, N); print("part 1:",res1sim,"/test");
    int res1 = p1(step, N);
    print("part 1:",res1);
    int res2 = p2(step, n2, 0);
    print("part 2:",res2);
}

int p2(int step, int N, int AFTER) {

    int curr = 0;
    int len = 1;
    int res = 0;
    int i = -1;
    while (++i < N) {
        int insertpos = (curr + step) % len;
        if (insertpos == AFTER)
            res = i + 1;
        curr = insertpos + 1;
        ++len;
    }
    return res;
}

int p1(int step, int N) {

    vector<int> SL = {0};
    int curr = 0;
    int i = -1;
    while (++i < N){
        int len = SL.size();
        int insertpos = (curr + step) % len;
        SL.insert(SL.begin() + insertpos + 1, i + 1);
        curr = insertpos + 1;
    }
    return SL[curr + 1];
}

/*(0)
 * 0 (1) - it/0 - insert/it + 1
 * 0 (2) 1
 * 0 2 (3) 1
*/

