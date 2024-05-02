# cif_rebuilder
Rebuild cif file to be compatible with Jems software

重建cif（晶体结构）文件，以使jems能读取老旧的cif晶体结构信息

## How it works/工作原理

remove line numbers in "_space_group_symop_operation_xyz" part of cif files

将cif文件中_space_group_symop_operation_xyz部分中原子占位信息前的行号删除：

## How to use/使用方法

Just drop your cif to the file box, and click the buttom "rebuild cif", a new cif file with name "cif_filename-rebuild.cif" will be created at the same directory, where cif_filename is the name you droped into the box.

只需要将需要转换的文件拖进文件框中，点"rebuild cif"按钮，然后一个重建过的cif就会以原文件名+后缀"-rebuild.cif"的形式保存在相同的文件夹。
