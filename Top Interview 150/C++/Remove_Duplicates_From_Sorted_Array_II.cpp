#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        for(int i=0;i<nums.size();i++){
            if(countOccurences(nums,nums[i]) > 2){
                nums.erase(nums.begin()+i);
                i--;
            }
        }
        return nums.size();
    }
private:
    int countOccurences(vector<int>& nums,int val){
        int count = 0;
        for(int i=0;i<nums.size();i++){
            if(nums[i] == val){
                count++;
            }
        }
        return count;
    }
};

int main(){
    Solution s;
    vector<int> nums = {1,1,1,2,2,3}; // 5
    cout << s.removeDuplicates(nums) << endl;
    for(int i=0;i<nums.size();i++){
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}