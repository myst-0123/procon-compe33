#include <vector>
#include <fstream>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

void output(vector<pair<string, double>> &result, vector<pair<string, double>> &result2, vector<pair<string, double>> &score);
