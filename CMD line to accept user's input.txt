@echo off 
rem 关闭自动输出
:begin

rem 接收输入

set input=
set /p input=请输入字符串:

rem 输出得到的输入信息

echo 您输入的字符串是：%input%
rem pause>null

echo.

rem 从begin标签出，再次运行

goto begin