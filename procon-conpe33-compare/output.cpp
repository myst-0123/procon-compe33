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
        if (find(answer.begin(), answer.end(), score[j].first.substr(1, 2)) == answer.end())
        {
            answer.push_back(score[j].first.substr(1, 2));
            i++;
        }
        j++;
    }

    json output_data = {
        {"problem_id", problem_data["id"]},
        {"answers", answer}
    };

    ofstream ofs("../solution.json");

    ofs << setw(4) << output_data << endl;

}