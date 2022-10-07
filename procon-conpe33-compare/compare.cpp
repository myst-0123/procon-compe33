#include "compare.hpp"

const int FREQ_LENGTH = 5000;

double find_match_rate(int problem, int compare)
{
    int error = abs(problem - compare);
    double error_rate = abs(error / compare);
    return 1 - error_rate;
}

vector<pair<int, double>> compare(vector<vector<int>> problem_data, bool mode)
{
    vector<pair<int, double>> match_rate;

    int problem_length = problem_data[1].size();

    if (mode)
    {
        for (int i = 1; i <= 44; i++)
        {
            vector<vector<int>> compare_data;
            vector<double> avg_match_rate;
            compare_data = read_file("../data/J" + to_string(i) + ".txt");
            int compare_length = compare_data[1].size();
            for (int j = 0; j < problem_length - compare_length; j++)
            {
                double match = 0;
                for (int k = 1; k <= FREQ_LENGTH; k++)
                {
                    for (int m = 0; m < compare_length; m++)
                    {
                        match += find_match_rate(problem_data[k][m], compare_data[k][m]);
                    }
                }
                avg_match_rate.push_back(match / (FREQ_LENGTH * compare_length));
            }
            sort(avg_match_rate.rbegin(), avg_match_rate.rend());
            match_rate.push_back(make_pair(i, avg_match_rate[0]));
            cout << avg_match_rate[0] << endl;
        }
    }
    else
    {
        for (int i = 1; i <= 44; i++)
        {
            vector<vector<int>> compare_data;
            vector<double> avg_match_rate;
            compare_data = read_file("../data/E" + to_string(i) + ".txt");

            int compare_length = compare_data[1].size();
            for (int j = 0; j < problem_length - compare_length; j++)
            {
                double match = 0;
                for (int k = 1; k <= FREQ_LENGTH; k++)
                {
                    for (int m = 0; m < compare_length; m++)
                    {
                        match += find_match_rate(problem_data[k][m], compare_data[k][m]);
                    }
                }
                avg_match_rate.push_back(match / (FREQ_LENGTH * compare_length));
            }
            sort(avg_match_rate.rbegin(), avg_match_rate.rend());
            match_rate.push_back(make_pair(i, avg_match_rate[0]));
        }
    }
    return match_rate;
}