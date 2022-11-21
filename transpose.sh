# Read from the file file.txt and print its transposed content to stdout.
#Given a text file file.txt, transpose its content.
#You may assume that each row has the same number of columns, and each field is separated by the ' ' character.

awk '
{
    for (i=1; i<=NF; i++)  {
        if (NR == 1) {
            s[i] = $i
        } else {
            s[i] = s[i]" "$i
        }
    }
}
END {
    for (i=1; s[i]!=""; i++) {
        print s[i]
    }
}' file.txt