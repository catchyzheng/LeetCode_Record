@echo off 
rem 关闭自动输出
:begin

rem 接收输入

set input=
set /p input=请输入字符串:

rem 输出得到的输入信息

echo your input is ：%input%
rem pause>null

echo on

git add .
git commit -m "%input%"
git push origin master