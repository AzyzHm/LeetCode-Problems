#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        short maxOccurences = 0;
        int majorityElement = 0;
        vector<int> uniqueNums = unique(nums);
        for(int i = 0; i < uniqueNums.size(); i++){
            int occurences = countOccurences(nums, uniqueNums[i]);
            if(occurences > maxOccurences){
                maxOccurences = occurences;
                majorityElement = uniqueNums[i];
            }
        }
        return majorityElement;
    }
private:
    int countOccurences(vector<int>& nums, int num){
        int count = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == num){
                count++;
            }
        }
        return count;
    }
    vector<int> unique(vector<int>& nums){
        vector<int> unique;
        for(int i = 0; i < nums.size(); i++){
            if(find(unique.begin(), unique.end(), nums[i]) == unique.end()){
                unique.push_back(nums[i]);
            }
        }
        return unique;
    }
};

int main(){
    Solution solution;
    vector<int> nums = {3,2,3};
    cout << solution.majorityElement(nums) << endl; // 3
    return 0;
}