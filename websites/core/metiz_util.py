

def remove_uni(s):
    """remove the leading unicode designator from a string"""
    try:
        s2 = ""
        if s.startswith("[u'"):
            s2 = s.replace("u'", "'")
        elif s.startswith('[u"'):
            s2 = s.replace('u"', '"')
    except Exception, e:
        print "ERROR ",e
        return s
    return s if not s2 else s2