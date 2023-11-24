# (2-1)1時間は何秒か？
print(60*60)
# (2-2)1時間の秒数を変数に入れる．seconds_per_hour
seconds_per_hour = 60*60
print(seconds_per_hour)
# (2-3)1日は何秒か？seconds_per_hour
seconds_per_hour = 24 * 60 * 60
print(seconds_per_hour)
# (2-4)1日の秒数をもう一度計算しよう．seconds_per_day
seconds_per_day = 24 * 60 * 60
print(seconds_per_day)
# (2-5)seconds_per_dayをseconds_per_hourで割る．
print(seconds_per_day / seconds_per_hour)
# (2-6)整数除算を使って，seconds_per_dayをseconds_per_hourで割る．
print(seconds_per_day // seconds_per_hour)
