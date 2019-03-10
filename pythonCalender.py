#python printline Calendar
import calendar
c= calendar.TextCalendar(calendar.SUNDAY)
str=c.formatmonth(2020,6)
print(str)
#html Calendar
hc=calendar.HTMLCalendar(calendar.SUNDAY)
form=hc.formatmonth(2025,1)
print(form)
