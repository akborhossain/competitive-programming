#include<bits/stdc++.h>
using namespace std;
void solve(int n)
{
    cout<< n << " " <<endl;
    if(n==1)
    {
        return;
    }
    solve(n-1);

}

int main()
{
    int n;
    cin>>n;
    solve(n);
}
