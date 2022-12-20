#include "iostream"
#include "vector"

#define end endl

using	namespace std;

int	solver1(string &);
int	solver2(string &);

int	main()
{
	vector<string>	a;
	string		s;
	int r1 = 0, r2 = 0;

	while (!cin.eof() && cin >> s)
		a.push_back( s );
	cout << "p1: ";
	for (string ss: a)
		r1 = solver1(ss);
	cout << "\np2: ";
	for (string ss: a)
		r2 = solver2(ss);
	cout << "\n\nStar 1: " << r1 << "\nStar 2: " << r2 << end;
}

int	solver2(string &s)
{
	int i = -1;
	int r = 0, len = s.length(), mid = len / 2;
	while (++i < len)
	{
		if (mid + i < len && s[i] == s[mid + i])
			r += (s[i] - '0') * 2;
	}
	cout << r << ' ';
	return r;
}

int	solver1(string& s)
{
	int i = -1;
	int r = 0;
	int len = s.length();
	while (++i < len)
	{
		if ((i ^ len - 1 && s[i] == s[i + 1])
		|| (i == len - 1 && s[i] == s[0]))
		{
			r += s[i] - '0';
		}
	}
	cout << r << ' ';
	return r;
}
