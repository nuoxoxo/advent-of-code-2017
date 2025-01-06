#include "iostream"
#include "sstream"
#include "map"
using namespace std;

template <typename ... Params>
void print(const Params &... args) {
    ( (std::cout << args << ' '), ... ) << '\n';
}

bool eval_r(int l, string m, int r){
    if (m == "==") return l == r;
    if (m == "!=") return l != r;
    if (m == "<") return l < r;
    if (m == ">") return l > r;
    if (m == "<=") return l <= r;
    assert(m == ">=");
    return l >= r;
}

int eval_l(int l, string m, int r) {return m == "inc" ? l + r : l - r;}

int main()
{
    map<string, int> D;
    string s;
    int p2 = -1;
    while (getline(cin, s))
    {
        string l,r,k,o,kk,oo;
        int v,vv;
        size_t idx = s.find(" if ");
        assert(idx != string::npos);
        l = s.substr(0,idx);
        r = s.substr(idx + 4);
        stringstream ll(l);
        ll >> k >> o >> v;
        stringstream rr(r);
        rr >> kk >> oo >> vv;
        //print(k,o,v,'-',kk,oo,vv); // dbg
        if (eval_r(D[kk], oo, vv))
        {
            D[k] = eval_l(D[k],o,v);
            p2 = p2 > D[k] ? p2 : D[k];
        }
    }
    int p1 = max_element(D.begin(), D.end(), [](auto& a, auto& b){
        return a.second < b.second;
    })->second;
    print("part 1:",p1);
    print("part 2:",p2);
}
