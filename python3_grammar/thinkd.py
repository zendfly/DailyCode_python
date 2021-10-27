import math
import numpy as np

this_scale = 0.88
next_scale = 1.05
two_boxes_for_ar1 = True
aspect_ratios = [1.0,2.0,0.5]
size = min(300,300)  # 图片size
print(size)
# Compute the box widths and and heights for all aspect ratios
wh_list = []  # 保存长宽
for ar in aspect_ratios:
    if (ar == 1):  # ar为1时，额外的一个scales计算
        # Compute the regular anchor box for aspect ratio 1.
        box_height = box_width = this_scale * size
        wh_list.append((box_width, box_height))
        if two_boxes_for_ar1:
            # Compute one slightly larger version using the geometric mean of this scale value and the next.
            box_height = box_width = np.sqrt(this_scale * next_scale) * size
            wh_list.append((box_width, box_height))
    else:
        box_height = this_scale * size / np.sqrt(ar)
        box_width = this_scale * size * np.sqrt(ar)
        wh_list.append((box_width, box_height))
wh_list = np.array(wh_list)

# print(wh_list)


offset_height = offset_width =  0.5
step_height = step_width = 100
feature_map_height = feature_map_width = 3
n_boxes = 4
clip_boxes = True
img_width = img_height = 300
cy = np.linspace(offset_height * step_height, (offset_height + feature_map_height - 1) * step_height, feature_map_height)
cx = np.linspace(offset_width * step_width, (offset_width + feature_map_width - 1) * step_width, feature_map_width)
cx_grid, cy_grid = np.meshgrid(cx, cy)
cx_grid = np.expand_dims(cx_grid, -1) # This is necessary for np.tile() to do what we want further down
cy_grid = np.expand_dims(cy_grid, -1) # This is necessary for np.tile() to do what we want further down
boxes_tensor = np.zeros((feature_map_height, feature_map_width, n_boxes, 4))

boxes_tensor[:, :, :, 0] = np.tile(cx_grid, (1, 1, n_boxes))  # Set cx
boxes_tensor[:, :, :, 1] = np.tile(cy_grid, (1, 1, n_boxes))  # Set cy
boxes_tensor[:, :, :, 2] = wh_list[:, 0]  # Set w
boxes_tensor[:, :, :, 3] = wh_list[:, 1]  # Set h

print(boxes_tensor)

# If `clip_boxes` is enabled, clip the coordinates to lie within the image boundaries
if clip_boxes:
    x_coords = boxes_tensor[:, :, :, [0, 2]]
    x_coords[x_coords >= img_width] = img_width - 1
    x_coords[x_coords < 0] = 0
    boxes_tensor[:, :, :, [0, 2]] = x_coords
    y_coords = boxes_tensor[:, :, :, [1, 3]]
    y_coords[y_coords >= img_height] = img_height - 1
    y_coords[y_coords < 0] = 0
    boxes_tensor[:, :, :, [1, 3]] = y_coords

# boxes_tensor.shape
print(boxes_tensor.shape)