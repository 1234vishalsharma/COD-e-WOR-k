#include<iostream>
#include<string.h>
#include<conio.h>

using namespace std;
class atm{
    long int account_No;
    string name;
    int pin;
    double balance;
    string mobile_no;
    public:
    void setdata(long int account_No_a,string name_a,double balance_a,int pin_a,string mobile_no_a){
        account_No=account_No_a;
        name=name_a;
        balance=balance_a;
        pin=pin_a;
        mobile_no=mobile_no_a;
    }
    long int getaccount_no(){
        return account_No;
    }
    int getpin(){
        return pin;
    }
    double getbalance(){
        return balance;
    }
    string getname(){
        return name;
    }
    string getmobile_no(){
        return mobile_no;
    }
    void check_balance(){
        cout<<"The available balance in your account is: "<<balance<<endl;
    }
    void cash_withdraw(){
        int amnt;
        x:
        cout<<"Enter the amount of cash you want to withdraw: "<<endl;
        cin>>amnt;
        if(amnt>balance){
                cout<<"Cannot have sufficient amount of balance in your account "<<endl;
                goto x;
        }
        else{
            balance=balance-amnt;
            cout<<"Please collect your cash from below"<<endl;
            cout<<"The available balance in your account is: "<<balance<<endl;
        }
    }
    void User_details(){
        cout<<"The name of account holder is: "<<name<<endl;
        cout<<"Mobile No. is: "<<mobile_no<<endl;
        cout<<"Balance in account is: "<<balance<<endl;
        cout<<"Account number is: "<<account_No<<endl;
    }
    void Update_Mobile_no(){
        string old,New;
        z:
        cout<<"Please Enter the old Mobile number: ";
        cin>>old;
        if(old==mobile_no){
            cout<<"Enter the New Mobile number: ";
            cin>>New;
            mobile_no=New;
            cout<<"Mobile number updated successfully: ";
        }
        else{
            cout<<"Old Mobile number does not matched"<<endl;
            cout<<"Please Enter the correct Mobile Number"<<endl;
            goto z;
        }
    }
};
int main()
{
    int choice,accno,pino;
    atm user;
    system("cls");
    user.setdata(987654321,"vishal",200000,4788,"9899955304");
    do{
        system("cls");
        cout<<"********Welcome to the ATM Application*********"<<endl;
        cout<<"Enter your account number:"<<endl;
        cin>>accno;
        cout<<"Enter your PIN Number: "<<endl;
        cin>>pino;

        if((accno==user.getaccount_no())&&(pino==user.getpin())){
            do{
                system("cls");
                cout<<"********Welcome to the ATM Application*********"<<endl;
                cout<<"Select options"<<endl;
                cout<<"1. Check Balance"<<endl;
                cout<<"2. cash Withdraw"<<endl;
                cout<<"3. User details"<<endl;
                cout<<"4. Update Mobile No."<<endl;
                cout<<"5. Exit"<<endl;
                cin>>choice;
                switch (choice)
                {
                case 1:
                    user.check_balance();
                    getch();
                    break;
                case 2:
                    user.cash_withdraw();
                    getch();
                    break;
                case 3:
                    user.User_details();
                    getch();
                    break;
                case 4:
                    user.Update_Mobile_no();
                    getch();
                    break;
                case 5:
                    exit(0);
                    
                default:
                    cout<<"Please enter a valid Choice";
                    break;
                }
            }while(1);
        } 

    }while(1);
      
    return 0;
}