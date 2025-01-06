#include "iostream"
#include "sstream"
#include "map"
using namespace std;

template <typename ... Params>
void print(const Params &... args) {
    ( (std::cout << args << ' '), ... ) << '\n';
}

int main(){
    string line;
    getline(cin, line);
    print(line,"/line");
    int N = line.size();
    int i = 0;
    string noxcl;
    while (i < N) {
        if (line[i] == '!') {
            i += 2;
            continue;
        } else {
            noxcl += line[i++];
        }
    }
    print(noxcl,"!/no");
    string end;
    i = 0;
    int p2 = 0;
    N = noxcl.size();
    while (i < N) {
        if (noxcl[i] == '<') {
            int shift = -1;
            while (i < N && noxcl[i] != '>') {
                ++shift;
                ++i;
            }
            p2 += shift;
        } else if (i < N) {
            if (noxcl[i] != '>')
                end += noxcl[i];
            i++;
        }
    }
    print(end,"no/<");
    int p1 = 0;
    int sc = 0;
    for (char c: end) {
        if (c == '{') {
            sc++;
            p1 += sc;
        } else if (c == '}') {
            sc--;
        }
    }
    print("part 1:",p1);
    print("part 2:",p2);
}
