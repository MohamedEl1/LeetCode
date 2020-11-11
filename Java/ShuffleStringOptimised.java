public static String restoreString(String s, int[] indices) {

    // use string builder to arrange characters accordingly

    StringBuilder ShuffledString = new StringBuilder("");
    ShuffledString.setLength(s.length());
    for (int i = 0; i < s.length(); i++) {

        // set the character of i to index of indices
        ShuffledString.setCharAt(indices[i], s.charAt(i)); // sets the character 'c' at index 4 (basically overrides the element at that specified index)
    }

    return ShuffledString.toString();
}