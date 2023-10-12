#MKHABELE MMM
#28/06/2023
def main():
    t=input("What time is it? ")

    newtime=convert(t)
    if 7.00<=newtime<=8.00:
        print("breakfast time")
    if 12.00<=newtime<=13.00:
        print('lunch time')
    if 18.00<=newtime<=19.00:
        print("dinner time")
def convert(time):
    hrs,min=time.split(":")
    newtime=float(hrs) +float(min)/60 #convert to hrs
    return newtime

if __name__ == "__main__":
    main()
