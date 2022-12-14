#pragma once
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include "readfile.hpp"

using namespace std;

double find_match_rate(int problem, int compare);

vector<pair<string, double>> compare(vector<vector<int>> data);
