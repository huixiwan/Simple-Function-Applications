## Introducer
***
这是一个附近地点生成脚本。它可以根据输入的经纬度，最大距离，随机生成指定数量的地点，生成的数据地点的经纬度与地区名。

<br/>

## How to use
***
#### Environment
python3.X

#### Input Txt
- 输入文件名：input.txt
- 每行数据：[经度] [纬度] [最大距离] [生成个数]
- 中间间隔符：空格

#### Run
将generate.py与input.txt放在同一个文件下，运行generate.py即可获取结果

<br/>

## Result
***
程序会输出output.txt与output.\_random.txt，output.\_random.txt是对output.txt结果的打乱。文件中每一行的结果为：[纬度],[经度] [地区名]
