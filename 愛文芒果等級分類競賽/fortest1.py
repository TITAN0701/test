all_score = []

for i in range(0, 3):
    print("第", i+1,"班")
    score_list = []
    
    for j in range(0,10):
        score = int(input('請輸入學生成績 : '))
        score_list += [score]

    all_score += [score_list]

for i, score_list in enumerate(all_score):
    print("第", i+1,"班，學生成績 : ",score_list)
        