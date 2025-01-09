#include <iostream>
#include <vector>

template <typename ... Params>
void print(const Params &... args) {
    ( (std::cout << args << ' '), ... ) << '\n';
}

int main() {
    std::vector<std::string> g;
    std::string line;
    while (std::getline(std::cin, line))
        g.push_back(line);
    int R = g.size();
    int C = g[0].size();
    int r = 0, c = 0;
    for (int cc = 0; cc < C; ++cc) {
        if (g[0][cc] == '|') {
            c = cc;
            break;
        }
    }
    std::string path = "";
    int D[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
    int d = 0;
    int step = 0; // p2
    while (-1 < r && r < R && -1 < c && c < C && g[r][c]!=' ') {
        ++step;
        char chr = g[r][c];
        int dr = D[d][0];
        int dc = D[d][1];
        if ('A' <= chr && chr <='Z') {
            path += chr;
            r += dr;
            c += dc;
        }
        else if (chr == '-' || chr == '|') {
            r += dr;
            c += dc;
        }
        else {
            assert (chr == '+');
            for (int i : {d-1,d+1}) {
                int dd = (i + 4) % 4;
                int dr = D[dd][0], dc = D[dd][1];
                int rr = r + dr, cc = c + dc;
                if (-1 < rr && rr < R && -1 < cc && cc < C && g[rr][cc]!=' '){
                    d = dd;
                    r += dr;
                    c += dc;
                    break;
                }
            }
            if (g[r][c] == ' ')
                break;
        }
    }
    print("part 1:", path);
    print("part 2:", step);
}
