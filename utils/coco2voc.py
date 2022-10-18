import json
import os
import pdb
import xml.etree.ElementTree as ET
from collections import defaultdict

import tqdm

'''
convert txt to xml
'''


def coco2voc(anno_file, save_dir):
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    with open(anno_file) as f:
        data = json.load(f)

    id_name_mapping = {}
    for each in data["categories"]:
        id = each["id"]
        name = each["name"]
        id_name_mapping[id] = name

    anno_dict = defaultdict(list)
    image_info = data["images"]

    for each in data["annotations"]:
        img_id = each["image_id"]
        cat_name = id_name_mapping[each["category_id"]]
        anno_dict[img_id].append(each)
    for each in data["images"]:
        each_imgpath = each["file_name"].split("/")[-1]
        each_imgid = each["id"]
        each_img_anno = anno_dict[each_imgid]
        each_anno_savename = os.path.splitext(each_imgpath)[0] + ".xml"
        each_anno_savename = os.path.join(save_dir, each_anno_savename)

        height = int(each["height"])
        width = int(each["width"])
        xml_file = open(each_anno_savename, 'w')

        xml_file.write('<annotation>\n')
        xml_file.write('    <folder>VOC2007</folder>\n')
        xml_file.write('    <filename>' + each_imgpath + '</filename>\n')
        xml_file.write('    <size>\n')
        xml_file.write('        <width>' + str(width) + '</width>\n')
        xml_file.write('        <height>' + str(height) + '</height>\n')
        xml_file.write('        <depth>3</depth>\n')
        xml_file.write('    </size>\n')

        for each_bbox_info in each_img_anno:
            xmin, ymin, bbox_w, bbox_h = each_bbox_info["bbox"]
            xmax = xmin + bbox_w
            ymax = ymin + bbox_h
            xmin = max(0, int(float(xmin)))
            ymin = max(0, int(float(ymin)))
            xmax = min(width, int(float(xmax)))
            ymax = min(height, int(float(ymax)))
            cls_id = each_bbox_info["category_id"]
            cls_name = id_name_mapping[cls_id]
            xml_file.write('    <object>\n')
            xml_file.write('        <name>' + cls_name + '</name>\n')
            xml_file.write('        <pose>Unspecified</pose>\n')
            xml_file.write('        <truncated>0</truncated>\n')
            xml_file.write('        <difficult>0</difficult>\n')
            xml_file.write('        <bndbox>\n')
            xml_file.write('            <xmin>' + str(xmin) + '</xmin>\n')
            xml_file.write('            <ymin>' + str(ymin) + '</ymin>\n')
            xml_file.write('            <xmax>' + str(xmax) + '</xmax>\n')
            xml_file.write('            <ymax>' + str(ymax) + '</ymax>\n')
            xml_file.write('        </bndbox>\n')
            xml_file.write('    </object>\n')

        xml_file.write('</annotation>')
        xml_file.close()

def COCO2VOC():
    SAVE_DIR = os.path.join('data', 'COCO', 'annotations', 'xml')
    coco2voc(os.path.join('data', 'COCO', 'annotations', 'instances_train2017.json'), SAVE_DIR)
    coco2voc(os.path.join('data', 'COCO', 'annotations', 'instances_val2017.json'), SAVE_DIR)
if __name__ == "__main__":
    COCO2VOC()
    
    
