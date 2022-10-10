#pragma once

#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<int> split(const string &s);

vector<vector<int>> read_file(string file_name);
