#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

using pii = pair<int,int>;
using vpii = vector<pii>;

template <typename ... Params>
void print(const Params &... args)
{ ((cout << args << ' '), ...) << endl; }

int go1(const vpii & cmps, vpii & bridge) {

    int maxscore = 0;

    function<void(vpii &, int, int)> backtracking;
    backtracking = [&](vpii & seen, int port, int score) {
        if (score > maxscore) {
            maxscore = score;
            bridge = seen;
        }
        for (const auto & cmp: cmps) {
            int L = cmp.first, R = cmp.second;
            if (find(seen.begin(), seen.end(), cmp) == seen.end()\
            && (port == L || port == R)) {
                int otherport = (port == L) ? R : L;
                seen.push_back(cmp);
                backtracking(seen, otherport, score + L + R);
                seen.pop_back();
            }
        }
    };

    vpii seen;
    backtracking(seen,0,0);
    return maxscore;
}

int go2(const vpii & cmps, vpii & bridge) {

    int maxlen = 0;
    int maxscore = 0;

    function<void(vpii &, int, int, int)> backtracking;
    backtracking = [&](vpii & seen, int port, int len, int score) {
        if (len > maxlen || (len == maxlen && score > maxscore)) {
            maxlen = len;
            maxscore = score;
            bridge = seen;
        }

        for (const auto& cmp : cmps) {
            int L = cmp.first, R = cmp.second;
            if (find(seen.begin(), seen.end(), cmp) == seen.end() \
            && (port == L || port == R)) {
                int otherport = (port == L) ? R : L;
                seen.push_back(cmp);
                backtracking(seen, otherport, len + 1, score + L + R);
                seen.pop_back();
            }
        }
    };

    vpii seen;
    backtracking(seen, 0, 0, 0);
    return maxscore;
}

string getpath(const vpii & path) {
    string res;
    int i = -1;
    while (++i < path.size())
        res += to_string(path[i].first) + "/" + \
            to_string(path[i].second) + \
            (i < path.size() - 1 ? "-": "");
    return res;
}

int main() {

    vpii cmps;
    string line;

    while (getline(cin, line)) {
        stringstream ss(line);
        int a, b;
        char _;
        ss >> a >> _ >> b;
        cmps.push_back({a, b});
    }

    vpii bridge1, bridge2;

    int p1 = go1(cmps, bridge1);
    print("part 1:", p1);

    int p2 = go2(cmps, bridge2);    
    print("part 2:", p2);

    print("path 1:",getpath(bridge1));
    print("path 2:",getpath(bridge2));
}

