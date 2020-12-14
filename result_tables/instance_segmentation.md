### Evaluated Instance Segmentation Models (Coming Soon)

|   Method   | Backbone | Epoch | Link to Config |  Model | Detections | LRP Results | oLRP ↓ | oLRP<sub>Loc</sub> ↓ | oLRP<sub>FP</sub> ↓ | oLRP<sub>FN</sub> ↓ | AP<sup>C</sup> ↑ | AP<sub>50</sub> ↑ | AP<sub>75</sub> ↑ | AR<sup>C</sup><sub>100</sub> ↑|
| :---------------------------: | :-------: | :-----: | :------------: | :------: | :-----:| :----------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: |
| Mask R-CNN | R50 | 24 | | | | | 70.7 | 18.5 | 28.5 | 47.0 | 35.4 | 56.4 | 37.9 | 48.1 |
| Mask R-CNN | R101 | 24 | | | | | 69.4 | 18.2 | 25.9 | 46.3 | 36.6 | 57.9 | 39.1 | 48.8 |
| Mask R-CNN | X101 | 12 | | | | | 67.8 | 18.3 | 24.9 | 43.5 | 38.4 | 60.6 | 41.3 | 50.3 |
| Cascade Mask R-CNN | X101 | 20 | | | | | 66.8 | 18.0 | 24.3 | 42.1 | 39.5 | 61.3 | 42.5 | 50.5 |
| Mask Scoring R-CNN | X101 | 12 | | | | | 67.5 | 17.9 | 24.5 | 43.3 | 39.5 | 60.5 | 42.6 | 50.1 |
| Hybrid Task Cascade | X101 | 20 | | | | | 63.6 | 17.0 | 23.4 | 37.9 | 43.8 | 66.8 | 47.1 | 57.4 |
