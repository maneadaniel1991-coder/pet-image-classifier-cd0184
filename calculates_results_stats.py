def calculates_results_stats(results_dic):
    s = {"n_images":0,"n_dogs_img":0,"n_notdogs_img":0,"n_match":0,
         "n_correct_dogs":0,"n_correct_notdogs":0,"n_correct_breed":0,
         "pct_match":0.0,"pct_correct_dogs":0.0,"pct_correct_breed":0.0,"pct_correct_notdogs":0.0}
    for v in results_dic.values():
        pet_label, clabel, match, isdog_pet, isdog_cls = v
        s["n_images"] += 1
        if match == 1: s["n_match"] += 1
        if isdog_pet == 1:
            s["n_dogs_img"] += 1
            if isdog_cls == 1:
                s["n_correct_dogs"] += 1
                if match == 1: s["n_correct_breed"] += 1
        else:
            s["n_notdogs_img"] += 1
            if isdog_cls == 0: s["n_correct_notdogs"] += 1
    if s["n_images"]>0: s["pct_match"]=100*s["n_match"]/s["n_images"]
    if s["n_dogs_img"]>0:
        s["pct_correct_dogs"]=100*s["n_correct_dogs"]/s["n_dogs_img"]
        s["pct_correct_breed"]=100*s["n_correct_breed"]/s["n_dogs_img"]
    if s["n_notdogs_img"]>0:
        s["pct_correct_notdogs"]=100*s["n_correct_notdogs"]/s["n_notdogs_img"]
    return s
