public class Solution {
    public bool IsPalindrome(int x) {
       string str = Convert.ToString(x);
       char [] arr1 = str.ToCharArray();
       Array.Reverse(arr1);
       string rev = new string(arr1);
       return str == rev;
        
    }
}