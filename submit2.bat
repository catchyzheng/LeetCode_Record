@echo off 
rem �ر��Զ����
:begin

rem ��������

set input=
set /p input=�������ַ���:

rem ����õ���������Ϣ

echo your input is ��%input%
rem pause>null

echo on

git add .
git commit -m "%input%"
git push origin master