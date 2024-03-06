#include <bits/stdc++.h>
#include <fstream>
using namespace std;

vector<string> split(string line){
    string temp="";
    vector<string> out;
    for(int i=0; i<line.size(); i++){
        if(line[i]==' '){
            out.push_back(temp);
            temp="";
            continue;
        }
        else if(line[i]==','){
            continue;
        }
        else{
            temp=temp+line[i];
        }
    }
    out.push_back(temp);
    return out;
}

string add(vector<string> splitted, map<string, string> dict){
    string temp="1100110 ";
    temp+=dict[splitted[1]];
    temp+=" 000 ";
    temp+=dict[splitted[2]]+" "+dict[splitted[3]];
    temp+=" 0000000";
    return temp;
}

string sub(vector<string> splitted, map<string, string> dict){
    string temp="1100110 ";
    temp+=dict[splitted[1]];
    temp+=" 000 ";
    temp+=dict[splitted[2]] + " " + dict[splitted[3]];
    temp+=" 0100000";
    return temp;
}

string sll(vector<string> splitted, map<string, string> dict){
    string temp="1100110 ";
    temp+=dict[splitted[1]];
    temp+=" 001 ";
    temp+=dict[splitted[2]] + " " + dict[splitted[3]];
    temp+=" 0000000";
    return temp;
}

string slt(vector<string> splitted, map<string, string> dict){
    string temp="1100110 ";
    temp+=dict[splitted[1]];
    temp+=" 010 ";
    temp+=dict[splitted[2]] + " " + dict[splitted[3]];
    temp+=" 0000000";
    return temp;
}

string sltu(vector<string> splitted, map<string, string> dict){
    string temp="1100110 ";
    temp+=dict[splitted[1]];
    temp+=" 011 ";
    temp+=dict[splitted[2]] + " " + dict[splitted[3]];
    temp+=" 0000000";
    return temp;
}

string xory(vector<string> splitted, map<string, string> dict){
    string temp="1100110 ";
    temp+=dict[splitted[1]];
    temp+=" 100 ";
    temp+=dict[splitted[2]] + " " + dict[splitted[3]];
    temp+=" 0000000";
    return temp;
}

string srl(vector<string> splitted, map<string, string> dict){
    string temp="1100110 ";
    temp+=dict[splitted[1]];
    temp+=" 101 ";
    temp+=dict[splitted[2]] + " " + dict[splitted[3]];
    temp+=" 0000000";
    return temp;
}

string ory(vector<string> splitted, map<string, string> dict){
    string temp="1100110 ";
    temp+=dict[splitted[1]];
    temp+=" 110 ";
    temp+=dict[splitted[2]] + " " + dict[splitted[3]];
    temp+=" 0000000";
    return temp;
}

string andy(vector<string> splitted, map<string, string> dict){
    string temp="1100110 ";
    temp+=dict[splitted[1]];
    temp+=" 111 ";
    temp+=dict[splitted[2]] + " " + dict[splitted[3]];
    temp+=" 0000000";
    return temp;
}

int main(){
    map <string, string> dict;
    dict = { {"zero", "00000"},{"ra", "00001"}, {"sp","00010"}, {"gp","00011"}, {"tp", "00100"}, {"t0", "00101"}, {"t1", "00110"}, {"t2", "00111"}, {"s0", "01000"}, {"fp", "01000"}, {"s1", "01001"}, {"a0", "01010"}, {"a1", "01011"}, {"a2", "01100"}, {"a3", "01101"}, {"a4", "01110"}, {"a5", "01111"}, {"a6", "10000"}, {"a7", "10001"}, {"s2", "10010"}, {"s3", "10011"}, {"s4", "10100"}, {"s5", "10101"}, {"s6", "10110"}, {"s7", "10111"}, {"s8", "11000"}, {"s9", "11001"}, {"s10", "11010"}, {"s11", "11011"}, {"t3", "11100"}, {"t4", "11101"}, {"t5", "11110"}, {"t6", "11111"} };
    
    string line;
    ifstream fin;
    fin.open("sample.txt");

    ofstream fb;
    fb.open("output.txt");
    
    while(getline(fin, line)){
        vector<string> splitted=split(line);
        
        if(splitted[0]=="add"){
            string out=add(splitted, dict);
            fb << out << endl;
        }
        
        else if(splitted[0]=="sub"){
            string out=sub(splitted, dict);
            fb << out << endl;
        }
        
        else if(splitted[0]=="sll"){
            string out=sll(splitted, dict);
            fb << out << endl;
        }
        
        else if(splitted[0]=="slt"){
            string out=slt(splitted, dict);
            fb << out << endl;
        }
        
        else if(splitted[0]=="sltu"){
            string out=slt(splitted, dict);
            fb << out << endl;
        }
        
        else if(splitted[0]=="xor"){
            string out=xory(splitted, dict);
            fb << out << endl;
        }
        
        else if(splitted[0]=="srl"){
            string out=srl(splitted, dict);
            fb << out << endl;
        }
        
        else if(splitted[0]=="or"){
            string out=ory(splitted, dict);
            fb << out << endl;
        }
        
        else if(splitted[0]=="and"){
            string out=andy(splitted, dict);
            fb << out << endl;
        }
    }
    fin.close();
}