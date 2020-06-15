#include<windows.h>

LRESULT CALLBACK WndProc( HWND, UINT, WPARAM, LPARAM ) ;
VOID CALLBACK TimerProc( HWND, UINT, UINT, DWORD ) ;

int WINAPI WinMain( HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow )
{
    static TCHAR szAppName[] = TEXT("UseTimer") ;
    HWND        hwnd ;
    MSG            msg ;
    WNDCLASS    wndclass ;

    wndclass.lpszClassName        = szAppName ;
    wndclass.hInstance            = hInstance ;
    wndclass.lpfnWndProc        = WndProc ;
    wndclass.style                = CS_HREDRAW | CS_VREDRAW ;
    wndclass.hbrBackground        = (HBRUSH) GetStockObject(WHITE_BRUSH) ;
    wndclass.hIcon                = LoadIcon( NULL, IDI_APPLICATION ) ;
    wndclass.hCursor            = LoadCursor( NULL, IDC_ARROW ) ;
    wndclass.cbClsExtra            = 0 ;
    wndclass.cbWndExtra            = 0 ;
    wndclass.lpszMenuName        = NULL ;

    if( !RegisterClass(&wndclass) )
    {
        MessageBox( NULL, TEXT("错误, 无法注册窗口类!"), szAppName, MB_OK | MB_ICONERROR ) ;
        return 0 ;
    }

    hwnd = CreateWindow( szAppName, TEXT("UseTimer - Demo"),
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT,
        900, 600,
        NULL, NULL, hInstance, NULL ) ;

    ShowWindow( hwnd, iCmdShow ) ;
    UpdateWindow( hwnd ) ;

    while( GetMessage( &msg, NULL, 0, 0) )
    {
        TranslateMessage( &msg ) ;
        DispatchMessage( &msg ) ;
    }
    return msg.wParam ;
}


LRESULT CALLBACK WndProc( HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam )
{
    HDC hdc ;
    PAINTSTRUCT ps ;
    static int iTimerID ;        //记录计时器ID
    static int y = 10 ;            //记录已输出行y坐标

    switch(message)
    {
    case WM_CREATE:        //处理WM_CREATE消息时完成计时器的创建
        iTimerID = SetTimer( hwnd, 0, 5000, TimerProc ) ;    //设置一个ID随机分配、时间间隔为5秒, 有回调函数的计时器
        SetTimer( hwnd, 2, 3000, NULL ) ;                    //设置一个ID为2, 时间间隔为3秒, 无回调函数的计时器
        return 0 ;

    case WM_TIMER:        //处理WM_TIMER消息
        switch(wParam)
        {
        case 2:
            hdc = GetDC( hwnd ) ;
            TextOut( hdc, 10, y, TEXT("我是来自ID为2的计时器, 间隔为3秒, 我负责绘制文字。"),
                lstrlen("我是来自ID为2的计时器, 间隔为3秒, 我负责绘制文字。") ) ;
            y += 20 ;        //向下移动20个像素, 模拟文字换行
            ReleaseDC( hwnd, hdc ) ;
            ValidateRect( hwnd, NULL ) ;
            break ;

        /*
            如果创建了更多的计时器, 这里继续case计时器的ID, 用来区分不同计时器发来的消息
        */
        }
        return 0 ;

    case WM_DESTROY:
        KillTimer( hwnd, iTimerID ) ;        //销毁ID为随机分配的计时器
        KillTimer( hwnd, 2 ) ;                //销毁ID为2的计时器
        PostQuitMessage( 0 ) ;
        return 0 ;
    }
    return DefWindowProc( hwnd, message, wParam, lParam ) ;
}

VOID CALLBACK TimerProc( HWND hwnd, UINT message, UINT iTimerID, DWORD dwTime )
{    //定义计时器回调函数
    MessageBox( hwnd, TEXT("我是负责弹出对话框的计时器! 间隔为5秒!"), TEXT("计时器消息"), MB_OK ) ;
}