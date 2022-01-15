"""
A widget showing the current week day and date.
"""

import widgets as wd
from datetime import datetime, timedelta

BACKGROUND = wd.Color.rgb(255/255, 250/255, 227/255)
FOREGROUND = wd.Color.rgb(75/255, 72/255, 55/255)

class DateProvider(wd.TimelineProvider):

    def timeline(self):
        today = datetime.today()
        today = datetime.combine(today, datetime.min.time())

        dates = []
        for i in range(30):
            date = today + timedelta(days=i)
            dates.append(date)

        return dates

    def widget(self, date):
        widget = wd.Widget()
        layout = widget.medium_layout

        date_text = wd.DynamicDate(
            date=date,
            font=wd.Font("AmericanTypewriter", 18),
            color=FOREGROUND,
            padding=wd.PADDING_ALL)

        layout.add_vertical_spacer()
        layout.add_row([date_text])
        layout.set_background_color(BACKGROUND)
        layout.set_link(date.ctime())

        return widget

if wd.link is not None:
    print(wd.link)
else:
    wd.provide_timeline(DateProvider())
