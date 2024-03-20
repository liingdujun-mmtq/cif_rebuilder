set c="C:\Program Files\Git\usr\bin\cp.exe"
set dst=C:\Users\Game\Code\cif_rebuilder\cif_rebuilder.dist
set libsrc=C:\Users\Game\AppData\Local\Programs\Python\Python311\Lib
set dllsrc=C:\Users\Game\AppData\Local\Programs\Python\Python311\DLLs
set srcdir=C:\Users\Game\AppData\Local\Programs\Python\Python311\Lib\site-packages


%c%  %srcdir%\tkinterDnD %dst% -rf 
%c%  %srcdir%\ttkwidgets %dst% -rf
%c%  %srcdir%\PIL %dst% -rf
%c%  %libsrc%\tkinter %dst% -rf