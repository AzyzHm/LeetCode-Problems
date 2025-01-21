#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        for(short i = 0;i < nums.size();++i){
            if (nums[i] == val)nums.erase(i + nums.begin()),--i;
        }
        return nums.size();
    }
};

int main(){
    Solution s;
    vector <int> nums = {3,2,2,3};
    int val = 3;
    cout << s.removeElement(nums,val) << endl; // 2
    return 0;
}