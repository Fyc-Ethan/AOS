#include <iostream>
#include <Windows.h>
 
 
class MyTimer{
 
private:
    LARGE_INTEGER large_integer;
    __int64 IntStart;
    __int64 IntEnd;
    double DobDff;
    double DobMillseconds;
 
public:
    MyTimer(){};
 
    void TimerStart(){
        QueryPerformanceFrequency(&large_integer);
        DobDff = large_integer.QuadPart;
 
        QueryPerformanceCounter(&large_integer);
        IntStart = large_integer.QuadPart;
    }
 
    double TimerFinish(){
        QueryPerformanceCounter(&large_integer);
        IntEnd = large_integer.QuadPart;
        DobMillseconds = (IntEnd - IntStart) * 1000 / DobDff; 
        return DobMillseconds;
    }
    
 
};
 
void main ()
{
    MyTimer timer;
    timer.TimerStart();
    Sleep(1.321);
    double tm = timer.TimerFinish();
    std::cout << tm << std::endl;
    
//    timer.OutputToFile("C:/timer.txt");
}