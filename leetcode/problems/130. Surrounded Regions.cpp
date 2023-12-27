class Solution {
public:
    // Depth First Search (DFS) function
    void dfs(int i, int j, vector<vector<char>>& board) {
        // Base case and conditions to skip processing
        if (i < 0 || j < 0 || i == board.size() || j == board[0].size() || board[i][j]!='O') {
            return;
        }
        board[i][j]='T';
        dfs(i-1,j, board);
        dfs(i+1,j, board);
        dfs(i,j-1, board);
        dfs(i,j+1, board);
    }

    void solve(vector<vector<char>>& board) {
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if(board[i][j]=='O' && (i==0 || i==board.size()-1 || j==0 || j==board[0].size()-1)){
                    dfs(i,j,board);
                }
            }
        }
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if(board[i][j]=='O'){
                    board[i][j]='X';
                }
            }}
                for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if(board[i][j]=='T'){
                    board[i][j]='O';
                }
            }}
    }
};
