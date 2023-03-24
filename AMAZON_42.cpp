#include<bits/stdc++.h>
using namespace std;

int maxProfit(int k, vector<int>& prices) {
    int n = prices.size();
    if(n <= 1) return 0;

    // If k is large, we can perform as many transactions as we want
    if(k >= n / 2){
        int max_profit = 0;
        for(int i = 1; i < n; i++){
            if(prices[i] > prices[i-1])
                max_profit += prices[i] - prices[i-1];
        }
        return max_profit;
    }

    // If k is small, we use dynamic programming to find the maximum profit
    vector<vector<int>> dp(k+1, vector<int>(n, 0));
    for(int i = 1; i <= k; i++){
        int max_profit = -prices[0];
        for(int j = 1; j < n; j++){
            dp[i][j] = max(dp[i][j-1], prices[j] + max_profit);
            max_profit = max(max_profit, dp[i-1][j-1] - prices[j]);
        }
    }
    return dp[k][n-1];
}

int main(){
    int n, k;
    cin >> n >> k;

    vector<int> prices(n);
    for(int i = 0; i < n; i++){
        cin >> prices[i];
    }

    cout << maxProfit(k, prices) << endl;
    return 0;
}
