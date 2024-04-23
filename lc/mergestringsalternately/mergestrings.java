// here's my solution, it's pretty inelegant
class Solution {
  public String mergeAlternately(String word1, String word2) {
      String ret = "";
      int shorter = word1.length();
      if (word2.length() < word1.length()) {
          shorter = word2.length();
      }
      for(int i = 0; i < shorter; i++) {
          ret += "" + word1.charAt(i) + word2.charAt(i);
      }
      
      if (word1.length() == word2.length()) {
          return ret;
      }
      else if (shorter == word1.length()) {
          ret += word2.substring(shorter, word2.length());
      } else if (shorter == word2.length()) {
          ret += word1.substring(shorter, word1.length());
      }
      return ret;
  }
}

/*
 * here's a really fast (1ms!) solution. 
 * 
 *         StringBuilder result = new StringBuilder();
        int minLength = Math.min(word1.length(),word2.length());
        for(int i=0;i<minLength;i++){
            result.append(word1.charAt(i)).append(word2.charAt(i));
        }
        return result.append(word1.substring(minLength)).append(word2.substring(minLength)).toString();


        StringBuilder in Java represents a mutable sequence of characters 
        (the String Class in Java creates an immutable sequence of characters)
 */