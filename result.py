from util.plot_utils import plot_logs
from pathlib import Path

#directory = 'output/202112217-'
directory = "D:/ishida workspace/detr_SOD ver.3/detr/output/VJx-"
log_directory = [Path(directory)]

fields_of_interest = (
    'mAP`',
)

plot_logs(directory=directory,
          logs=log_directory,
          fields=fields_of_interest)



