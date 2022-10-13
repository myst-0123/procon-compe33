#include "output.hpp"

void output(vector<pair<string, double>> score)
{
    ifstream problem_file("../problem-data.json");
    json problem_data;
    problem_file >> problem_data;

    int i = 0, j = 0;
    vector<string> answer;
    while (i < problem_data["data"])
    {
        if (find(answer.begin(), answer.end(), score[j].first) == answer.end())
        {
            answer.push_back(score[j].first);
            i++;
        }
        j++;
    }

    json output_data;

    output_data["answers"] = answer;
    output_data["problem_id"] = problem_data["id"];

    ofstream ofs("../solution.json");

    ofs << output_data << endl;

}