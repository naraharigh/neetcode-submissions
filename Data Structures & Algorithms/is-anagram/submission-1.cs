public class Solution {
    public bool IsAnagram(string s, string t) {

        if (s.Length != t.Length )
        {
            return false;
        }
        char[] s1 = s.ToCharArray();
        Array.Sort(s1);

        char[] t1 = t.ToCharArray();
        Array.Sort(t1);



        for (int i = 0; i< s.Length ; i++)
        {
            if (s1[i] != t1[i])
            {
                return false;
            }
        }


        return true;
    }
}
