1. python函数参数列表中的'[]'
>cv.bitwise_and(src1, src2[, dst[, mask]]	) ->	dst

在OpenCV中，方括号（[]）表示参数是可选的。也就是说，你可以选择性地提供这些参数，具体取决于你的需求。下面是每个参数的解释：

src1：第一个输入数组或图像。  
src2：第二个输入数组或图像。  
dst（可选）：输出数组或图像，用于存储按位与操作的结果。  
mask（可选）：可选的掩码数组或图像，用于指定按位与操作的有效区域。只有在掩码对应的像素位置为非零时，才会执行按位与操作。  
cv.bitwise_and()函数执行的是按位与操作，它将对src1和src2的对应像素进行按位与运算，并将结果存储在dst中。掩码mask用于指定哪些像素需要参与按位与操作。如果没有提供dst，函数将创建一个与src1和src2具有相同形状和数据类型的新数组。  

**总结起来，方括号表示参数是可选的，你可以根据需要选择是否提供这些参数。**  
2. python函数调用传参
>img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)  

mask = mask_inv不是赋值,而是显式指定函数的参数  

3. 元组用法
>height, width = img.shape[:2]
     
[:2]返回值是img.shape的前两个元素

4. masked_equal是NumPy库中的一个函数，用于创建一个掩码数组，将数组中特定的值屏蔽（遮蔽）起来.

# 设置打印选项以显示更多的数组元素
np.set_printoptions(threshold=np.inf)
