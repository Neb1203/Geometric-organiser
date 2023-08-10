def removeSpeach(txt):
    if txt.startswith('"') and txt.endswith('"'):
        return txt[1:-1]
    else:
        return txt