func isIsomorphic(s string, t string) bool {
    // Create two arrays to store the frequency of characters in the strings
    map1 := make([]int, 128) // Stores the frequency of characters in string s
    map2 := make([]int, 128) // Stores the frequency of characters in string t
    
    // Iterate through each character of the strings
    for i := 0; i < len(s); i++ {
        sCh := s[i] // Get the current character in string s
        tCh := t[i] // Get the current character in string t
        
        // Check if both characters are not mapped yet
        if map1[sCh] == 0 && map2[tCh] == 0 {
            map1[sCh] = int(tCh) // Map character from s to t
            map2[tCh] = int(sCh) // Map character from t to s
        } else if map1[sCh] != int(tCh) || map2[tCh] != int(sCh) {
            return false // If the mapping is not consistent, strings are not isomorphic
        }
    }
    
    return true // If the loop completes without returning false, strings are isomorphic
}
