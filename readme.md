# 相機率定與影像修正作業

## 作業說明
本作業實作使用Australis軟體進行相機率定，並利用OpenCV實現影像校正。

## 作業時間
- **開始日期:** 2024年10月1日 (週二) 00:00
- **截止日期:** 2024年12月31日 (週二) 00:00

## 實作步驟

### 1. 相機率定
1. 使用Australis Demo軟體
2. 佈置人造標場域
3. 使用iPhone 13進行環繞拍攝
4. 在Australis中進行相機率定

### 2. 影像校正
使用Python程式進行影像校正，主要使用以下套件：
- OpenCV
- NumPy

### 專案結構
```
project/
│
├── pic/                    # 原始照片資料夾
│   ├── IMG_3728.JPG
│   ├── IMG_3729.JPG
│   └── ...
│
├── revise_pic/            # 校正後照片資料夾
│   ├── undistorted_IMG_3728.JPG
│   ├── undistorted_IMG_3729.JPG
│   └── ...
│
├── main.py                # 校正程式
└── README.md              # 說明文件
```

### 相機參數
iPhone 13相機參數：
```
- Resolution: 4032 x 3024 pixels
- Pixel size: 0.0017mm
- Principal distance (cb): 5.2518mm
- 畸變係數：
  - K0 = 3.65279e-30
  - K1 = -4.05865e-31
  - K2 = -3.22146e-38
  - K3 = -2.48791e-49
  - K4 = 0.00000e+00
  - K5 = 0.00000e+00
```

## 使用說明

### 環境設置
1. 安裝必要套件：
```bash
pip install opencv-python numpy
```

2. 建立所需資料夾：
   - 建立 `pic` 資料夾並放入原始照片
   - 程式會自動建立 `revise_pic` 資料夾存放校正後的照片

### 執行程式
```bash
python main.py
```

## 執行結果
1. 程式會讀取 `pic` 資料夾中的所有 JPG 圖片
2. 使用相機率定參數進行校正
3. 校正後的圖片會儲存在 `revise_pic` 資料夾中
4. 檔名格式：`undistorted_原始檔名.jpg`

## 注意事項
1. 確保原始照片放在正確的資料夾位置
2. 確認 Python 環境已正確安裝所需套件
3. 校正過程中若出現錯誤會顯示相關訊息
4. 校正後的影像會自動進行最佳化裁剪