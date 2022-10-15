#include "output.hpp"

void output(vector<pair<string, double>> &result, vector<pair<string, double>> &result2, vector<pair<string, double>> &score)
{
    ifstream problem_file("../problem-data.json");
    ifstream submitted("../submitted.json");
    json problem_data;
    json submitted_data;
    problem_file >> problem_data;
    submitted >> submitted_data;

    int i = 0, j = 0;
    vector<string> submitted_answer = submitted_data["submitted_answer"];
    vector<string> answer;
    while (i < problem_data["data"])
    {

        if (find(submitted_answer.begin(), submitted_answer.end(), result[j].first.substr(1, 2)) == submitted_answer.end())
        {
            answer.push_back(result[j].first.substr(1, 2));
            submitted_answer.push_back(result[j].first.substr(1, 2));
            i++;
            if (i == problem_data["data"]) break;
        }
        if (find(submitted_answer.begin(), submitted_answer.end(), result2[j].first.substr(1, 2)) == submitted_answer.end())
        {
            answer.push_back(result2[j].first.substr(1, 2));
            submitted_answer.push_back(result2[j].first.substr(1, 2));
            i++;
            if (i == problem_data["data"]) break;
        }
        if (find(submitted_answer.begin(), submitted_answer.end(), score[j].first.substr(1, 2)) == submitted_answer.end())
        {
            answer.push_back(score[j].first.substr(1, 2));
            submitted_answer.push_back(score[j].first.substr(1, 2));
            i++;
            if (i == problem_data["data"]) break;
        }
        j++;
    }

    json output_data = {
        {"problem_id", problem_data["id"]},
        {"answers", answer}
    };

    submitted_data["submitted_answer"] = submitted_answer;

    ofstream ofs("../solution.json");
    ofstream ofs2("../submitted.json");

    ofs << setw(4) << output_data << endl;
    ofs2 << setw(4) << submitted_data << endl;

}