months = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}

date_out = [0, 1, 2]

while True:
    date_in = input("Enter Date: ")
    if "/" in date_in:
        try:
            date_slash = date_in.strip().split("/")
            if len(date_slash[0]) == 1:
                date_slash[0] = "0" + date_slash[0]
            if len(date_slash[1]) == 1:
                date_slash[1] = "0" + date_slash[1]
        except IndexError:
            pass
        else:
            try:
                int(date_slash[0])
                int(date_slash[1])
                int(date_slash[2])
            except ValueError:
                pass
            else:
                if 1 > int(date_slash[0]) or int(date_slash[0]) > 12:
                    pass
                elif 1 > int(date_slash[1]) or int(date_slash[1]) > 31:
                    pass
                else:
                    date_out = date_slash
                    break
    elif "," in date_in:
        try:
            m, d, y = date_in.split()
        except ValueError:
            pass
        else:
            m = m.title()
            try:
                date_out[0] = months[m]
            except KeyError:
                pass
            else:
                d = d.strip(",")
                if len(d) == 1:
                    d = "0" + d
                date_out[1] = d
                date_out[2] = y
                if int(date_out[1]) > 31 or int(date_out[1]) < 1:
                    pass
                else:
                    break
    else:
        pass





print(date_out[2], date_out[0], date_out[1], sep="-")
