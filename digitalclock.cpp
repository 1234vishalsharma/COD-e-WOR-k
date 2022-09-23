#include <iostream>
#include <time.h>
#include<dos.h>
#include<conio.h>
using namespace std;
int main()
{
    int h, m, s;
    z:
    cout << "Enter the current time:\n";
    cin >> h;
    cout << endl;
    cin >> m;
    cout << endl;
    cin >> s;
    cout << endl;
    if(h>=12||m>=60||s>=60){
        cout<<"Invalid Inputs"<<endl;
        goto z;
    }
    while(1)
    {
        system("cls");
        cout<<h<<":"<<m<<":"<<s<<endl;
       if(s>59){
            m++;
            s=0;
       }
       if(m>59){
        h++;
        m=0;
       }
       if(h>11){
        h=1;
       }
       s++;
       _sleep(1000);
    }

    return 0;
}