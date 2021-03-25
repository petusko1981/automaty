step = 1 #nemenit
win = 12.6 #zadatjte hodnotu winu ktory ma zacat gamble
cwin = 1 #ak chcete prehrat poslednom kroku dajte 0 ak neprehrat realny cwin kontrola este neni
count = 2 #pocer risky games
startbet = win
tbet = 0 
twin = 0

win = float(input('Zadajte pociatocny, win stavku do gamble: '))
count = int(input('Zadajte pocet gamble: '))
cwin = float(input('zadajte cwin pre kontrolu ak ma prehrat daj 0 :'))
win = round(win,2)

if cwin>0:
    while (step <= count):
        startbet = startbet
        gabmlewin = startbet * 2
        print('Gamble step: {} Bet: {} win: {}'.format(step, startbet, gabmlewin))
        tbet += startbet
        twin += gabmlewin
        startbet = gabmlewin
        step+=1


elif cwin==0:
    laststep = count - 1
    while (step <= count):
        if step <= laststep:
            gabmlewin = startbet * 2
            print('Gamble step: {} Bet: {} win: {}'.format(step, startbet, gabmlewin))
            tbet += startbet
            twin += gabmlewin
            startbet = gabmlewin
            step+=1
        else:
            gabmlewin = 0
            print('Gamble step: {} Bet: {} win: {}'.format(step, startbet, gabmlewin))
            tbet += startbet
            twin += gabmlewin
            step += 1
twin = round(twin,2)
tbet= round(tbet,2)
zisk = twin - tbet
zisk = round(zisk,2)
vyhernost =  twin / tbet
vyhernost = round(vyhernost,2)
vyhernot = vyhernost * 100
print('Total Gamblebet {} Total Gamblewin {} zisk(RISKYCWIN) {} vyhernost % {}'.format(tbet, twin, zisk, vyhernot))




