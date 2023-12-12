#include<bits/stdc++.h>
#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
const int N=1e3+10;

vector<vector<int> > g;
vector<int> color;

bool dfs(int vertex)
{
    bool re=true;
    for (int child:g[vertex])
    {
        if(color[child]!=0 && color[vertex]==color[child]){
            return false;
        }
        if(color[child]==0){
            color[child]=(color[vertex]==1 ? 2 : 1);
            re=re&dfs(child);
        }

    }
    return re;
}
int main()
{
    int n,l;

    while(1)
    {
        cin>>n;
        if (n==0) break;
        cin>>l;
        g.clear();
        g.resize(n);
        color.assign(n,0);
        for(int i=0; i<l; i++)
        {
            int v,u;
            cin>>v>>u;
            g[v].push_back(u);
            g[u].push_back(v);

        }

        color[0] = 1;

        if(dfs(0)){
            cout<<"BICOLORABLE."<<endl;
        }
        else{
            cout<<"NOT BICOLORABLE."<<endl;
        }

    }

}
