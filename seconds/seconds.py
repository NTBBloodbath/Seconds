# Seconds is distributed under MIT License #
#==========================================#

import inspect

class Secs:
    """
    Seconds class
    """

    # Default options
    abbrev = False

    def __new__(cls, time, **options):
        """
        Set the time to convert and the output options.

        ...

        Parameters
        ----------
        time
            The time that will be converted.
        options
            The options that control the output.

        Raises
        ------
        TypeError
            if time isn't a String or an Integer.
        """

        if not isinstance(time, (str, int)): #or not isinstance(time, int):
            raise TypeError(f"time must be a String or an Integer in \"{inspect.currentframe().f_code.co_name}\".")
        else:
            # Get options
            if "abbrev" in options:
                # Raise error if abbrev isn't a Boolean.
                if not isinstance(options["abbrev"], bool):
                    raise TypeError(
                        "abbrev must be a Boolean in options parameter in options parameter in \"{inspect.currentframe)(.f_code.co_name)}\".")
                else:
                    cls.abbrev = options["abbrev"]
            return cls.convert(cls, time)

    def convert(self, time):
        """
        Convert time from seconds to other times and vice versa

        ...

        Parameters
        ----------
        time
            The time which will be converted.
        """

        # Set the time variables
        secs = 1
        mins = secs * 60
        hrs = mins * 60
        dys = hrs * 24
        wks = dys * 7
        mos = wks * 30.4375
        yrs = mos * 12

        # Convert seconds to other time (minutes, hours, days, etc.)
        if isinstance(time, int):
            try:
                abs_time = abs(time)
                # To minutes
                if abs_time >= mins and abs_time < hrs:
                    return self.pluralize(self, time, abs_time, mins, "minute") if self.abbrev else str(round(time // mins)) + "m"
                # To hours
                if abs_time >= hrs and abs_time < dys:
                    return self.pluralize(self, time, abs_time, hrs, "hour") if self.abbrev else str(round(time // hrs)) + "h"
                # To days
                if abs_time >= dys and abs_time < wks:
                    return self.pluralize(self, time, abs_time, dys, "day") if self.abbrev else str(round(time // dys)) + "d"
                # To weeks
                if abs_time >= wks and abs_time < mos:
                    return self.pluralize(self, time, abs_time, wks, "week") if self.abbrev else str(round(time // wks)) + "w"
                # To months
                if abs_time >= mos and abs_time < yrs:
                    return self.pluralize(self, time, abs_time, mos, "month") if self.abbrev else str(round(time // mos)) + "mo"
                # To years
                if abs_time >= yrs:
                    return self.pluralize(self, time, abs_time, yrs, "year") if self.abbrev else str(round(time // yrs)) + "y"
            except Exception as err:
                print(f"[ERROR]: {err} in \"{inspect.currentframe().f_code.co_name}\".")
                exit(1)
        # Convert minutes, hours, days, etc. to seconds
        elif isinstance(time, str):
            try:
                # If time is in minutes
                if time.endswith("m"):
                    return int(time.replace("m", "")) * mins
                elif time.endswith("min"):
                    return int(time.replace("min", "")) * mins
                elif time.endswith("mins"):
                    return int(time.replace("mins", "")) * mins
                elif time.endswith("minute"):
                    return int(time.replace("minute", "")) * mins
                elif time.endswith("minutes"):
                    return int(time.replace("minutes", "")) * mins
                # If time is in hours
                if time.endswith("h"):
                    return int(time.replace("h", "")) * hrs
                elif time.endswith("hr"):
                    return int(time.replace("hr", "")) * hrs
                elif time.endswith("hrs"):
                    return int(time.replace("hrs", "")) * hrs
                elif time.endswith("hour"):
                    return int(time.replace("hour", "")) * hrs
                elif time.endswith("hours"):
                    return int(time.replace("hours", "")) * hrs
                # If time is in days
                if time.endswith("d"):
                    return int(time.replace("d", "")) * dys
                elif time.endswith("dy"):
                    return int(time.replace("dy", "")) * dys
                elif time.endswith("dys"):
                    return int(time.replace("dys", "")) * dys
                elif time.endswith("day"):
                    return int(time.replace("day", "")) * dys
                elif time.endswith("days"):
                    return int(time.replace("days", "")) * dys
                # If time is in weeks
                if time.endswith("w"):
                    return int(time.replace("w", "")) * wks
                elif time.endswith("wk"):
                    return int(time.replace("wk", "")) * wks
                elif time.endswith("wks"):
                    return int(time.replace("wks", "")) * wks
                elif time.endswith("week"):
                    return int(time.replace("week", "")) * wks
                elif time.endswith("weeks"):
                    return int(time.replace("weeks", "")) * wks
                # If time is in months
                if time.endswith("M"):
                    return round(int(time.replace("M", "")) * mos)
                elif time.endswith("mo"):
                    return round(int(time.replace("mo", "")) * mos)
                elif time.endswith("mos"):
                    return round(int(time.replace("mos", "")) * mos)
                elif time.endswith("month"):
                    return round(int(time.replace("month", "")) * mos)
                elif time.endswith("months"):
                    return round(int(time.replace("months", "")) * mos)
                # If time is in years
                if time.endswith("y"):
                    return round(int(time.replace("y", "")) * yrs)
                elif time.endswith("yr"):
                    return round(int(time.replace("yr", "")) * yrs)
                elif time.endswith("yrs"):
                    return round(int(time.replace("yrs", "")) * yrs)
                elif time.endswith("year"):
                    return round(int(time.replace("year", "")) * yrs)
                elif time.endswith("years"):
                    return round(int(time.replace("years", "")) * yrs)
            except Exception as err:
                print(f"[ERROR]: {err} in \"{inspect.currentframe().f_code.co_name}\".")
                exit(1)

    def pluralize(self, time, abs_time, time_type, name: str):
        """
        Pluralize the output if time is greater than 1.

        ...

        Parameters
        ----------
        time
            The time which will be pluralized.
        abs_time
            The absolute time.
        time_type
            The time type (mins, hrs, etc.).
        name
            The time name (minute, hour, etc.).
        """

        try:
            plural = abs_time >= time_type * 1.5
            return str(round(time // time_type)) + ' ' + name + ('s' if plural else '')
        except Exception as err:
            print(f"[ERROR]: {err} in \"{inspect.currentframe().f_code.co_name}\".")
            exit(1)

