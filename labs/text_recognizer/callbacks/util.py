from __future__ import annotations

import logging

logging.basicConfig(level=logging.WARNING)


def check_and_warn(logger, attribute, feature):
    if not hasattr(logger, attribute):
        warn_no_attribute(feature, attribute)
        return True
    return False


def warn_no_attribute(blocked_feature, missing_attribute):
    message = f"Unable to log {blocked_feature}: logger does not have attribute {missing_attribute}."
    logging.warning(message)
