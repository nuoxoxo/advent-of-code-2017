#include "iostream" // hex
#include "vector"
#include "sstream"
#include "algorithm" //reverse
#include "iomanip" // setfill setw

template <typename ... Params>
void print(const Params &... args) {
    ( (std::cout << args << ' '), ... ) << '\n';
}

std::vector<int> go(int, std::string, int);
std::string go2(std::string);

int main(){
    std::string line;
    std::getline(std::cin, line);
    print(line,"/line");
    std::vector<int> nums = go(1,line,256);
    std::string p2 = go2(line);

    print("part 1:", nums[0] * nums[1]);
    print("part 2:", go2(line));
}

std::string go2(std::string LINE) {
    std::string SEQ = "17, 31, 73, 47, 23";
    std::string line;
    for (char c: LINE)
        line += std::to_string(int(c)) + ',';
    for (char c: SEQ)
        if (c != ' ') line += c;
    std::vector<int> nums = go(64,line,256);
    int i = 0;
    int N = nums.size();
    std::string knot;
    while (i < N){
        int x = nums[i];
        int j = i;
        while (++j < i + 16)
            x ^= nums[j];
        // 2 ways to get a len-2 hex string
        //  1/ hex and iomanip
        std::stringstream ss;
        ss << std::hex << std::setw(2) << std::setfill('0') << x;
        knot += ss.str();
        //  2/ sprintf
        char hx[2];
        std::sprintf(hx, "%x", x);
        std::string res = hx;
        assert (ss.str() == (res.size() < 2 ? '0' + res : res));
        i += 16;
    }
    assert (knot.size() == 1<<5);
    return knot;
}

std::vector<int> go(int rounds, std::string line, int RANGE) {
    std::vector<int> lens;
    std::vector<int> nums(RANGE);
    std::stringstream ss(line);
    std::string tmp;
    while (std::getline(ss, tmp, ','))
        lens.push_back(stoi(tmp));
    int i = -1;
    while (++i < RANGE)
        nums[i] = i;
    int curr = 0;
    int skip = 0;
    i = -1;
    while (++i < rounds) {
        for (int ln: lens) {
            std::vector<int> indices, rv;
            int j = -1;
            while (++j < ln) {
                int idx = (curr + j) % RANGE;
                indices.push_back(idx);
                rv.push_back(nums[idx]);
            }
            std::reverse(rv.begin(), rv.end());
            j = -1;
            while (++j < indices.size())
                nums[indices[j]] = rv[j];
            curr = (curr + skip + ln) % RANGE;
            skip = (skip + 1) % RANGE;
        }
    }
    return nums;
}
