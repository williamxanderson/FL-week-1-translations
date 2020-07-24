#!/usr/bin/python3
#!/usr/bin/env python
import os, sys, codecs

def find_missing_strings(f, fp):
    lines = fp.readlines()
    j = 0
    untranslated_lines = []
    for i in range(len(lines)-1):
        if lines[i].startswith("    # \""):
            if lines[i+1][4:].strip() == lines[i][6:].strip():
                untranslated_lines.append(i+2)
        elif lines[i].startswith("    old"):
            if lines[i+1][8:].strip() == lines[i][8:].strip():
                untranslated_lines.append(i+2)
    if len(untranslated_lines) > 0:
        output_file.write(u"File: {0}\n\n".format(f))
        for i in untranslated_lines:
            try:
                output_file.write(u"{0}: {1}\n".format(i, lines[i-1].strip()))
            except:
                output_file.write(u"{0}: unparsed line\n".format(i))
        output_file.write(u"\n")

is_python3 = (sys.version_info > (3, 0))

if is_python3:
    output_file = open("./check_translations.txt", 'w', encoding='utf-8')
else:
    output_file = codecs.open("./check_translations.txt", 'w', encoding='utf-8')

languages = ("./deutsch", "./italian", "./russian")

for l in languages:
    output_file.write(u"{1} Language: {0} {1}\n\n".format(l[2:], "=" * 30))
    path = os.path.join(l, "code/")
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(path) for f in filenames if os.path.splitext(f)[1] == '.rpy']
    for f in files:
        with (open(f, encoding='utf-8') if is_python3 else codecs.open(f, encoding='utf-8')) as fp:
            find_missing_strings(f, fp)
output_file.close()
