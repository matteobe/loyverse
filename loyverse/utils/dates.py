"""
Date (datetime objects) manipulation methods
"""

import pytz
from datetime import datetime


def add_timezone(date: datetime, timezone_id: str) -> datetime:
    """
    Localize a datetime object

    Args:
        date (datetime): date + time to be localized
        timezone_id (str): timezone identifier to be used for localizing date (e.g. Europe/Zurich).
            For a list of available identifiers, check the
            `tz database <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_.
    Returns:
        date_local (datetime): localized datetime object
    """

    timezone = pytz.timezone(timezone_id)
    date_local = timezone.localize(date)

    return date_local


def utc_isoformat(date: datetime, timezone_id: str = None) -> str:
    """
    Format datetime object using the ISO8601 format to UTC timezone

    Args:
        date (datetime): date + time to be converted into ISO8601 format (can be timezone aware).
        timezone_id (str): timezone identifier to be used for conversion to UTC time (e.g. Europe/Zurich).
            For a list of available identifiers, check the
            `tz database <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_.
    Returns:
        date_str (str): date + time converted to UTC timezone and ISO format (e.g. 2020-10-12T23:14:59.897Z)
    """

    if timezone_id is None:
        date_aware = date

        if date.tzinfo is None:
            raise ValueError('Either a timezone-aware date or a timezone-id has to be passed in.')
    else:
        date_aware = add_timezone(date, timezone_id)

    date_utc = date_aware.astimezone(pytz.utc)
    date_str = date_utc.isoformat(sep='T', timespec='milliseconds')[:23] + 'Z'

    return date_str


def day_start(date: datetime) -> datetime:
    """
    Calculates day start for passed in date object

    Args:
        date (datetime): datetime object, for which to calculate the start of the day
    Returns:
        date_start (datetime): timestamp for start of the given date
    """

    return datetime(date.year, date.month, date.day, 0, 0, 0, 0, tzinfo=date.tzinfo)


def day_end(date: datetime) -> datetime:
    """
    Calculates end of date

    Args:
        date (datetime): datetime object, for which to calculate the end of the day
    Returns:
        date_end (datetime): timestamp for end of the given date
    """

    return datetime(date.year, date.month, date.day, 23, 59, 59, 999999, tzinfo=date.tzinfo)
