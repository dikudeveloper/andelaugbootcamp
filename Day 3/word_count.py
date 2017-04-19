def words(word):
    if isinstance(word, str):
        if len(word):
            if "\t" in word:
                wlist =word.split("\t")
            elif "\n" in word:
                wlist =word.split("\n")
            else:
                wlist = word.split(" ")

            result = {}
            for i in wlist:
                if i.isdigit():
                    result[int(i)] = wlist.count(i)
                else:
                    result[i] = wlist.count(i)

            if "" in result:
                del result[""]
            return result