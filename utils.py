def find_none_indices(track_uris):
    indices = []
    for i, uri in enumerate(track_uris):
        if uri is None:
            indices.append(i)
    return indices
