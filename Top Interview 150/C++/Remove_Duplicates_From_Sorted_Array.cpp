#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        short i = 0;
        while(i < nums.size() - 1){
            if(nums[i] == nums[i+1]) nums.erase(nums.begin() + i);
            else i++;
        }
        return nums.size();
    }
};

int main(){
    Solution s;
    vector<int> nums = {0,0,1,1,1,2,2,3,3,4};
    cout << s.removeDuplicates(nums) << endl; // 5
    for(int i = 0; i < nums.size(); i++){
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}