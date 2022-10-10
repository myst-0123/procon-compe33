#include "compare2.hpp"

vector<pair<int, double>> compare2(vector<vector<int>> problem_data, bool mode)
{
    cout << "----Function compare----" << endl;
    vector<pair<int, double>> match_rate;

    int problem_length = problem_data[1].size();

    int freq = problem_data.size();

    if (mode)
    {
        for (int i = 1; i <= 44; i++)
        {
            vector<vector<int>> compare_data;
            vector<double> avg_match_rate;

            compare_data = read_file("../data/Jb" + to_string(i) + ".txt");

            int compare_length = compare_data[1].size();

            int correct, all;

            for (int j = 0; j < problem_length - compare_length; j++)
            {
                correct = 0;
                all = 0;
                for (int k = 1; k < freq-1; k++)
                {
                    for (int m = 0; m < compare_length; m++)
                    {
                        if (compare_data[k][m] == 1)
                        {
                            all++;
                            if(problem_data[k][m + j] == 1)
                            {
                                correct++;
                            }
                        }
                    }
                }
                avg_match_rate.push_back(correct / (double)all);
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

            compare_data = read_file("../data/Eb" + to_string(i) + ".txt");

            int compare_length = compare_data[1].size();

            int correct, all;

            for (int j = 0; j < problem_length - compare_length; j++)
            {
                correct = 0;
                all = 0;
                for (int k = 1; k < freq-1; k++)
                {
                    for (int m = 0; m < compare_length; m++)
                    {
                        if (compare_data[k][m] == 1)
                        {
                            all++;
                            if(problem_data[k][m + j] == 1)
                            {
                                correct++;
                            }
                        }
                    }
                }
                avg_match_rate.push_back(correct / (double)all);
            }
            sort(avg_match_rate.rbegin(), avg_match_rate.rend());
            match_rate.push_back(make_pair(i, avg_match_rate[0]));
            cout << avg_match_rate[0] << endl;
        }
    }

    return match_rate;

}