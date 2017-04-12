      #download_imagenet.py

从imaegnet中按给定链接下载图片。需要fan qiang，但仍有很多time out。程序会提示哪些页面已失效、哪些无法访问。

      #set_label.py

为图片打上标签，输入：图片的根目录

功能：

   1. 把乱七八糟的文件名改成 1,2,3,4...
   
   2. 把类名改成 1,2,3... 方便统计
  
  输出文件格式：file_path label


      ##calculate_similarity

计算两张图片的相似度，借助于DBH（Deep Learning of Binary Hash Codes for Fast Image Retrieval）

由于DBH是基于matlab版本的caffe，因此我们用Python进行简单复现和实验。
