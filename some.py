import string
table = string.ascii_letters
table = list(table)
for i in table:
    try:
        exec("%s = '%s'" % (i,i))

    except:
        pass
    for t in table:
        try:
            exec("%s = '%s'" % (i+t,i+t))
        except:
            pass
        for k in table:
            try:
                exec("%s = '%s'" % (i+t+k,i+t+k))
            except:
                pass
            for m in table:
                try:
                    exec("%s = '%s'" % (i+t+k+m,i+t+k+m))
                except:
                    pass
                for h in table:
                    try:
                        exec("%s = '%s'" % (i+t+k+m+h,i+t+k+m+h))
                    except:
                        pass
print(hello)
