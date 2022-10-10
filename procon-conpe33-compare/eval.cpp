#include "eval.hpp"

bool comp(pair<string, double> lhs, pair<string, double> rhs)
{
    return lhs.second < rhs.second;
}

void eval(vector<pair<string, double>> &result, vector<pair<string, double>> &result2)
{
    vector<pair<string, double>> scores;

    for (int i = 0; i < 44; i++)
    {
        double score = result[i].second + result2[i].second;
        scores.push_back(make_pair("J" + to_string(i+1), score));
    }
    for (int i = 44; i < 88; i++)
    {
        double score = result[i].second + result2[i].second;
        scores.push_back(make_pair("E" + to_string(i-43), score));
    }

    sort(result.rbegin(), result.rend(), comp);
    sort(result2.rbegin(), result2.rend(), comp);
    sort(scores.rbegin(), scores.rend(), comp);
    cout << "---------result------------" << endl;
    for (auto i: result)
    {
        printf("%s %lf\n", i.first.c_str(), i.second);
    }
    cout << "--------result2------------" << endl;
    for (auto i: result2)
    {
        printf("%s %lf\n", i.first.c_str(), i.second);
    }
    cout << "---------score-------------" << endl;
    for (auto i: scores)
    {
        printf("%s %lf\n", i.first.c_str(), i.second);
    }
}