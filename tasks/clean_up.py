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
    pr_dirs = []
    for job_dir in job_dirs:
        # Save upper directory to remove later (pr_xx)
        pr_dirs.append(os.path.dirname(job_dir))

    # Remove event_xxx-yyy/run_nnn/ directories
    pr_dirs = list(set(pr_dirs))  # get only unique dirs
    for pr_dir in pr_dirs:
        destination_dir = shutil.copytree(pr_dir, trash_bin_dir)
        log(f"{funcname}(): copied {pr_dir} to {destination_dir}")
        shutil.rmtree(pr_dir)  # Use shutil.rmtree to remove directories recursively
        log(f"{funcname}(): removed {pr_dir}")

    return True
