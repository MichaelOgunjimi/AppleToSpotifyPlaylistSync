import datetime


def get_current_day_of_week():
    # Get the current date
    current_date = datetime.date.today()
    # Get the name of the day
    day_name = current_date.strftime("%A")
    return day_name


def find_none_indices(track_uris):
    indices = []
    for i, uri in enumerate(track_uris):
        if uri is None:
            indices.append(i)
    return indices
