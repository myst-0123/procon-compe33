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
        double score = (result[i].second + result2[i].second) / 2;
        if (i <= 8)
        {
            scores.push_back(make_pair("J0" + to_string(i+1), score));
        }
        else
        {
            scores.push_back(make_pair("J" + to_string(i+1), score));
        }
    }
    for (int i = 44; i < 88; i++)
    {
        double score = (result[i].second + result2[i].second) / 2;
        if (i <= 52)
        {
            scores.push_back(make_pair("E0" + to_string(i-43), score));
        }
        else
        {
            scores.push_back(make_pair("E" + to_string(i-43), score));
        }
    }

    sort(result.rbegin(), result.rend(), comp);
    sort(result2.rbegin(), result2.rend(), comp);
    sort(scores.rbegin(), scores.rend(), comp);
    cout << "----result---------result2---------score----" << endl;
    for (int i = 0; i < 88; i++)
    {
        printf("%3s %lf | %3s %lf |  %3s %lf \n", result[i].first.c_str(), result[i].second, result2[i].first.c_str(), result2[i].second, scores[i].first.c_str(), scores[i].second);
    }

    output(result, result2, scores);
}