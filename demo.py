from ctypes_termkey import TermKey, Result, KeyType, KeyModifier

tk = TermKey()

result_str_map = {
    Result.NONE: 'None',
    Result.KEY: 'Key',
    Result.EOF: 'EOF',
    Result.AGAIN: 'AGAIN',
}

while True:
    result, key = tk.waitkey()
    print "*** result", result_str_map[result]
    keystr = tk.sprint_key(key)
    print "    keystr", repr(keystr)

    if keystr == 'C-C':
        break

tk.close()
