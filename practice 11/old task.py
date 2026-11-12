for b in range(11):
    for k in range(21):
        for t in range(201):
            if(20*b+10*k+t == 200) and (b+k+t>=1) and b>0 and k>0 and t>1:
                print(f"Быков {b}, Коров {k}, Телят {t}")
