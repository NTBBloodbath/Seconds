import unittest
from seconds import Secs

class TestPush(unittest.TestCase):
    def test_convert_to_secs(self):
        # From minutes to seconds
        print("From minutes:")
        print(f"    2 minutes = {Secs('2m')}")
        print(f"    5 minutes = {Secs('5 mins')}")
        print(f"    10 minutes = {Secs('10 minutes')}", "\n")

        # From hours to seconds
        print("From hours:")
        print(f"    1 hour = {Secs('1h')}")
        print(f"    2 hours = {Secs('2 hrs')}")
        print(f"    3 hours = {Secs('3 hours')}", "\n")

        # From days to seconds
        print("From days:")
        print(f"    1 day = {Secs('1d')}")
        print(f"    2 days = {Secs('2 dys')}")
        print(f"    3 days = {Secs('3 days')}", "\n")

        # From weeks to seconds
        print("From weeks:")
        print(f"    1 week = {Secs('1w')}")
        print(f"    2 weeks = {Secs('2 wks')}")
        print(f"    3 weeks = {Secs('3 weeks')}", "\n")

        # From months to seconds
        print("From months:")
        print(f"    1 month = {Secs('1M')}") # It can also be mo
        print(f"    6 months = {Secs('6 mos')}")
        print(f"    12 months = {Secs('12 months')}", "\n")

        # From years to seconds
        print("From years:")
        print(f"    1 year = {Secs('1y')}")
        print(f"    2 years = {Secs('2 yrs')}")
        print(f"    3 years = {Secs('3 years')}", "\n\n")

    def test_secs_to_time(self):
        # From seconds to minutes
        print("To minutes:")
        print(f"    60 secs = {Secs(60)}")
        print(f"    600 secs = {Secs(600, abbrev=True)}", "\n")
        # From seconds to hours
        print("To hours:")
        print(f"    3600 secs = {Secs(3600)}")
        print(f"    7200 secs = {Secs(7200, abbrev=True)}", "\n")
        # From seconds to days
        print("To days:")
        print(f"    86400 secs = {Secs(86400)}")
        print(f"    172800 secs = {Secs(172800, abbrev=True)}", "\n")
        # From seconds to weeks
        print("To weeks:")
        print(f"    604800 secs = {Secs(604800)}")
        print(f"    1209600 secs = {Secs(1209600, abbrev=True)}", "\n")
        # From seconds to months
        print("To months:")
        print(f"    18408600 secs = {Secs(18408600)}")
        print(f"    110451600 secs = {Secs(110451600, abbrev=True)}", "\n")
        # From seconds to years
        print("To years:")
        print(f"    220903200 secs = {Secs(220903200)}")
        print(f"    441806400 secs = {Secs(441806400, abbrev=True)}", "\n")

if __name__ == '__main__':
    unittest.main()
