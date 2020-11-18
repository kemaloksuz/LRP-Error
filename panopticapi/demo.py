from panopticapi.evaluation import pq_lrp_compute

model = "panoptic_fpn_R_50_1x"

gt_json = "/home/kemal/Datasets/coco/annotations/panoptic_val2017.json"
pred_json = "./results/" + model + "/predictions.json"
gt_dir = "/home/kemal/Datasets/coco/panoptic_val2017"
pred_dir = "./results/" + model + "/panoptic_img"

pq_lrp_compute(gt_json, pred_json, gt_dir, pred_dir)
