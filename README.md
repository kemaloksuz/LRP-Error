# One Metric to Measure them All: Localisation Recall Precision (LRP) for Evaluating Visual Detection Tasks

The official implementation of LRP Error. Our implementation follows official COCO repository to evaluate object detection, keypoint detection, instance segmentation and panoptic segmentation tasks. You can also find the implementation to be used with mmdetection [in this link](https://github.com/kemaloksuz/cocoapi).

> [**One Metric to Measure them All: Localisation Recall Precision (LRP) for Evaluating Visual Detection Tasks**](https://arxiv.org/abs/2009.13592),            
> [Kemal Oksuz](https://kemaloksuz.github.io/), Baris Can Cam, , [Sinan Kalkan](http://www.kovan.ceng.metu.edu.tr/~sinan/), [Emre Akbas](http://user.ceng.metu.edu.tr/~emre/),
> *NeurIPS 2020. ([arXiv pre-print](https://arxiv.org/abs/2009.13592))*


## Summary

In a nutshell, LRP is an alternative to average precision (AP), which is the area under the recall-precision curve and is currently the dominant performance measure used in object detection. 

![LRP Toy Example](assets/figure1.png)

In the figure above, three different object detection results are shown (for an image from ILSVRC 2015 Dataset) with very different RP (recall-precision) curves. Note that they all have same same AP. AP is not able to identify the difference between these curves. In (a), (b) and (c), red, blue and green colors denote ground-truth bounding boxes, true positive detections and false positive detections respectively. The numerical values in the images denote confidence scores. (d), (e) and (f) show RP curves, AP and oLRP results for the corresponding detections in (a),(b),(c). Red crosses denote Optimal LRP points.


### What does LRP provide?

1. The Performance Metric for the Object Detection Problem: Average precision (AP), the area under the recall-precision (RP) curve, is the standard performance measure for object detection. Despite its wide acceptance, it has a number of shortcomings, the most important of which are (i) the inability to distinguish very different RP curves, and (ii) the lack of directly measuring bounding box localization accuracy. ''Localization Recall Precision (LRP) Error'' is a new metric which is specifically designed for object detection. LRP Error is composed of three components related to localization, false negative (FN) rate and false positive (FP) rate. Based on LRP, we introduce the ''Optimal LRP'', the minimum achievable LRP error representing the best achievable configuration of the detector in terms of recall-precision and the tightness of the boxes. In our experiments, we show that, for state-of-the-art object (SOTA) detectors, Optimal LRP provides richer and more discriminative information than AP.

2. LRP As a Thresholder: In contrast to AP, which considers precisions over the entire recall domain, Optimal LRP determines the ''best'' confidence score threshold for a class, which balances the trade-off between localization and recall-precision. We demonstrate that the best confidence score thresholds vary significantly among classes and detectors. Moreover, we present LRP results of a simple online video object detector which uses a SOTA still image object detector and show that the class-specific optimized thresholds increase the accuracy against the common approach of using a general threshold for all classes.


## How to Cite

Please cite the paper if you benefit from our paper or repository:
```
@inproceedings{LRP,
       title = {One Metric to Measure them All: Localisation Recall Precision (LRP) for Evaluating Visual Detection Tasks},
       author = {Kemal Oksuz and Baris Can Cam and Sinan Kalkan and Emre Akbas},
       booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
       year = {2020}
}
```

## Evaluated Object Detection Models

|    Method     |    Backbone     |  Scale   | AP (test-dev) | AP (minival) | oLRP (minival) | Model  | Log  |
| :-------------: | :-------------: | :-----: | :------------: | :------------: | :----: | :-------: |:-------: |
| AP Loss* |    ResNet-50    |  500  |   35.7   |   35.4   |  71.0  | [model](https://drive.google.com/file/d/17T2TqSA_mexGx1CSsTj6H6-46jxjafRC/view?usp=sharing)|[log](https://drive.google.com/file/d/1pkSLBDbTLqeRqSUZlxUMxofSR6FQO_0U/view?usp=sharing)|
| aLRP Loss (GIoU)* |    ResNet-50    |  500  |   39.5   |   39.0   |  68.1  | [model](https://drive.google.com/file/d/1K-YGYrVMRGp0M6w7_PgIYAp2kHFOJo8C/view?usp=sharing)|[log](https://drive.google.com/file/d/1iGj9zb68sksJsYKG68T8sd900PMOTbqd/view?usp=sharing)|
| aLRP Loss (GIoU+ATSS) |    ResNet-50    |  500  |   41.3   |   41.0   |  66.6  | [model](https://drive.google.com/file/d/15wKL1YVPrCBLpPKtaOe8VQR2uhyKUB0L/view?usp=sharing)|[log](https://drive.google.com/file/d/1blRO6-C2itppoLCKt6q9CQEl8POn4J4q/view?usp=sharing)|
|aLRP Loss (GIoU+ATSS)|    ResNet-101    |  500  |   42.8   |   42.2   |  65.1  | [model](https://drive.google.com/file/d/1Cozn9fB44IPq26SN1L-qbGqbLucSMnKK/view?usp=sharing)|[log](https://drive.google.com/file/d/1T8vJug62foZna9VRhE-m5i_xpDZpC-TO/view?usp=sharing)|
|aLRP Loss (GIoU+ATSS)|    ResNext-101-64x4d    |  500  |   44.6   |   44.5   |  ?  | [model](https://drive.google.com/file/d/1YB7R68VDsruBVI1YhqMVO2XO2EgX3aUA/view?usp=sharing)|[log](https://drive.google.com/file/d/1oP2jDBkQfK3x0G2kvS-ZimM9IAiTfQ_t/view?usp=sharing)|
|aLRP Loss (GIoU+ATSS)|    ResNet-101    |  800  |   45.9   |   45.4   |  62.9  | [model](https://drive.google.com/file/d/1L74v4LLWt5uYDEeSBMhKECpztqNG3QIQ/view?usp=sharing)|[log](https://drive.google.com/file/d/1lhz_UI5kKlhZXI1DQ7Gt1ph-DJRS-zW4/view?usp=sharing)|
|aLRP Loss (GIoU+ATSS)|    ResNext-101-64x4d    |  800  |   47.8   |   47.2   |  ?  | [model](https://drive.google.com/file/d/1-sJoRM7u43rLx9ntJkvuE4BmOwEfukDs/view?usp=sharing)|[log](https://drive.google.com/file/d/1TROgjqCWmlWm9wH8YIYV8V5IsaVVY4w8/view?usp=sharing)|
|aLRP Loss (GIoU+ATSS)|    ResNext-101-64x4d-DCN    |  800  |   48.9   |   48.6   |  ?  | [model](https://drive.google.com/file/d/1vO_wAPzVQm8-tCj0ReoJeo6T0EpeRv61/view?usp=sharing)|[log](https://drive.google.com/file/d/1Q6HALIEg60bpKXuJIiiLF9IzdsYdZ8BC/view?usp=sharing)|

## Evaluated Keypoint Detection Models

|    Method     |  Backbone   | AP (minival) | oLRP (minival) | Model  |  Log  |
| :-------------: | :-----: | :------------: | :------------: | :-------: | :-------: |
|    Focal Loss+Smooth L1 |  ResNet-50  |   38.3   |   68.8  | [model](https://drive.google.com/file/d/1uOB7r6XuQvEzPvZnmHvmL69qSYFQj2mR/view?usp=sharing)|[log](https://drive.google.com/file/d/1yiKJ8UHEz1Uql-Qi4rUEVHheeFaji0Va/view?usp=sharing)|
|    AP Loss+Smooth L1  | ResNet-50 |   36.5  |   69.8   | [model](https://drive.google.com/file/d/1FyaKNJOE6Rbq2bSN6SAWnE8t_hW7OIFC/view?usp=sharing)|[log](https://drive.google.com/file/d/1O5H2RdRijVJzJgHtyxX7qrThsA_Rcrft/view?usp=sharing)|
|    aLRP Loss | ResNet-50 |   39.7   |   67.2  | [model](https://drive.google.com/file/d/1f76mMqp7yAPIKzj5Cb6Moy6Dk13I1qny/view?usp=sharing)|[log](https://drive.google.com/file/d/1UGbcaAgAwL0P_dbY5RDhy53DqPDY20j7/view?usp=sharing)|

## Evaluated Instance Segmentation Models

|    Method     |  Backbone   | AP (minival) | oLRP (minival) | Model  |  Log  |
| :-------------: | :-----: | :------------: | :------------: | :-------: | :-------: |
|    Cross Entropy+Smooth L1 |  ResNet-50  |   37.8   |   69.3  | [model](https://drive.google.com/file/d/1eUahlGWfArXhc5e58IQWT7QU0TVMZGAM/view?usp=sharing)|[log](https://drive.google.com/file/d/19_0pT3H3q1I5oNTMN8rbRgPSjL-hltaL/view?usp=sharing)|
|    Cross Entropy+GIoU Loss  | ResNet-50 |   38.2  |   69.0   | [model](https://drive.google.com/file/d/1OSdruWbtYmC35BaM7pz9Oe34OuVnyu71/view?usp=sharing)|[log](https://drive.google.com/file/d/15IlJ8G5G0COF-JktijcYi37qcNkY4X0Q/view?usp=sharing)|
|    aLRP Loss | ResNet-50 |   40.7   |   66.7  | [model](https://drive.google.com/file/d/1NgbI9_5f6giKLfT9UlZZNoPH6D-Cm3U8/view?usp=sharing)|[log](https://drive.google.com/file/d/1IivL3d693s_jYD5CoUuRoSrLTKj5tTcp/view?usp=sharing)|

## Evaluated Panoptic Segmentation Models

|    Method     |  Backbone   | AP (minival) | oLRP (minival) | Model  |  Log  |
| :-------------: | :-----: | :------------: | :------------: | :-------: | :-------: |
|    Cross Entropy+Smooth L1 |  ResNet-50  |   37.8   |   69.3  | [model](https://drive.google.com/file/d/1eUahlGWfArXhc5e58IQWT7QU0TVMZGAM/view?usp=sharing)|[log](https://drive.google.com/file/d/19_0pT3H3q1I5oNTMN8rbRgPSjL-hltaL/view?usp=sharing)|
|    Cross Entropy+GIoU Loss  | ResNet-50 |   38.2  |   69.0   | [model](https://drive.google.com/file/d/1OSdruWbtYmC35BaM7pz9Oe34OuVnyu71/view?usp=sharing)|[log](https://drive.google.com/file/d/15IlJ8G5G0COF-JktijcYi37qcNkY4X0Q/view?usp=sharing)|
|    aLRP Loss | ResNet-50 |   40.7   |   66.7  | [model](https://drive.google.com/file/d/1NgbI9_5f6giKLfT9UlZZNoPH6D-Cm3U8/view?usp=sharing)|[log](https://drive.google.com/file/d/1IivL3d693s_jYD5CoUuRoSrLTKj5tTcp/view?usp=sharing)|

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

