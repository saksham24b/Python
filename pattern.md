 re.search(pattern, string, flags=0)
 
 .    | any character except newline  
 \*    | zero or more of the preceding character  
 \+    | one or more of the preceding character 
 ?    | zero or one of the preceding character
 {n}  | exactly n of the preceding character
 {n,} | n or more of the preceding character
 {n,m}| n to m of the preceding character
 ^    | start of the string  
 $    | end of the string
 \[]   | a set of characters
 \[^]  | a set of characters that are not allowed