pyinstaller --noconfirm --log-level=WARN ^
    --onedir --windowed ^
    --add-data="E:/My Programs/Python/PushpSoochak/PSVenv/Lib/site-packages/customtkinter;customtkinter/" ^
    --upx-dir "upx.exe" ^
    --distpath ""./pyInstaller/dist" ^
    Recogniser.spec