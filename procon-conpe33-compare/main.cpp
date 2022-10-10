#include <iostream>
#include <vector>

#include "readfile.hpp"
#include "compare.hpp"

using namespace std;

bool comp(pair<int, double> lhs, pair<int, double> rhs)
{
    return lhs.second < rhs.second;
}

int main(int argc, char *argv[])
{
    bool is_japanese = stoi(argv[1]);

    vector<vector<int>> problem_data;
    vector<pair<int, double>> result; 

    problem_data = read_file("../problem.txt");

    result = compare(problem_data, is_japanese);
    sort(result.rbegin(), result.rend(), comp);
    cout << "---------result------------" << endl;
    for (auto i: result)
    {
        cout << i.first << " " << i.second << endl;
    }
}
