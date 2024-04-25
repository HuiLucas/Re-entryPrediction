#!/bin/bash --login
# The --login ensures the bash configuration is loaded,
# enabling Conda.

# Enable strict mode.
set -euo pipefail
# ... Run whatever commands ...


# Temporarily disable strict mode and activate conda:
set +euo pipefail
conda activate tudat-space

# Re-enable strict mode:
set -euo pipefail
echo something
pip install -r requirements.txt
echo something2
conda list -n tudat-space
# exec the final command:
exec python main.py
