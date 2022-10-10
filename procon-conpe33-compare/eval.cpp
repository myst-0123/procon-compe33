#include "eval.hpp"

bool comp(pair<int, double> lhs, pair<int, double> rhs)
{
    return lhs.second < rhs.second;
}

void eval(vector<pair<int, double>> &result, vector<pair<int, double>> &result2)
{
    vector<pair<int, double>> scores;

    for (int i = 0; i < 44; i++)
    {
        double score = result[i].second + result2[i].second;
        scores.push_back(make_pair(i+1, score));
    }

    sort(result.rbegin(), result.rend(), comp);
    sort(result2.rbegin(), result2.rend(), comp);
    sort(scores.rbegin(), scores.rend(), comp);
    cout << "---------result------------" << endl;
    for (auto i: result)
    {
        printf("%2d %lf\n", i.first, i.second);
    }
    cout << "--------result2------------" << endl;
    for (auto i: result2)
    {
        printf("%2d %lf\n", i.first, i.second);
    }
    cout << "---------score-------------" << endl;
    for (auto i: scores)
    {
        printf("%2d %lf\n", i.first, i.second);
    }
}