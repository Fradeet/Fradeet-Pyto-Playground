"""
Opens a Shortcut and retrieves the result.
"""

import xcallback
from urllib.parse import quote

#shortcut_name = input("The name of the shortcut to open: ")
#shortcut_input = input("What would you like to send to the Shortcut? ")

shortcut_name = "Pyto Version"
shortcut_name = quote(shortcut_name)
shortcut_input = "No"
shortcut_input = quote(shortcut_input)

url = f"shortcuts://run-shortcut?name={shortcut_name}&input=text&text={shortcut_input}"

try:
    res = xcallback.open_url(url)
    print("Result:\n"+res)
except RuntimeError as e:
    print("Error: "+str(e))
except SystemExit:
    print("Cancelled")
