# One Metric to Measure them All: Localisation Recall Precision (LRP) for Evaluating Visual Detection Tasks

The official implementation of LRP Error [1, 2]. This repository contains the implementation of LRP Error on following evaluation apis:

- Official COCO api [3] to evaluate object detection, keypoint detection and instance segmentation (pycocotools folder) 
- Official COCO panoptic api [4] to evaluate panoptic segmentation (panopticapi folder)

> [**One Metric to Measure them All: Localisation Recall Precision (LRP) for Evaluating Visual Detection Tasks**](https://arxiv.org/abs/2009.13592),            
> [Kemal Oksuz](https://kemaloksuz.github.io/), Baris Can Cam, , [Sinan Kalkan](http://www.kovan.ceng.metu.edu.tr/~sinan/), [Emre Akbas](http://user.ceng.metu.edu.tr/~emre/),
> ([arXiv pre-print](https://arxiv.org/abs/2009.13592))*

For mmdetection COCO api [5] to evaluate object detection, keypoint detection and instance segmentation [see this repository](https://github.com/kemaloksuz/cocoapi).

## Summary

In a nutshell, LRP Error (previously proposed only for object detection in [4])

- is an alternative to average precision (AP) for object detection, keypoint detection and instance segmentation
- is an alternative to panoptic quality (PQ) for panoptic segmentation 
- can be extended to evaluate other visual detection tasks such as 3D object detection etc.
- can be used to assign class-wise optimal thresholds for practical needs

## Benefits of LRP Compared to AP and PQ

In our paper, we first define three important features for a performance measure to evaluate visual object detection tasks, then analyse AP, PQ and LRP based on these features. Finally, in order experiments, again based on these important features and our analysis, we empirically demonstrate the drawbacks of AP and PQ, and discuss how LRP alleviates these drawbacks.

### Important features for a performance measure

Three important features for a performance measure to evaluate visual object detection tasks are:

- Completeness: We call a performance measure ``complete'' if it precisely  takes into account three most important  performance aspects in a visual detection task, that are false positive (FP) rate, false negative (FN) rate and localisation error.

- Interpretability: Interpretability of a performance measure is related to its ability to provide insights on the strengths and weaknesses of the detector being evaluated.
  
- Practicality. Any issue that arises during  practical use of a performance measure diminishes its practicality. 

### Definition and Intuition of LRP
LRP Error is defined as  the ``average matching error'', where the ``total matching error'' between ground truth set (G) and detection set (D) is normalised by  $Z$, the ``maximum possible value of the total matching error'': 

![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cmathrm%7BLRP%7D%28%5Cmathcal%7BG%7D%2C%5Cmathcal%7BD%7D%29%3A%3D%20%5Cfrac%7B1%7D%7BZ%7D%20%5Cleft%28%20%5Csum%20%5Climits_%7Bi%3D1%7D%5E%7B%5Cmathrm%7BN_%7BTP%7D%7D%7D%20%20%5Cfrac%7B1-%5Cmathrm%7Blq%7D%28g_i%2C%20d_%7Bg_i%7D%29%7D%7B1-%5Ctau%7D%2B%5Cmathrm%7BN_%7BFP%7D%7D%20%2B%20%5Cmathrm%7BN_%7BFN%7D%7D%20%5Cright%29%2C%20%5Ctext%7B%20where%20%7D%20Z%3D%5Cmathrm%7BN_%7BTP%7D%7D%2B%5Cmathrm%7BN_%7BFP%7D%7D%20%2B%20%5Cmathrm%7BN_%7BFN%7D%7D&bc=White&fc=Black&im=jpg&fs=12&ff=modern&edit=0)

As a result, a TP contributes to the total matching error by its localization error normalized by 1-\tau to ensure that the value is in interval [0,1]. And, each FP or FN contributes to the total matching error by 1. Finally, normalisation by Z ensures  LRP has a range of [0,1].

LRP can directly be used to evaluate panoptic segmentation since the outputs do not contain confidence scores. As for the outputs with confidence scores such the ones in object detection, keypoint detection and instance segmentation, we define Optimal LRP (oLRP) as the minimum achievable LRP Error over the confidence scores. 

### Comparison of LRP with AP and PQ (Coming Soon)


## How to Cite

Please cite the paper if you benefit from our paper or repository:
```
@article{LRP,
       title = {One Metric to Measure them All: Localisation Recall Precision (LRP) for Evaluating Visual Detection Tasks},
       author = {Kemal Oksuz and Baris Can Cam and Sinan Kalkan and Emre Akbas},
       booktitle = {arXiv},
       year = {2020}
}
```

## Evaluated Models (Coming Soon)

We evaluate the models from the three common repositories: mmdetection [6], detectron [7], detectron [8], and our aLRP Loss implementation [9].

### Evaluated Object Detection Models

|    Method  Name   |  Source Repo    | AP  | $AP_{50}$ | $AP_{75}$ | $AR$  | oLRP  | $oLRP_{Loc}$ | $oLRP_{FP}$ | $oLRP_{FN}$  | model  |
| :-------------:  | :-----: | :------------: | :------------: | :----: | :-------: |:-------: |:------------: | :----: | :-------: |:-------: |

### Evaluated Keypoint Detection Models 

|    Method  Name   |  Source Repo    | AP  | $AP_{50}$ | $AP_{75}$ | $AR$  | oLRP  | $oLRP_{Loc}$ | $oLRP_{FP}$ | $oLRP_{FN}$  | model  |
| :-------------:  | :-----: | :------------: | :------------: | :----: | :-------: |:-------: |:------------: | :----: | :-------: |:-------: |

### Evaluated Instance Segmentation Models 

|    Method  Name   |  Source Repo    | AP  | $AP_{50}$ | $AP_{75}$ | $AR$  | oLRP  | $oLRP_{Loc}$ | $oLRP_{FP}$ | $oLRP_{FN}$  | model  |
| :-------------:  | :-----: | :------------: | :------------: | :----: | :-------: |:-------: |:------------: | :----: | :-------: |:-------: |

### Evaluated Panoptic Segmentation Models 

|    Method  Name   |  Source Repo    | AP  | $AP_{50}$ | $AP_{75}$ | $AR$  | oLRP  | $oLRP_{Loc}$ | $oLRP_{FP}$ | $oLRP_{FN}$  | model  |
| :-------------:  | :-----: | :------------: | :------------: | :----: | :-------: |:-------: |:------------: | :----: | :-------: |:-------: |

## Specification of Dependencies and Preparation

- ?

## Installation

In this repo, we merge using LRP on different tasks and datasets into one repo. Currently, you could install by run

```shell
# Install cocoapi
pip install "git+https://github.com/open-mmlab/cocoapi.git#subdirectory=pycocotools"
# Install lvis-api
pip install "git+https://github.com/open-mmlab/cocoapi.git#subdirectory=panopticapi"
```

## Examples Usage (Demos)


## License
Following MMDetection, this project is released under the [Apache 2.0 license](LICENSE).

## References
[1] Oksuz K, Cam BC, Akbas E, Kalkan S, Localization recall precision (LRP): A new performance metric for object detection, ECCV 2018.  
[2] [cocoapi](https://github.com/cocodataset/cocoapi) of [COCO dataset](http://cocodataset.org/).

## Contact

This repo is maintained by [Kemal Oksuz](http://github.com/kemaloksuz) and [Baris Can Cam](http://github.com/cancam).
