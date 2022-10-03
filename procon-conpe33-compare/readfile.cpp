#include "readfile.hpp"

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

vector<vector<int>> read_file(string file_name)
{
    vector<vector<int>> data(1);

    ifstream read_file;
    read_file.open(file_name, ios::in);

    string read_buffer;

    while (!read_file.eof())
    {
        vector<int> buffer;
        getline(read_file, read_buffer);
        
        buffer = split(read_buffer);
        data.push_back(buffer);
    }

    return data;
}