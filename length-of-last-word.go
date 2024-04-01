func lengthOfLastWord(s string) int {
    startAt := -1
    endAt := -1
    for i := len(s) - 1; i >= 0; i-- {
        if startAt == -1 && s[i] >= 'A' {
            startAt = i
        } else if startAt != -1 && s[i] == ' ' {
            endAt = i
            break
        }
    }

    return startAt - endAt
}
