import cv2
import numpy as np
import os

def undistort_images(input_folder, output_folder):
   # 確保輸出資料夾存在
   if not os.path.exists(output_folder):
       os.makedirs(output_folder)
   
   # 影像解析度
   width, height = 4032, 3024
   
   # 相機參數
   cb = 5.2518  # balanced principal distance (mm)
   pixel_size = 0.0017  # mm/pixel
   
   # 將焦距從毫米轉換為像素
   fx = fy = cb / pixel_size
   cx = width / 2
   cy = height / 2
   
   # 構建相機矩陣
   camera_matrix = np.array([
       [fx, 0, cx],
       [0, fy, cy],
       [0, 0, 1]
   ], dtype=np.float64)
   
   # 畸變係數 [k1, k2, p1, p2, k3]
   # 使用5參數模型，這是OpenCV最常用的格式
   dist_coeffs = np.array([
       4.05865e-31,   # k1
       3.22146e-38,   # k2
       0.0,            # p1
       0.0,            # p2
       2.48791e-49    # k3
   ], dtype=np.float64).reshape(-1, 1)
   
   print("相機矩陣:")
   print(camera_matrix)
   print("\n畸變係數:")
   print(dist_coeffs)
   
   # 處理資料夾中的所有JPG圖片
   for filename in os.listdir(input_folder):
       if filename.lower().endswith(('.jpg', '.jpeg')):
           # 讀取影像
           img_path = os.path.join(input_folder, filename)
           img = cv2.imread(img_path)
           
           if img is None:
               print(f"無法讀取影像: {filename}")
               continue
           
           print(f"處理中 {filename}...")
           
           # 獲取影像尺寸
           h, w = img.shape[:2]
           
           # 獲取最佳相機矩陣
           newcameramtx, roi = cv2.getOptimalNewCameraMatrix(
               camera_matrix, 
               dist_coeffs, 
               (w, h), 
               1, 
               (w, h)
           )
           
           try:
               # 校正影像
               dst = cv2.undistort(
                   img, 
                   camera_matrix, 
                   dist_coeffs, 
                   None, 
                   newcameramtx
               )
               
               # 裁剪影像
               x, y, w, h = roi
               if all(v > 0 for v in [x, y, w, h]):
                   dst = dst[y:y+h, x:x+w]
               
               # 儲存校正後的影像
               output_path = os.path.join(output_folder, f"undistorted_{filename}")
               cv2.imwrite(output_path, dst)
               print(f"已成功處理: {filename}")
               
           except Exception as e:
               print(f"處理 {filename} 時發生錯誤: {str(e)}")

if __name__ == "__main__":
   # 設置輸入和輸出資料夾路徑
   input_folder = "pic"
   output_folder = "revise_pic"
   
   try:
       undistort_images(input_folder, output_folder)
       print("所有影像處理完成！")
   except Exception as e:
       print(f"處理過程中發生錯誤: {str(e)}")