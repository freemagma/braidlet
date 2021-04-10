def parse_braid(s, braids):
    # TODO implement this
    s = s.lower().strip().replace("[", "").replace("]", "")
    b_ix = s.find("b")
    if b_ix != -1:
        b_id = int(s[(b_ix + 1) :])
        if b_id >= len(braids):
            return None
        return parse_braid(braids[b_id]["input_form"], braids)
    if "," in s:
        return [int(x) for x in s.split(",") if x]
    else:
        return [int(x) for x in s.split(" ") if x]