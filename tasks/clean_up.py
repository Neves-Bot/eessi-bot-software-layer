# This file is part of the EESSI build-and-deploy bot,
# see https://github.com/EESSI/eessi-bot-software-layer
#
# The bot helps with requests to add software installations to the
# EESSI software layer, see https://github.com/EESSI/software-layer
#
# author: Pedro Santos Neves (@Neves-P)
#
# license: GPLv2
#

# Standard library imports
import sys
import os
import shutil

# Third party imports (anything installed into the local Python environment)
from pyghee.utils import log

# Local application imports (anything from EESSI/eessi-bot-software-layer)


def move_to_trash_bin(trash_bin_dir, job_dirs):
    """
    Move directory to trash_bin_dir

    Args:
        trash_bin_dir (string): path to the trash_bin_dir. Defined in .cfg
        job_dirs (list): list with job directory names

    Returns:
        None (implicitly)
    """
    funcname = sys._getframe().f_code.co_name
    log(f"{funcname}(): trash_bin_dir = {trash_bin_dir}")

    os.makedirs(trash_bin_dir, exist_ok=True)
    for job_dir in job_dirs:
        destination_dir = shutil.move(job_dir, trash_bin_dir)
        log(f"{funcname}(): moved {job_dir} to {destination_dir}")
    return True