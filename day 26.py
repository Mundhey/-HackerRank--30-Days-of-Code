ret_day,ret_month,ret_year = map(int,(raw_input().strip().split(' ')))

act_day,act_month,act_year= map(int,(raw_input().strip().split(' ')))


if(ret_year<act_year):
    fine=0
elif(ret_year==act_year and ret_month<act_month ):
    fine=0
elif(ret_year==act_year and ret_month==act_month and ret_day>act_day):
    fine=(ret_day-act_day)*15
elif(ret_year==act_year and ret_month>act_month):
    fine=(ret_month-act_month)*500
elif(ret_year>act_year):
    fine=1000


print fine