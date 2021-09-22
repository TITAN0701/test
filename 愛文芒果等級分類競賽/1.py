
import os
from PIL import Image, ImageFilter
import numpy as np

# 直接指定全部圖片路徑
path_sample_image = 'C:/Users/abc86/Desktop/manchine learning/愛文芒果等級分類競賽/AIMango_sample/sample_image'
image_path = os.listdir(path_sample_image)
    
#查看第一張照片
onepage = Image.open("D-Plant2_0610_4.jpg")
print(onepage.size)
#print(onepage.mode)
#onepage.save("D-Plant2_0610_4.png","png")

#轉換成灰白的圖片
#onepage_f = onepage.filter(ImageFilter.FIND_EDGES)
#onepage_f.save("D-Plant2_0610_4.png","png")

#onepage_s = onepage.filter(ImageFilter.SHARPEN)
#onepage_s.show()

from keras.preprocessing import image as image_utils
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input
from keras.applications import VGG16
import cv2
# 使用Keras工具箱加載圖片，並縮放圖片到224x224像素
image = image_utils.load_img("D-Plant2_0610_4.jpg", target_size=(224, 224))
image = image_utils.img_to_array(image)  # 把圖片轉為numpy數組
image = np.expand_dims(image, axis=0)
image = preprocess_input(image)

#模型設定
model = VGG16(include_top=True, weights="imagenet")
preds = model.predict(image) 
P = decode_predictions(preds)

#顯示前5個預測結果
for (i, (imagenetID, label, prob)) in enumerate(P[0]): 
    print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))

#然後使用opencv加載圖片
oc = cv2.imread("D-Plant2_0610_4.jpg")
(imagenetID, label, prob) = P[0][0] 
cv2.putText(oc, "Label: {}, {:.2f}%".format(label, prob * 100),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
cv2.imshow("Classification", oc)
cv2.waitKey(12000)
