from lvis import LVIS, LVISResults, LVISEval

# result and val files for 100 randomly sampled images.
ANNOTATION_PATH = "./data/lvis_val_100.json"
RESULT_PATH = "./data/lvis_results_100.json"

# Annotation type is segm or bbox
ANN_TYPE = 'segm'

# Number of detections to be collected from each image
# LVIS uses 300 by default. 
# If you want to use all detections in the detection 
# file, then you can set it to -1.
MAX_DETS = 300

gt = LVIS(ANNOTATION_PATH)
results = LVISResults(gt, RESULT_PATH, max_dets=MAX_DETS)
lvis_eval = LVISEval(gt, results, iou_type=ANN_TYPE)
params = lvis_eval.params
params.max_dets = MAX_DETS  # No limit on detections per image.

lvis_eval.run()
lvis_eval.print_results()


# Uncomment to print class-specific LRP-Optimal Thresholds
# lvis_eval.print_lrp_opt_thresholds()
