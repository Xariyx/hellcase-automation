# hellcase-automation
Collection of python scripts that help automate obtaining daily rewards.

# requirements
- requests library
- python2+
- account created on hellcase

# editing config files
Before using any of these scripts you must edit config.json file
- xsrf is a token that is obtained from XSRF-TOKEN cookie from your browser, it doesn't need to be replaced every so often
- session is a session token that can be obtained from hellcase_session cookie, it must be replaced every session closage or 30 days

# obtaining tokens from cookies
To obtain tokens needed in config.json you should:
- go to hellcase.com
- login via steam link
- press F12 when on main page of hellcase
- go down into data section
- search for cookies at https://hellcase.com
- copy values from browser into config.json file
Some values need to be replaced every so often.

# usage of scripts
My preffered way of using these scripts is to set up crohntab job every 1450 mins (24h + 10min).
You can use raspberrypi or anything else that supports python, personally i'm using ASUS RT-N18U with Advanced Tomato + USB Stick containing files.
