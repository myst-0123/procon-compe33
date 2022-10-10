#include <iostream>
#include <vector>

#include "readfile.hpp"
#include "compare.hpp"
#include "compare2.hpp"

using namespace std;

bool comp(pair<int, double> lhs, pair<int, double> rhs)
{
    return lhs.second < rhs.second;
}

int main(int argc, char *argv[])
{
    bool is_japanese = stoi(argv[1]);

    vector<vector<int>> problem_data;
    vector<vector<int>> problem_data_b;
    vector<pair<int, double>> result;
    vector<pair<int, double>> result2;

    problem_data = read_file("../problem.txt");
    problem_data_b = read_file("../problemb.txt");

    result = compare(problem_data, is_japanese);
    result2 = compare2(problem_data_b, is_japanese);

    sort(result.rbegin(), result.rend(), comp);
    sort(result2.rbegin(), result2.rend(), comp);
    cout << "---------result------------" << endl;
    for (auto i: result)
    {
        cout << i.first << " " << i.second << endl;
    }
    cout << "--------result2------------" << endl;
    for (auto i: result2)
    {
        cout << i.first << " " << i.second << endl;
    }
}
