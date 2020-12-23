from panopticapi.evaluation import pq_lrp_compute

gt_json = "/home/kemal/Datasets/coco/annotations/panoptic_val2017.json"
gt_dir = "/home/kemal/Datasets/coco/panoptic_val2017"

# Download these files from PQ results table and place in the following folder
pred_json = ".sample_data/lrp_example/panoptic_fpn_R_50_1x/predictions.json"
pred_dir = ".sample_data/lrp_example/panoptic_fpn_R_50_1x/panoptic_img"

pq_lrp_compute(gt_json, pred_json, gt_dir, pred_dir)
