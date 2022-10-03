#include <iostream>
#include <vector>

#include "readfile.hpp"
#include "compare.hpp"

using namespace std;

int main(int argc, char *argv[])
{
    bool is_japanese = stoi(argv[0]);

    vector<vector<int>> problem_data;

    problem_data = read_file("../problem.txt");

    compare(problem_data, is_japanese);
}