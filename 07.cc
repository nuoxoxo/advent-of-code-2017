#include "iostream"
#include "vector"
#include "unordered_map"
#include "sstream"
#include "deque"

struct Node
{ int weight = 0; std::vector<std::string> progs; };

struct defaultdict
{
    std::unordered_map<std::string, Node> _map;
    Node & operator[] (const std::string & key)
    { return _map[key]; }
};

template <typename ... Params>
void print(const Params &... args)
{ ((std::cout << args << ' '), ...) << std::endl; }

std::string join(const std::vector<std::string> & v)
{
    std::string res = join(v);
    res.pop_back();
    return res;
}

int main() {
    defaultdict g;
    std::string line;
    while (std::getline(std::cin, line)) {
        std::stringstream ss(line);
        std::string tmp;
        std::vector<std::string> v;
        while (ss >> tmp) {
            if (tmp[tmp.size() - 1] == ',')
                tmp.pop_back();
            v.push_back(tmp);
        }
        std::string name = v[0];
        int end = v[1].size();
        int weight = std::stoi(v[1].substr(1, end - 1));
        g[name].weight = weight;
        if (v.size() > 2) {
            std::vector<std::string> sub(v.begin() + 3,v.end());
            for (auto child: sub)
                g[name].progs.push_back(child);
        }
        //print("added/",name, g[name].weight, join(g[name].progs));
    }
    // do kahn
    std::unordered_map<std::string, int> indg;
    for (auto & [name,node] : g._map) {
        for (auto & child: node.progs)
            indg[child] += 1;
    }
    std::unordered_map<std::string, int>::iterator it = indg.begin(); 
    std::deque<std::string> degree0;
    for (auto & [name,_] : g._map) {
        if (indg.find(name) == indg.end())
            degree0.push_back(name);
    }
    assert (degree0.size() == 1);
    std::string p1 = degree0[0];
    std::vector<std::string> sorted;
    while (degree0.size()){
        std::string name = degree0.front();
        sorted.push_back(name);
        degree0.pop_front();
        for (auto & child : g[name].progs) { // childname
            indg[child]--;
            if (!indg[child])
                degree0.push_back(child);
        }
    }
    std::vector<std::string> reversed(sorted.rbegin(), sorted.rend());
    // now we got a reversedly topo-sorted tree
    std::unordered_map<std::string,int> SUMS;
    std::string special;
    int p2;
    for (auto name: reversed) {
        auto children = g[name].progs;
        // print("name/",name,"- progs/",join(children));
        std::unordered_map<int,int> FREQ;
        for (auto child: children)
            FREQ[SUMS[child]]++;
        assert (FREQ.size() < 3);
        int N = FREQ.size();
        int freqmax = -1, freqmin = INT_MAX, many, only;
        if (N == 2) {
            for (auto & [k,v] : FREQ) {
                if (freqmax < v) {
                    freqmax = v;
                    many = k;
                }
                if (freqmin > v) {
                    freqmin = v;
                    only = k;
                }
            }
        }
        int update = 0;
        std::string thewrongone;
        for (auto child: children) {
            update += SUMS[child];
            int accumulated = SUMS[child];
            if (N == 2 && accumulated ^ many) {
                thewrongone = child;
                break ;
            }
        }
        if (thewrongone != "") {
            int correction = std::abs(many - only);
            p2 = g[thewrongone].weight - correction;
            break ;
        }
        SUMS[name] = update + g[name].weight;
    }
    print("part 1:", p1);
    print("part 2:", p2);
}

