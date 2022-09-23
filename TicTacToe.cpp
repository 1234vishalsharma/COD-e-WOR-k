#include<iostream>
#include<windows.h>
#include<conio.h>
using namespace std;
char square[10]{'0','1','2','3','4','5','6','7','8','9'};
void drawmatch(){
    system("cls");
    cout<<"Player 1 (X) and Player 2 (Y)\n";
    cout<<"   |     |   \n";
    cout<<square[1] <<"  |  "<<square[2] << "  |  " << square[3];
    cout<<endl;
    cout<<"___|_____|___\n";
    cout<<"   |     |   \n";
    cout<<square[4] << "  |  " << square[5]<< "  |  " << square[6];
    cout<<endl;
    cout<<"___|_____|___\n";
    cout<<"   |     |   \n";
    cout<<square[7] << "  |  " << square[8] << "  |  " << square[9];
    cout<<endl;
    cout<<"   |     |   \n";
}
int checkwin(){
     if     (square[1]==square[2]&&square[2]==square[3]){
        return 1;
    }
    else if(square[4]==square[5]&&square[5]==square[6]){
        return 1;
    }
    else if(square[7]==square[8]&&square[8]==square[9]){
        return 1;
    }
    else if(square[1]==square[5]&&square[5]==square[9]){
        return 1;
    }
    else if(square[1]==square[4]&&square[4]==square[7]){
        return 1;
    }
    else if(square[3]==square[6]&&square[6]==square[9]){
        return 1;
    }
    else if(square[2]==square[5]&&square[5]==square[8]){
        return 1;
    }
    else if(square[1]!='1' && square[2]!='2' && square[3]!='3' && square[4]!='4' && square[5]!='5' && square[6]!='6' && square[7]!='7' && square[8]!='8' && square[9]!='9'){
        return 0;
    }
    else{
        return -1;
    }
    return 0;
}
int main()
{
    int player=1,i,choice;
    char mark;
    do{
        drawmatch();
        player=(player%2) ? 1 : 2;
        cout<<"Player "<<player<<" Enter your Choice (1 to 9)\n";
        cin>>choice;
        mark=(player==1)? 'X':'0';
        if(choice==1 && square[1]=='1'){
            square[1]=mark;
        }else if(choice==2 && square[2]=='2'){
            square[2]=mark;
        }else if(choice==3 && square[3]=='3'){
            square[3]=mark;
        }else if(choice==4 && square[4]=='4'){
            square[4]=mark;
        }else if(choice==5 && square[5]=='5'){
            square[5]=mark;
        }else if(choice==6 && square[6]=='6'){
            square[6]=mark;
        }else if(choice==7 && square[7]=='7'){
            square[7]=mark;
        }else if(choice==8 && square[8]=='8'){
            square[8]=mark;
        }else if(choice==9 && square[1]=='9'){
            square[9]=mark;
        }
        else{
            cout<<"Invalid Option"<<endl;
            player--;
            getch();
        }
        i=checkwin();
        player++;
    }while(i==-1);
    drawmatch();
    if(i==1){
        player--;
        cout<<"Player "<<player<<" Won the game"<<endl;
    }
    else{
        cout<<"Match Draw\n";
    }
    getch();
    return 0;
}