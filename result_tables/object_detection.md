### Evaluated Object Detection Models (Coming Soon)

|   Method   | Backbone | Epoch | Link to Config |  Model | Detections | LRP Results | oLRP | oLRP<sub>Loc</sub> | oLRP<sub>FP</sub> | oLRP<sub>FN</sub> | AP<sup>C</sup> | AP<sub>50</sub> | AP<sub>75</sub> | AR<sup>C</sup><sub>100</sub>|
| :---------------------------: | :-------: | :-----: | :------------: | :------: | :-----:| :----------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: |
| SSD-300 | VGG-16 | 120 | [mmdetection](https://github.com/open-mmlab/mmdetection/blob/master/configs/ssd/ssd300_coco.py) | [model](https://drive.google.com/file/d/1pASqIfWRAJICBGW2MPwVW3C8pquA-pqV/view?usp=sharing) | [json](https://drive.google.com/file/d/1vt0Gn5El4st31_CUJqq_Gaf1VlLdqpan/view?usp=sharing) |[txt](https://drive.google.com/file/d/1kfXbmKPyoLvtBpFJKPGeIWMGphdYMoWC/view?usp=sharing)| 78.4 | 20.6 | 37.1 | 57.9 | 25.6 | 43.8 | 26.3 | 37.5 |
| SSD-512 | VGG-16 | 120 | | | | | 75.4 | 19.7 | 32.8 | 53.6 | 29.4 | 49.3 | 31.0 | 42.5 |
| RetinaNet | R50 | 12 | | | | | 71.0 | 17.0 | 29.1 | 50.0 | 35.7 | 54.7 | 38.5 | 52.0 |
| RetinaNet | R50 | 24 | | | | | 70.6 | 17.1 | 28.4 | 49.6 | 35.7 | 54.9 | 38.2 | 51.4 |
| RetinaNet | X101 | 24 | | | | | 67.5 | 16.1 | 24.5 | 46.3 | 39.2 | 59.2 | 41.8 | 53.5 |
| ATSS | R50 | 12 | | | | | 68.6 | 15.4 | 30.3 | 46.6 | 39.4 | 57.6 | 42.8 | 58.3 |
| RetinaNet | X101 | 12 | | | | | 67.6 | 16.1 | 25.3 | 46.2 | 39.8 | 59.5 | 43.0 | 54.8 |
| NAS-FPN | R50 | 50 | | | | | 66.7 | 14.8 | 26.6 | 46.3 | 40.5 | 58.4 | 43.1 | 55.6 |
| GHM | X101 | 12 | | | | | 66.3 | 15.6 | 27.1 | 44.2 | 41.4 | 60.9 | 44.2 | 57.7 |
| FreeAnchor | X101 | 12 | | | | | 66.0 | 15.2 | 26.4 | 44.5 | 41.9 | 61.0 | 45.0 | 58.6 |
| FCOS | X101 | 24 | | | | | 64.4 | 14.9 | 25.4 | 41.9 | 42.5 | 62.1 | 45.7 | 58.2 |
| RPDet | X101 | 24 | | | | | 63.3 | 15.4 | 23.4 | 39.5 | 44.2 | 65.5 | 47.8 | 58.7 |
| aLRP Loss | X101 | 100 | | | | | 62.5 | 15.1 | 23.2 | 39.5 | 45.4 | 66.6 | 48.0 | 60.3 |

