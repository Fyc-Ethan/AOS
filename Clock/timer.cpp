#include<iostream>
#include<Windows.h>
 
using namespace std;
 
#define ID_TIMER 0
void CALLBACK printSTR(HWND hwnd, UINT message, UINT iTimerID, DWORD dwTimer)
{
    cout<<"hello world!\n";
}
 
int main()
{
    int iId;
     MSG msg;
     
    iId = SetTimer(NULL, ID_TIMER, 1000, printSTR);
     
    while(GetMessage(&msg, NULL, 0, 0))
    {
        DispatchMessage(&msg);
    }
     
    KillTimer(NULL, iId);
    return 0;
}