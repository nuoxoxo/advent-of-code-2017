#include "iostream"
#include "vector"
#include "map"

using namespace std;

template <typename ... Params>
void print(const Params &... args)
{ ((cout << args << ' '), ...) << endl; }

int go1(vector<string>&, int);
int go2(vector<string>&, int);

const int DR[4] = {-1,0,1, 0};
const int DC[4] = { 0,1,0,-1};
// faster than:
// const vector<vector<int>> D = {{-1,0},{0,1},{1,0},{0,-1}};
enum State { None = 0, Inf, Flag, Weak }; // also faster

int main(){
    vector<string> v;
    string line;
    while (getline(cin, line))
        v.push_back(line);
    int p1 = go1(v, 10000);
    int p2 = go2(v, 10000000);
    print("part 1:", p1);
    print("part 2:", p2);
    assert (p1 == 5322 || p1 == 5587);
    assert (p2 == 2511944 || p2 == 2512079);
}

int go2(vector<string> &v, int RANGE) {
    //map<pair<int,int>, int> states; // map is slow
    int N = v.size();
    int OFFSET = N * 72; // 64 too small
    vector<vector<int>> states(OFFSET * 2 , vector<int>(OFFSET * 2, None));
    int r = -1, c;
    while (++r < N){
        c = -1;
        while (++c < N)
            if (v[r][c] == '#')
                states[r + OFFSET][c + OFFSET] = Inf;//states[{r,c}] = Inf;
    }
    r = N / 2 + OFFSET;
    c = r;
    int d = 0;
    int i = -1;
    int res = 0;
    while (++i < RANGE) {
        if (i % 2000000 == 0) print("i/",i);
        int &state = states[r][c];
        int todo;
        if (state == Inf) {
            d = (d + 1) % 4;
            todo = Flag;
        } else if (state == Flag) {
            d = (d + 2) % 4;
            todo = None;
        } else if (state == None) {
            d = (d + 3) % 4;
            todo = Weak;
        } else if (state == Weak) {
            todo = Inf;
            ++res;
        } else {
            assert (false);
        }
        state = todo;
        int dr = DR[d];
        int dc = DC[d];
        r += dr;
        c += dc;
    }
    return res;
}

int go1(vector<string> &v, int RANGE) {
    map<pair<int,int>,bool> states;
    int N = v.size();
    int r = -1, c;
    while (++r < N){
        c = -1;
        while (++c < N)
            if (v[r][c] == '#')
                states[{r,c}] = true;
    }
    r = N / 2;
    c = r;
    int d = 0;
    int i = -1;
    int res = 0;
    while (++i < RANGE) {
        bool &state = states[{r,c}];
        if (state) {
            d = (d + 1) % 4;
        } else {
            d = (d + 3) % 4;
            ++res;
        }
        state = !state;
        int dr = DR[d];
        int dc = DC[d];
        r += dr;
        c += dc;
    }
    return res;
}
