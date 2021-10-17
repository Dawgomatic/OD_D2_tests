import os

def test():
  #instance segmentation 
  os.system('python demo.py --config-file ../configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml --input ./my_file.jpg --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl')
  
  #panotic segmentation
    os.system('python demo.py --config-file ../configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_3x.yaml --input ./my_file.jpg --opts MODEL.WEIGHTS detectron2://COCO-PanopticSegmentation/panoptic_fpn_R_50_3x/139514569/model_final_c10459.pkl')
  
  #object detection
  os.system('python demo.py --config-file ../configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml --input ./my_file.jpg --opts MODEL.WEIGHTS detectron2://COCO-Detection/fast_rcnn_R_50_FPN_1x/137635226/model_final_e5f7ce.pkl')
   
  #Keypoint
  os.system('python demo.py --config-file ../configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml --input ./my_file.jpg --opts MODEL.WEIGHTS detectron2://COCO-Keypoints/keypoint_rcnn_R_50_FPN_1x/137261548/model_final_04e291.pkl')
  
  #DensePose
  os.system('python apply_net.py show configs/densepose_rcnn_R_50_FPN_s1x.yaml https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_s1x/165712039/model_final_162be9.pkl C:/full/path/to/my_file.jpg dp_contour,bbox -v')
  
  #DensePose deeplabv3
   #DensePose
  os.system('python apply_net.py show configs/densepose_rcnn_R_101_FPN_DL_s1x.yaml https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_101_FPN_DL_s1x/165712116/model_final_844d15.pkl C:/full/path/to/my_file.jpg dp_contour,bbox -v')
            
test()
