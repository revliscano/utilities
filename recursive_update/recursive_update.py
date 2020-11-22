from copy import deepcopy


def update(original_dict, new_dict):
    resultant_dict = _merge(original_dict, new_dict)
    _recursive_update(resultant_dict, new_dict)
    return resultant_dict


def _merge(original_dict, new_dict):
    merged = {
        **deepcopy(new_dict),
        **deepcopy(original_dict)
    }
    return merged


def _recursive_update(base, update):
    for key, value in update.items():
        if isinstance(value, dict):
            _recursive_update(base[key], value)
        else:
            base[key] = value
