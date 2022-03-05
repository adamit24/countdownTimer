import time



def timerCountdown(t):
    while t:
        min, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, secs)
        print('\r',timer,end='')
        time.sleep(1)
        t -= 1

    print('\n Timer Completed')


t = input('Please enter the time in seconds: \n')

timerCountdown(int(t))
