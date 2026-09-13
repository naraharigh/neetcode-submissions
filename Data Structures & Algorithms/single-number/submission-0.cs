public class Solution {
    public int SingleNumber(int[] nums) {
        bool flag = false;
        for (int i = 0;i< nums.Length; i++ )
        {
            flag = false;
            for(int j =0 ; j < nums.Length ; j++)
            {
                if ((i != j )  && (nums[i] == nums[j]))
                {
                    flag = true;
                }
            }
            if (flag == false)
            {
                return nums[i];
            }

        }

        return -1;
        
    }
}
