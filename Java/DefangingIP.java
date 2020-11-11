/**
 * Leetcode Problem #1108. Defanging an IP Address
 * Given a valid (IPv4) IP address, return a defanged version of that IP address.
 * A defanged IP address replaces every period "." with "[.]".
 * 
 First way is simple (one liner):
 It uses a built in method called replace which if it sees '.' in the address string it will replace it everytime
 String modifiedIp = address.replace(".", "[.]");
       
        return modifiedIp;

For the second solution:
first I used a string builder. As strings in java immutable, string builder is mutable.
I used string builders append method to append each element within the string to the string builder that does not ocntain '.' if it does then instead of appending '.' append '[.]'
 */

class Solution {
    public String defangIPaddr(String address) {

        StringBuilder modifiedIp = new StringBuilder("");
        
        for(int i = 0; i < address.length(); i++) {
            if(address.charAt(i) != '.') {
                modifiedIp.append(address.charAt(i));
            } else {
                modifiedIp.append("[.]");
            }
            
        }
        
        
        return modifiedIp.toString();
    }
}