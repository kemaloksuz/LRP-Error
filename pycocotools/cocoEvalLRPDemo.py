from pycocotool.coco import COCO
from pycocotool.cocoeval import COCOeval
import pylab
pylab.rcParams['figure.figsize'] = (10.0, 8.0)

# Specify result file. It can be a result file from an object detector,
# keypoint detector of an instance segmentation method.

# Uncomment for an instance segmentation example
# resFile = '../results/htc_X_101.segm.json'

# Uncomment for an object detection example
resFile = '../results/faster_rcnn_R_50.json'

# Uncomment for a keypoint detection example
# resFile = '../results/keypoint_rcnn_X_101.json'

# initialize COCO detections api
annType = ['segm', 'bbox', 'keypoints']

# #specify type here
annType = annType[1]
prefix = 'person_keypoints' if annType == 'keypoints' else 'instances'
print('Running demo for *%s* results.' % (annType))

# initialize COCO ground truth api
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
