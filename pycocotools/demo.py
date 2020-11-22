from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

# This file presents an evaluation example given a detection file in
# json formatted following COCO sytle output.

# Specify result file. It can be a result file from an object detector,
# keypoint detector of an instance segmentation method.

# Uncomment for an instance segmentation example
# resFile = 'htc_X_101.segm.json'

# Uncomment for an object detection example
# We provide this json file in our example in Readme.md
# Please download ssd300_coco.bbox.json from the table 
# and place it in the same folder with this script
resFile = 'ssd300_coco.bbox.json'

# Uncomment for a keypoint detection example
# resFile = 'keypoint_rcnn_X_101.json'

# initialize COCO detections api
annType = ['segm', 'bbox', 'keypoints']

# #specify the type here, e.g for object detection use 1
annType = annType[1]
prefix = 'person_keypoints' if annType == 'keypoints' else 'instances'
print('Running demo for *%s* results.' % (annType))

# initialize COCO ground truth api, set the path of accordingly
dataDir = '../'
dataType = 'val2017'
annFile = '%s/annotations/%s_%s.json' % (dataDir, prefix, dataType)
cocoGt = COCO(annFile)

# load detection file
cocoDt = cocoGt.loadRes(resFile)

imgIds = sorted(cocoGt.getImgIds())

# running evaluation
cocoEval = COCOeval(cocoGt, cocoDt, annType)
cocoEval.params.imgIds = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()
