#include <iostream>
#include <vector>

#include "readfile.hpp"
#include "compare.hpp"
#include "compare2.hpp"
#include "eval.hpp"

using namespace std;

int main(int argc, char *argv[])
{
    bool is_japanese = stoi(argv[1]);

    vector<vector<int>> problem_data;
    vector<vector<int>> problem_data_b;
    vector<pair<string, double>> result;
    vector<pair<string, double>> result2;

    problem_data = read_file("../problem.txt");
    problem_data_b = read_file("../problemb.txt");

    result = compare(problem_data, is_japanese);
    result2 = compare2(problem_data_b, is_japanese);

    eval(result, result2);
    
}
