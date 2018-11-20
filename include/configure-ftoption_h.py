#!/usr/bin/env python3

import os
import sys
import shutil

shutil.copy2(sys.argv[1], sys.argv[2])

with open(sys.argv[2], 'a') as f:
    for opt in ('SYSTEM_ZLIB', 'USE_BZIP2', 'USE_PNG', 'USE_HARFBUZZ'):
        f.write('#undef FT_CONFIG_OPTION_{}\n'.format(opt))
        f.write('#mesondefine FT_CONFIG_OPTION_{}\n'.format(opt))
