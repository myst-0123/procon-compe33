#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<int> split(const string &s)
{
    vector<int> elems;
    string item;
    for (char ch: s)
    {
        if (ch == ' ')
        {
            if (!item.empty())
            {
                elems.push_back(stoi(item));
                item.clear();
            }
        }
        else
        {
            item += ch;
        }
    }
    if (!item.empty())
    {
        elems.push_back(stoi(item));
    }
    return elems;
}

int main()
{
    
    vector<vector<int>> problem_data(1);

    ifstream read_file;
    read_file.open("../problem.txt", ios::in);

    string read_buffer;

    while (!read_file.eof())
    {
        vector<int> buffer;
        getline(read_file, read_buffer);
        
        buffer = split(read_buffer);
        problem_data.push_back(buffer);
    }

    for (auto i: problem_data)
    {
        for (auto j: i)
        {
            printf("%4d", j);
        }
        cout << endl;
    }
}