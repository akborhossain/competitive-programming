#include<bits/stdc++.h>
using namespace std;
#include<iostream>
const int N=1e3+10;
vector<int> g[N];
bool vis[N];
void dfs(int vertex){

	vis[vertex]=true;
	for(int child: g[vertex]){
		if(vis[child]){
			continue;
		}
		dfs(child);
	}
}
int main() {
	int n,e;
	cin >> n>>e; 
	for(int i =0;i<e;i++){
		int u,v;
		cin>>u>>v;
		g[u].push_back(v);
		g[v].push_back(u);
	}
	int count=0;
	for(int i=1;i<=n;i++){

		if(vis[i]){
			continue;
		}
		dfs(i);
		count++;
	}
	cout<<count<<endl;
	
}