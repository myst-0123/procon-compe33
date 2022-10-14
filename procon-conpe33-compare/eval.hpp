#pragma once
#include <vector>
#include <algorithm>
#include <iostream>

#include "output.hpp"

using namespace std;

bool comp(pair<string, double> lhs, pair<string, double> rhs);

void eval(vector<pair<string, double>> &result, vector<pair<string, double>> &result2);
