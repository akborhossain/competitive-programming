#include<iostream>
using namespace std;
string s,ss;
void StringToNumber(string)
{



}
void NumberToString(int num)
{
    if(num){
        num_to_str((num-1)/26);
        ss+=('A'+(num-1)%26);
    }

}

int main()
{
    int n;
    cin>>n;

    vector<string> v,v2;
    for(int i=0; i<n; i++)
    {

        cin>>s;

        for(int j=0; j<s.size(); j++)
        {
            if(s[j]>='A' && s[j]<='Z')
            {
                string s1;

                while(s[j]>='A' && s[j]<='Z')
                {
                    s1+=s[j];
                    j++;
                }
                v.push_back(s1);
            }
            else
            {
                string s1;
                while(s[j]>='0' && s[j]<='9')
                {
                    s1+=s[j];
                    j++;
                }
                v2.push_back(s1);

            }
            j--;
        }

    }


}
