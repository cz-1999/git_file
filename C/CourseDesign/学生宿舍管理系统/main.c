#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include<ctype.h>
#include<windows.h>
#include<conio.h>
#define N 10000

typedef struct stu
{
 char id[30];
 char name[30];
 char dianhua[30];//学生信息
 char susehao[30];
 int chuanghao;
 char bz1[30];//决定信息是否可以删除
 char bz2[30];//寝室长标识
 struct stu *next;
}*linklist,lnode;

typedef struct xuezy
{
char id2[30];
char xueyuan[30];
char zhuanye[30];
char banji[30];
struct xuezy *next4;
}*linklist4,lnode4;

typedef struct qinsz
{
 char susehao2[30];
 char name2[30];
 char id3[30];
 char dianhua2[30];
 int chuanghao2;
 struct qinsz *next5;
}*linklist5,lnode5;

typedef struct yh
{
    char zh[20];
    char mima[20];//账号密码信息
    char f[20];//权限级别
    struct yh *next2;
}*linklist2,lnode2;

typedef struct qs
{
    char qs[30];//宿舍号
    int b;//空闲床位
    struct qs *next3;
}*linklist3,lnode3;
typedef struct xy
{
    char id4[10];
    char xy[30];
    struct xy *next6;
}*linklist6,lnode6;


void suma(linklist head,linklist2 head2,linklist3 head3,linklist4 head4,linklist5 head5);
void denglu(linklist head,linklist2 head2,linklist3 head3,linklist4 head4,linklist5 head5,linklist6 head6);
void gengxin(linklist head,linklist4 head4,linklist5 head5);
void output(linklist head,linklist4 head4,linklist5 head5,linklist6 head6);
void chaxun(linklist head,linklist4 head4,linklist5 head5);
void luru(linklist head,linklist4 head4,linklist5 head5);
void chacw(linklist head,linklist4 head4);
void tjcw(linklist head,linklist3 head3);
void cjyonghu(linklist2 head2);
void scyonghu(linklist2 head2);
void output2(linklist2 head2);
void xgmima(linklist2 head2);
void llyonghu(linklist2 head2);
void load2(linklist2 head2);
void load4(linklist4 head4);
void load5(linklist5 head5);
void load6(linklist6 head6);
void save2(linklist2 head2);
void save5(linklist5 head5);
void shanchu(linklist head,linklist5 head5);
void load(linklist head);
void save(linklist head);
void display(void);
void display2(void);
void display3(void);
void display4(void);
void guanliyuan(linklist head,linklist2 head2,linklist4 head4,linklist5 head5,linklist6 head6);
int main()
{
    linklist head;
    linklist2 head2;
    linklist3 head3;
    linklist4 head4;
    linklist5 head5;
    linklist6 head6;
    head = (linklist)malloc(sizeof(lnode));
    head2 = (linklist2)malloc(sizeof(lnode2));
    head3 = (linklist3)malloc(sizeof(lnode3));
    head4 = (linklist4)malloc(sizeof(lnode4));
    head5 = (linklist5)malloc(sizeof(lnode5));
    head6 = (linklist6)malloc(sizeof(lnode6));
    head->next=NULL;
    head2->next2=NULL;
    head3->next3=NULL;
    head4->next4=NULL;
    head5->next5=NULL;
    head6->next6=NULL;
    load(head);
    load2(head2);
    load4(head4);
    load5(head5);
    load6(head6);
    denglu(head,head2,head3,head4,head5,head6);

}
void guanliyuan(linklist head,linklist2 head2,linklist4 head4,linklist5 head5,linklist6 head6)
{
    int a,num;
loop: system( "cls" );
	printf( "\n\n\t\t    **************功能列表**************\n");
    printf( "\n\t\t\t       1.用户管理" );
	printf( "\n\t\t\t       2.学生信息" );
	printf( "\n\t\t\t       0.退出\n" );
	printf( "\n\t\t    ************************************\n" );
	printf( "请输入你的选择：" );
	scanf("%d", &num );
	if(num==1)
    {
    system("cls");
    while(1)
    {
    display();
    scanf("%d",&a);
    switch(a)
    {
    case 1:
        cjyonghu(head2);break;
    case 2:
        scyonghu(head2);break;
    case 3:
        llyonghu(head2);break;
    case 4:
        xgmima(head2);break;
    default:
        goto loop;break;
    }
    }
    }
    else if(num==2)
    {
    while(1)
    {
    system("cls");
    display4();
    scanf("%d",&a);
    switch(a)
    {
    case 1:
        luru(head,head4,head5);break;
    case 2:
        gengxin(head,head4,head5);break;
    case 3:
        shanchu(head,head5);break;
    case 4:
        output(head,head4,head5,head6);break;
    case 5:
        chaxun(head,head4,head5);break;
    default:
        goto loop;break;
    }
    }
    }
    else if(num==0)
        exit(0);

}
void display(void)
{
printf("欢迎您！！！超级管理员\n");
printf("请输入数字选择相应功能                 \n");
printf("1.创建用户                            \n");
printf("2.删除用户                            \n");
printf("3.浏览用户                            \n");
printf("4.修改密码                            \n");
printf("0.返回上一级                                \n");
}
void display4(void)
{
printf("                                         へ　　　　　／|\n");
printf("欢迎您！！！超级管理员                  /＼7　　　 ∠＿/\n");
printf("                                       /　│　　 ／　／\n");
printf("                                      │　Z ＿,＜　／　　 /`ヽ\n");
printf("1.录入信息                            │　　　　　ヽ　　 /　　〉\n");
printf("2.更新信息                             Y　　　　　`　 /　　/\n");
printf("3.删除信息                             r●　.　● ）　　〈\n");
printf("4.浏览信息                             0　 へ　　　　|　＼\n");
printf("5.查询信息                               >-_　 　-/ ／ ／\n");
printf("0.返回上一级                           / へ　　 /　＜＼＼\n");
printf("                                      ヽ_?　　(_／　 ／／\n");
printf("                                       7　　　　　　|／\n");
printf("                                      ＞―r￣￣`?―＿\n");

}
void suma(linklist head,linklist2 head2,linklist3 head3,linklist4 head4,linklist5 head5)
{
    int a;
    while(1)
    {
    display2();
    scanf("%d",&a);
    switch(a)
    {
    case 1:
        xgmima(head2);break;
    case 2:
        chaxun(head,head4,head5);break;
    case 3:
        chacw(head,head4);break;
    case 4:
        tjcw(head,head3);break;
    default:
        exit(0);break;

    }
    }
}
void display2(void)
{
    printf("欢迎您！！！\n");
    printf("请输入数字选择相应的功能\n");
    printf("1:用户管理\n");
    printf("2:查询信息\n");
    printf("3:查询床位\n");
    printf("4:统计空闲床位\n");
    printf("其他字符:退出\n");
    printf(" へ　　　　　／|\n/＼7　　　 ∠＿/\n/　│　　 ／　／\n│　Z ＿,＜　／　　 /`ヽ\n│　　　　　ヽ　　 /　　〉\n Y　　　　　`　 /　　/\n r●　.　● ）　　〈　　\n 0　 へ　　　　|　＼\n   >-\_　 　-/ ／ ／\n / へ　　 /　＜＼＼\nヽ_?　　(_／　 ／／\n 7　　　　　　|／\n＞―r￣￣`?―＿\n");
}
void denglu(linklist head,linklist2 head2,linklist3 head3,linklist4 head4,linklist5 head5,linklist6 head6)
{
int c,i=0,num;
char zh[20],mima[20]="\0";
char a[6]={'V','\0'},b[6]={'P','\0'},d;
linklist2 p = head2->next2;
printf("欢迎来到学生宿舍管理系统,请进行登录\n");
printf(" へ　　　　　／|\n/＼7　　　 ∠＿/\n/　│　　 ／　／\n│　Z ＿,＜　／　　 /`ヽ\n│　　　　　ヽ　　 /　　〉\n Y　　　　　`　 /　　/\n r●　.　● ）　　〈　　\n 0　 へ　　　　|　＼\n   >-\_　 　-/ ／ ／\n / へ　　 /　＜＼＼\nヽ_?　　(_／　 ／／\n 7　　　　　　|／\n＞―r￣￣`?―＿\n");
printf("1.用户登录\n");
printf("2.管理员登录\n");
printf("0.退出\n");
printf("请进行选择\n");
scanf("%d",&num);
system("cls");
if(num==0)
    exit(0);
printf("请输入账号,按回车键结束\n");
scanf("%s",zh);
printf("请输入密码,按回车键结束\n");
while ((d=getch()) != '\r')
{
    mima[i] = d;
    i++;
    if(d!='\b')    //输入内容不是退格时就显示 “*”号
    {
    printf("*");
    }
    else     //输入内容是退格时 删除前一个 “*”号
    {
    printf("\b \b");
    }
}
system("cls");
while(p)
{
  if(strcmp(zh,p->zh)==0&&strcmp(mima,p->mima)==0&&strcmp(a,p->f)==0)
  {
      guanliyuan(head,head2,head4,head5,head6);
      break;
  }
  if(strcmp(zh,p->zh)==0&&strcmp(mima,p->mima)==0&&strcmp(b,p->f)==0)
  {
       suma(head,head2,head3,head4,head5);
      break;
  }
  p=p->next2;
}
printf("输入账号或密码错误\n");
printf("1.重新输入  其他字符.退出\n");
scanf("%d",&c);
if(c==1)
while(1)
{
p=head2->next2;
printf("请输入账号,按回车键结束\n");
scanf("%s", zh);
printf("请输入密码,按回车键结束\n");
i=0;
while ((d=getch()) != '\r')
{
    mima[i] = d;
    i++;
    if(d!='\b')    //输入内容不是退格时就显示 “*”号
    {
    printf("*");
    }
    else     //输入内容是退格时 删除前一个 “*”号
    {
    printf("\b \b");
    }
}
system("cls");
while(p)
{
  if(strcmp(zh,a)==0&&strcmp(mima,b)==0)
  {
      guanliyuan(head,head2,head4,head5,head6);
      break;
  }
  if(strcmp(zh,p->zh)==0&&strcmp(mima,p->mima)==0)
  {
      suma(head,head2,head3,head4,head5);
      break;
  }
  p=p->next2;
}
printf("输入账号或密码错误\n");
printf("1.重新输入  其他字符.退出\n");
scanf("%d",&c);
if(c==1)
    continue;
else
    return;
}
else
    exit(0);
}
void load2(linklist2 head2)
{
linklist2 p,rear=head2;
char zh[20],mima[20],f[20];
FILE *fp;
if((fp=fopen("zhanghao.txt","r"))==NULL)
{
     printf("open error\n");
     exit(0);
}

while((fscanf(fp,"%s %s %s\n",zh,mima,f))!=EOF)
{
        p = (linklist2)malloc(sizeof(lnode2));
        strcpy(p->zh,zh);
        strcpy(p->mima,mima);
        strcpy(p->f,f);
        rear->next2 = p;
        rear = p;
}
rear->next2=NULL;
fclose(fp);
}
void save2(linklist2 head2)
{
linklist2 p=head2->next2;
char mima[20],zh[20],f[20];
FILE *fp;
if((fp=fopen("zhanghao.txt","w"))==NULL)
   {
       printf("open error\n");
       return;
   }
while(p)
 {
     strcpy(zh,p->zh);
     strcpy(mima,p->mima);
     strcpy(f,p->f);
     fprintf(fp,"%s %s %s\n",zh,mima,f);
     p=p->next2;
 }
fclose(fp);
}

void cjyonghu(linklist2 head2)
{
        linklist2 p = head2->next2;
        char zh[20],mima[20],f[20];
        int a,n=11,b=0;
        while(p)
        {
            b++;
            p=p->next2;
        }
        printf("请选择1.逐个创建 2.批量创建 3.其他字符退出\n");
        scanf("%d",&a);
        if(a==1)
        {
        p = head2->next2;
        system("cls");
        printf("请输入要创建的账号,以回车键结束\n");
        scanf("%s",zh);
        while(p)
        {
            if(strcmp(zh,p->zh)==0)
            {
                printf("该账号已存在\n");
                break;
            }
            if(p->next2==NULL)
            {
                printf("请输入密码,以回车键结束\n");
                scanf("%s",mima);
                printf("请选择帐户的权限级别 V.管理员 P.用户\n");
                scanf("%s",f);
                p=(linklist2)malloc(sizeof(lnode2));
                strcpy(p->zh,zh);
                strcpy(p->mima,mima);
                strcpy(p->f,f);
                p->next2=head2->next2;
                head2->next2=p;
                p=head2->next2;
                system("cls");
                printf("现在系统中共有%d个帐户\n",b+1);
                printf("现有的帐户为:\n");
                output2(head2);
                save2(head2);
                break;
            }
            p=p->next2;
        }
        }
       else if(a==2)
        {
        printf("请输入要批量创建10个的账号,以回车键结束\n");
        while(n--)
        {
        p = head2->next2;
        printf("请输入要创建的帐号\n");
        scanf("%s",zh);
        while(p)
        {
            if(strcmp(zh,p->zh)==0)
            {
                printf("该账号已存在\n请继续输入\n");
                break;
            }
            if(p->next2==NULL)
            {
                printf("请输入密码\n");
                scanf("%s",mima);
                printf("请选择帐户的权限级别 V.管理员 P.用户\n");
                scanf("%s",f);
                p=(linklist2)malloc(sizeof(lnode2));
                strcpy(p->zh,zh);
                strcpy(p->mima,mima);
                strcpy(p->f,f);
                p->next2=head2->next2;
                head2->next2=p;
                p=head2->next2;
                b++;
                save2(head2);
                break;
            }
            p=p->next2;
        }
        if(n==1)
        {
                system("cls");
                printf("现在系统中共有%d个帐户\n",b);
                printf("现有的帐户为:\n");
                output2(head2);
                break;
        }
        }

        }
        else
             exit(0);
}
void scyonghu(linklist2 head2)
{
    linklist2 p=head2->next2,rear;
    char zh[20];
    int n=11,a,b=0;
    while(p)
    {
    b++;
    p=p->next2;
    }
printf("请选择1.逐个删除 2.批量删除 3.其他字符返回上一级\n");
scanf("%d",&a);
if(a==1)
{
    p=head2->next2,rear=head2;
    printf("请输入要删除的账号\n");
    scanf("%s",zh);
    while(p)
    {
        if(strcmp(zh,p->zh)==0)
        {
            rear->next2=p->next2;
            free(p);
            system("cls");
            printf("现在系统中共有%d个帐户\n",b-1);
            printf("删除后的信息为:\n");
            output2(head2);
            break;
        }
        if(p->next2==NULL)
        {
            system("cls");
            printf("要删除的信息不存在\n");
            break;
        }
        rear=rear->next2;
        p=p->next2;
    }
    save2(head2);

}
else if(a==2)
{
    printf("请输入要批量删除10个账号\n");
    while(n--)
    {
    p=head2->next2,rear=head2;
    scanf("%s",zh);
    while(p)
    {
        if(strcmp(zh,p->zh)==0)
        {
            rear->next2=p->next2;
            free(p);
            b--;
            break;
        }
        if(p->next2==NULL)
        {
            printf("要删除的信息不存在\n");
            printf("请继续输入\n");
        }
        rear=rear->next2;
        p=p->next2;
    }
            if(n==1)
        {
            system("cls");
            printf("现在系统中共有%d个帐户\n",b);
            printf("删除后的信息为:\n");
            output2(head2);
            break;
        }
   }
    save2(head2);
}

}
void llyonghu(linklist2 head2)
{
    linklist2 p=head2->next2;
    system("cls");
    printf("%-20s%-20s%-20s\n","帐号","密码","权限级别");
    while(p)
    {
     printf("%-20s%-20s%-20s\n",p->zh,p->mima,p->f);
     p=p->next2;
    }
}
void xgmima(linklist2 head2)
{
    linklist2 p=head2->next2;
    char zh[20],mima[20];
    printf("请输入要修改密码的帐号\n");
    scanf("%s",zh);
    while(p)
    {
        if(strcmp(zh,p->zh)==0)
        {
            printf("请输入修改后的密码\n");
            scanf("%s",mima);
            system("cls");
            strcpy(p->mima,mima);
            printf("修改后帐号的信息为:\n");
            printf("%s %-20s\n","帐号","密码");
            printf("%s %-20s\n",zh,mima);
            break;
        }
        if(p->next2==NULL)
        {
            system("cls");
            printf("要修改的帐号不存在\n");
            break;
        }
        p=p->next2;
    }
        save2(head2);
}

void load(linklist head)
{
linklist p,rear=head;
char susehao[30];
int chuanghao;
char name[30];
char id[30];
char dianhua[30];
char bz1[10],bz2[10];
FILE *fp;
fp=fopen("xuesheng.txt","r");
while((fscanf(fp,"%s %d %s %s %s %s %s\n",susehao,&chuanghao,name,id,dianhua,bz1,bz2))!=EOF)
{
    p=(linklist)malloc(sizeof(lnode));
    strcpy(p->susehao,susehao);
    strcpy(p->name,name);
    strcpy(p->id,id);
    strcpy(p->dianhua,dianhua);
    strcpy(p->bz1,bz1);
    strcpy(p->bz2,bz2);
    p->chuanghao=chuanghao;
    rear->next=p;
    rear=p;
}
rear->next=NULL;
p=head->next;
/*while(p)
{
printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s\n",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
p=p->next;
}*/
fclose(fp);
}

void load4(linklist4 head4)
{
linklist4 p4,rear=head4;
char id2[30];
char xueyuan[30];
char zhuanye[30];
char banji[30];
FILE *fp;
fp=fopen("xuezb.txt","r");
while((fscanf(fp,"%s %s %s %s\n",id2,xueyuan,zhuanye,banji))!=EOF)
{
    p4=(linklist4)malloc(sizeof(lnode4));
    strcpy(p4->id2,id2);
    strcpy(p4->xueyuan,xueyuan);
    strcpy(p4->zhuanye,zhuanye);
    strcpy(p4->banji,banji);
    rear->next4=p4;
    rear=p4;
}
rear->next4=NULL;
/*p4=head4->next4;
while(p4)
{
    printf("%s %s %s\n",p4->xueyuan,p4->zhuanye,p4->banji);
    p4=p4->next4;
}*/
fclose(fp);
}

void load5(linklist5 head5)
{
linklist5 p3,rear=head5;
char susehao2[30];
char name2[30];
char id3[30];
char dianhua2[30];
FILE *fp;
fp=fopen("qinshizhang.txt","r");
while(fscanf(fp,"%s %s %s %s\n",susehao2,name2,id3,dianhua2)!=EOF)
{
    p3=(linklist5)malloc(sizeof(lnode5));
    strcpy(p3->susehao2,susehao2);
    strcpy(p3->name2,name2);
    strcpy(p3->id3,id3);
    strcpy(p3->dianhua2,dianhua2);
    rear->next5=p3;
    rear=p3;
}
rear->next5=NULL;
p3=head5->next5;
/*while(p3)
{
printf("%s %d %s %s %s\n",p3->susehao2,p3->chuanghao2,p3->name2,p3->id3,p3->dianhua2);
p3=p3->next5;
}*/
fclose(fp);
}

void save(linklist head)
{
linklist p=head->next;
char susehao[30];
int chuanghao;
char name[30];
char id[30];
char dianhua[30];
char bz1[10],bz2[10];
FILE *fp;
if((fp=fopen("xuesheng.txt","w"))==NULL)
   {
       printf("open error\n");
       return;
   }
while(p)
{
    strcpy(susehao,p->susehao);
    strcpy(name,p->name);
    strcpy(id,p->id);
    strcpy(dianhua,p->dianhua);
    strcpy(bz1,p->bz1);
    strcpy(bz2,p->bz2);
    chuanghao=p->chuanghao;
fprintf(fp,"%s %d %s %s %s %s %s\n",susehao,chuanghao,name,id,dianhua,bz1,bz2);
p=p->next;
}
fclose(fp);
}
void save5(linklist5 head5)
{
linklist5 p=head5->next5;
char susehao2[30];
char name2[30];
char id3[30];
char dianhua2[30];
FILE *fp;
fp=fopen("qinshizhang.txt","w");
while(p)
{
    strcpy(susehao2,p->susehao2);
    strcpy(name2,p->name2);
    strcpy(id3,p->id3);
    strcpy(dianhua2,p->dianhua2);
    fprintf(fp,"%s %s %s %s\n",susehao2,name2,id3,dianhua2);
    p=p->next5;
}
fclose(fp);
}
 void luru(linklist head,linklist4 head4,linklist5 head5)
{
        linklist p,r;
        linklist4 p4;
        char susehao[30],name[30],id[30],dianhua[30],bz1[30],b[30],c[30];
        int a,n=11,chuanghao,f=10;
        c[0]='P',c[1]='\0';
        printf("请选择 1.逐个录入 2.批量录入 3.其他字符.返回上一级\n");
        scanf("%d",&a);
        if(a==1)
        {
        p = head->next;
        printf("请输入学号,以回车键结束\n");
        scanf("%s",id);
        while(p)
        {
            if(strcmp(id,p->id)==0)
            {p=head->next;
                system("cls");
                printf("该学生信息已存在\n");
                break;
            }
            if(p->next==NULL)
            {
                printf("请输入姓名,以回车键结束\n");
                scanf("%s",name);
                printf("请输入电话,以回车键结束\n");
                scanf("%s",dianhua);
                printf("请输入宿舍号,以回车键结束\n");
                scanf("%s",susehao);
                printf("请输入床位号,以回车键结束\n");
                scanf("%d",&chuanghao);
                printf("请输入能否删除信息,Y.可删除 N.不可删除 以回车键结束\n");
                scanf("%s",bz1);
                r =(linklist)malloc(sizeof(lnode));
                strcpy(r->susehao,susehao);
                strcpy(r->name,name);
                strcpy(r->id,id);
                strcpy(r->dianhua,dianhua);
                strcpy(r->bz1,bz1);
                strcpy(r->bz2,c);
                r->chuanghao=chuanghao;
                r->next=head->next;
                head->next=r;
                system("cls");
                printf("录入的学生信息为:\n");
                printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
                printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s",r->susehao,r->chuanghao,r->name,r->id,r->dianhua,r->bz1,r->bz2);
                p4=head4->next4;
                sscanf(r->id,"%*4d%6d%*2d",&a);
                b[6]='\0',b[5]=a%10+'0',b[4]=a/10%10+'0',b[3]=a/100%10+'0',b[2]=a/1000%10+'0',b[1]=a/10000%10+'0',b[0]=a/100000+'0';
                    while(p4)
                {
                    if((strcmp(p4->id2,b))==0)
                    {
                    printf("%-20s %-20s %-20s\n",p4->xueyuan,p4->zhuanye,p4->banji);
                    break;
                    }
                    p4=p4->next4;
                }
                        save(head);
                }
                    p=p->next;
        }
        }
       else if(a==2)
        {
        printf("请输入要批量录入10个的信息,以回车键结束\n");
        while(n--)
        {
         p = head->next;
        printf("请输入学号,以回车键结束\n");
        scanf("%s",id);
        while(p)
        {
            if(strcmp(id,p->id)==0)
            {p=head->next;
                system("cls");
                printf("该学生信息已存在\n");
                break;
            }
            if(p->next==NULL)
            {
                printf("请输入姓名,以回车键结束\n");
                scanf("%s",name);
                printf("请输入电话,以回车键结束\n");
                scanf("%s",dianhua);
                printf("请输入宿舍号,以回车键结束\n");
                scanf("%s",susehao);
                printf("请输入床位号,以回车键结束\n");
                scanf("%d",&chuanghao);
                printf("请输入能否删除信息,Y.可删除 N.不可删除 以回车键结束\n");
                scanf("%s",bz1);
                r =(linklist)malloc(sizeof(lnode));
                strcpy(r->susehao,susehao);
                strcpy(r->name,name);
                strcpy(r->id,id);
                strcpy(r->dianhua,dianhua);
                strcpy(r->bz1,bz1);
                strcpy(r->bz2,c);
                r->chuanghao=chuanghao;
                r->next=head->next;
                head->next=r;
                system("cls");
                printf("录入的学生信息为:\n");
                printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
                printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s",r->susehao,r->chuanghao,r->name,r->id,r->dianhua,r->bz1,r->bz2);
                p4=head4->next4;
                sscanf(r->id,"%*4d%6d%*2d",&a);
                b[6]='\0',b[5]=a%10+'0',b[4]=a/10%10+'0',b[3]=a/100%10+'0',b[2]=a/1000%10+'0',b[1]=a/10000%10+'0',b[0]=a/100000+'0';
                    while(p4)
                {
                    if((strcmp(p4->id2,b))==0)
                    {
                    printf("%-20s %-20s %-20s\n",p4->xueyuan,p4->zhuanye,p4->banji);
                    break;
                    }
                    p4=p4->next4;
                }
                        save(head);
                }
                    p=p->next;
        }

        if(n==1)
        {
                system("cls");
                p=head->next;
                printf("录入的学生信息为:\n");
                printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
                while(f--)
                {
                printf("%-20s %-20d %-20s %-20s %-20s %-20s %-20s",r->susehao,r->chuanghao,r->name,r->id,r->dianhua,r->bz1,r->bz2);
                p4=head4->next4;
                sscanf(p->id,"%*4d%6d%*2d",&a);
                 b[6]='\0',b[5]=a%10+'0',b[4]=a/10%10+'0',b[3]=a/100%10+'0',b[2]=a/1000%10+'0',b[1]=a/10000%10+'0',b[0]=a/100000+'0';
                    while(p4)
                {
                    if((strcmp(p4->id2,b))==0)
                    printf("%-20s %-20s %-20s\n",p4->xueyuan,p4->zhuanye,p4->banji);
                    p4=p4->next4;
                }
                p=p->next;
                }
                break;
        }
        }
        }


}
 void gengxin(linklist head,linklist4 head4,linklist5 head5)
 {
    char susehao[30],dianhua[30],id[30],bz1[30],bz2[30],b[30],d[30],e[30],f[30],id3[30];
    linklist p=head->next;
    linklist4 p4;
    linklist5 p5;
    int a,chuanghao,c;
    d[0]=' ',d[1]='\0';
    e[0]='V',e[1]='\0';
    f[0]='P',f[1]='\0';
    printf("请输入要更改信息的学号\n");
    scanf("%s",id);
    while(p)
    {
    p4=head4->next4;
    p5=head5->next5;
    if(strcmp(id,p->id)==0)
    {
        printf("请输入数字选择相应功能\n");
        printf("1.宿舍号\n");
        printf("2.床号\n");
        printf("3.电话\n");
        printf("4.是否正常毕业,Y 正常毕业 N 非正常毕业\n");
        printf("5.是否寝室长,V 寝室长 P 普通成员\n");
        printf("其它字符返回上一级\n");
        scanf("%d",&a);
        if(a==1)
        {
            p4=head4->next4;
            p5=head5->next5;
            printf("请输入新的宿舍号\n");
            scanf("%s",susehao);
            strcpy(p->susehao,susehao);
            system("cls");
            printf("修改后的信息为\n");
            printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
            printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
            sscanf(p->id,"%*4d%6d%*2d",&c);
            b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
            while(p4)
            {
                if((strcmp(p4->id2,b))==0)
                {
                printf("%-20s %-20s %-20s\n",p4->xueyuan,p4->zhuanye,p4->banji);
                break;
                }
                p4=p4->next4;
            }
            while(p5)
            {
                if((strcmp(p5->susehao2,p->susehao))==0)
                {
                printf("%-20s %-10s %-10s %-20s %-20s\n","寝室长",d,p5->name2,p5->id3,p5->dianhua2);
                break;
                }
                p5=p5->next5;
            }
                    save(head);
                    break;
            }
        else if(a==2)
        {
            p4=head4->next4;
            p5=head5->next5;
            printf("请输入新的床号\n");
            scanf("%d",&chuanghao);
            p->chuanghao=chuanghao;
            system("cls");
            printf("修改后的信息为\n");
                        printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
            printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
            sscanf(p->id,"%*4d%6d%*2d",&c);
            b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
            while(p4)
            {
                if((strcmp(p4->id2,b))==0)
                {
                printf("%-20s %-20s %-20s\n",p4->xueyuan,p4->zhuanye,p4->banji);
                break;
                }
                p4=p4->next4;
            }
            while(p5)
            {
                if((strcmp(p5->susehao2,p->susehao))==0)
                {
                printf("%-20s %-10s %-10s %-20s %-20s\n","寝室长",d,p5->name2,p5->id3,p5->dianhua2);
                break;
                }
                p5=p5->next5;
            }
                save(head);
                break;
        }
        else if(a==3)
        {
            p4=head4->next4;
            p5=head5->next5;
            printf("请输入新的电话号\n");
            scanf("%s",dianhua);
            strcpy(p->dianhua,dianhua);
            system("cls");
            printf("修改后的信息为\n");
                        printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
            printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
            sscanf(p->id,"%*4d%6d%*2d",&c);
            b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
            while(p4)
            {
                if((strcmp(p4->id2,b))==0)
                {
                printf("%-20s %-20s %-20s\n",p4->xueyuan,p4->zhuanye,p4->banji);
                break;
                }
                p4=p4->next4;
            }
            while(p5)
            {
                if((strcmp(p5->susehao2,p->susehao))==0)
                {
                printf("%-20s %-10s %-10s %-20s %-20s\n","寝室长",d,p5->name2,p5->id3,p5->dianhua2);
                break;
                }
                p5=p5->next5;
            }
                save(head);
                break;
        }
    else if(a==4)
    {
            p4=head4->next4;
            p5=head5->next5;
            printf("请输入是否正常毕业 Y.正常 N.不正常\n");
            scanf("%s",bz1);
            strcpy(p->bz1,bz1);
            system("cls");
            printf("修改后的信息为\n");
            printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
            printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
            sscanf(p->id,"%*4d%6d%*2d",&c);
            b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
            while(p4)
            {
                if((strcmp(p4->id2,b))==0)
                {
                printf("%-20s %-20s %-20s\n",p4->xueyuan,p4->zhuanye,p4->banji);
                break;
                }
                p4=p4->next4;
            }
            while(p5)
            {
                if((strcmp(p5->susehao2,p->susehao))==0)
                {
                printf("%-20s %-10s %-10s %-20s %-20s\n","寝室长",d,p5->name2,p5->id3,p5->dianhua2);
                break;
                }
                p5=p5->next5;
            }
                save(head);
                break;

    }
    else if(a==5)
    {
            strcpy(id,p->id);
            printf("请输入是否为寝室长 V.是 P.不是\n");
            scanf("%s",bz2);
            if((strcmp(bz2,e))==0)
            {
                strcpy(p->bz2,e);
                p5=head5->next5;
                while(p5)
                {
                    if((strcmp(p5->susehao2,p->susehao))==0)
                    {
                        strcpy(id3,p5->id3);
                        strcpy(p5->name2,p->name);
                        strcpy(p5->id3,p->id);
                        strcpy(p5->dianhua2,p->dianhua);
                        save5(head5);
                        break;
                    }
                    p5=p5->next5;
                }
                p=head->next;
                while(p)
                {
                    if((strcmp(p->id,id3))==0)
                    {
                        strcpy(p->bz2,f);
                        save(head);
                        break;
                    }
                    p=p->next;
                }
                save(head);

            }
            system("cls");
            printf("修改后的信息为\n");
            p=head->next;
            while(p)
            {
                if((strcmp(p->id,id))==0)
                    break;
                p=p->next;
            }
            printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
            printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
            sscanf(p->id,"%*4d%6d%*2d",&c);
            b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
            p4=head4->next4;
            p5=head5->next5;
            while(p4)
            {
                if((strcmp(p4->id2,b))==0)
                {
                printf("%-20s %-20s %-20s\n",p4->xueyuan,p4->zhuanye,p4->banji);
                break;
                }
                p4=p4->next4;
            }
            while(p5)
            {
                if((strcmp(p5->susehao2,susehao))==0)
                {
                printf("%-20s %-10s %-10s %-20s %-20s\n","寝室长",d,p5->name2,p5->id3,p5->dianhua2);
                break;
                }
                p5=p5->next5;
            }
            save(head);
            save5(head5);
                break;


    }
  }
      if(p->next==NULL)
    {
        printf("该学号不存在\n");
        break;
    }
    p=p->next;
 }
 }
void shanchu(linklist head,linklist5 head5)
{
    linklist p,pre;
    linklist5 p5=head5->next5;
    char susehao[30],dianhua[30],id[30],bz2[30],name[30],bz1[30];
    int a,n=11,s=0;
    bz2[0]='V',bz2[1]='\0';
    bz1[0]='Y',bz1[1]='\0';
    printf("请选择1.逐个删除 2.批量删除 3.其他字符返回上一级\n");
    scanf("%d",&a);
    if(a==1)
    {
        p = head->next;
        pre=head;
        printf("请输入要删除的信息\n");
        printf("请输入学号\n");
        scanf("%s",id);
        while(p5)
        {
         s++;
         p5=p5->next5;
        }
        while(p)
        {
           if((strcmp(p->id,id))==0&&(strcmp(p->bz1,bz1))==0)
           {
            if((strcmp(p->bz2,bz2))==0)
            {

                if(s!=1)
                {
                    strcpy(susehao,p->susehao);
                    pre->next=p->next;
                    free(p);
                    p=head->next;
                    while(p)
                    {
                       if((strcmp(p->susehao,susehao))==0)
                       {
                            strcpy(name,p->name);
                            strcpy(id,p->id);
                            strcpy(dianhua,p->dianhua);
                            strcpy(p->bz2,bz2);
                            save(head);
                            break;
                       }
                       p=p->next;
                    }
                    p5=head5->next5;
                    while(p5)
                    {
                        if((strcmp(p5->susehao2,susehao))==0)
                        {
                            strcpy(p5->name2,name);
                            strcpy(p5->id3,id);
                            strcpy(p5->dianhua2,dianhua);
                            save5(head5);
                            break;
                        }
                        p5=p5->next5;
                    }
                    system("cls");
                    printf("删除成功\n");
                    break;
                }
                else
                {
                    pre->next=p->next;
                    free(p);
                    system("cls");
                    printf("删除成功\n");
                    break;
                }
                break;
            }
            else
            {
              pre->next=p->next;
              free(p);
              system("cls");
              printf("删除成功\n");
              break;
            }
                break;
           }
           if(p->next==NULL)
           {
               system("cls");
               printf("要删除的信息不存在或该信息不能删除\n");
               break;
           }
            p=p->next;
            pre=pre->next;
        }
        save(head);

     }
    else if(a==2)
    {
        p=head->next,pre=head;
        printf("请输入要批量删除10个学生信息,输入学号即可\n");
        while(n--)
        {
        p=head->next,pre=head;
        p5=head5->next5;
        s=0;
        scanf("%s",id);
        while(p5)
        {
         s++;
         p5=p5->next5;
        }
        while(p)
        {
           if((strcmp(p->id,id))==0&&(strcmp(p->bz1,bz1))==0)
           {
            if((strcmp(p->bz2,bz2))==0)
            {

                if(s!=1)
                {
                    strcpy(susehao,p->susehao);
                    pre->next=p->next;
                    free(p);
                    p=head->next;
                    while(p)
                    {
                       if((strcmp(p->susehao,susehao))==0)
                       {
                            strcpy(name,p->name);
                            strcpy(id,p->id);
                            strcpy(dianhua,p->dianhua);
                            strcpy(p->bz2,bz2);
                            save(head);
                            break;
                       }
                       p=p->next;
                    }
                    p5=head5->next5;
                    while(p5)
                    {
                        if((strcmp(p5->susehao2,susehao))==0)
                        {
                            strcpy(p5->name2,name);
                            strcpy(p5->id3,id);
                            strcpy(p5->dianhua2,dianhua);
                            break;
                        }
                        p5=p5->next5;
                    }
                    break;
                }
                else
                {
                    pre->next=p->next;
                    free(p);
                    break;
                }
                break;
            }
            else
            {
              pre->next=p->next;
              free(p);
              break;
            }
                break;
           }
           if(p->next==NULL)
           {
               printf("要删除的信息不存在或该信息不能删除\n请继续删除\n");
               break;
           }
            p=p->next;
            pre=pre->next;
        }
                if(n==1)
            {
                system("cls");
                printf("删除成功\n");
                break;
            }
       }
    save(head);
}
}
void chaxun(linklist head,linklist4 head4,linklist5 head5)
{
    linklist p=head->next;
    linklist4 p4;
    linklist5 p5;
    int a,c;
    char id[30],dianhua[30],name[30],b[30];
    display3();
    scanf("%d",&a);
    if(a==1)
    {
    printf("请输入学号\n");
    scanf("%s",id);
    while(p)
    {
        if(strcmp(id,p->id)==0)
        {
        p4=head4->next4;
        p5=head5->next5;
        printf("%-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长");
        sscanf(p->id,"%*4d%6d%*2d",&c);
        printf("%-20s %-20d %-20s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
        b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
        while(p4)
        {

            if((strcmp(p4->id2,b))==0)
            printf("%s %s %s",p4->xueyuan,p4->zhuanye,p4->banji);
            p4=p4->next4;
        }
        while(p5)
        {
            if((strcmp(p5->susehao2,p->susehao))==0)
            printf("%s %s %s %s\n",p5->susehao2,p5->name2,p5->id3,p5->dianhua2);
            p5=p5->next5;
        }
        break;
        }
        if(p->next==NULL)
        {
            printf("要查找的信息不存在\n");
            break;
        }
        p=p->next;
    }
    }
        else if(a==2)
    {
    printf("请输入电话\n");
    scanf("%s",dianhua);
    while(p)
    {
        if(strcmp(dianhua,p->dianhua)==0)
        {
        p4=head4->next4;
        p5=head5->next5;
        printf("%-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长");
        sscanf(p->id,"%*4d%6d%*2d",&c);
        printf("%-20s %-20d %-20s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
        b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
        while(p4)
        {

            if((strcmp(p4->id2,b))==0)
            printf("%s %s %s",p4->xueyuan,p4->zhuanye,p4->banji);
            p4=p4->next4;
        }
        while(p5)
        {
            if((strcmp(p5->susehao2,p->susehao))==0)
            printf("%s %s %s %s\n",p5->susehao2,p5->name2,p5->id3,p5->dianhua2);
            p5=p5->next5;
        }
        break;

        }
        if(p->next==NULL)
        {
            printf("要查找的信息不存在\n");
            break;
        }
        p=p->next;
    }
    }
   else  if(a==3)
    {
    printf("请输入姓名\n");
    scanf("%s",name);
    while(p)
    {
        if(strcmp(name,p->name)==0)
        {
        p4=head4->next4;
        p5=head5->next5;
        printf("%-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长");
        sscanf(p->id,"%*4d%6d%*2d",&c);
        printf("%-20s %-20d %-20s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
        b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
        while(p4)
        {

            if((strcmp(p4->id2,b))==0)
            printf("%s %s %s",p4->xueyuan,p4->zhuanye,p4->banji);
            p4=p4->next4;
        }
        while(p5)
        {
            if((strcmp(p5->susehao2,p->susehao))==0)
            printf("%s %s %s %s\n",p5->susehao2,p5->name2,p5->id3,p5->dianhua2);
            p5=p5->next5;
        }
        break;
        }
        if(p->next==NULL)
        {
            printf("要查找的信息不存在\n");
            break;
        }
        p=p->next;
    }
    }

}
void display3(void)
{
    system("cls");
    printf("欢迎来到查询系统\n");
    printf("请输入数字选择相应功能\n");
    printf("1.按学号查询\n");
    printf("2.按电话查询\n");
    printf("3.按姓名查询\n");
    printf("其它字符.返回上一级\n");
}
void chacw(linklist head,linklist4 head4)
{
    linklist p=head->next;
    //linklist4 p4;
    char susehao[30];
    int n=6;
    printf("请输入要查询的寝室号\n");
    scanf("%s",susehao);
while(p)
{
if(strcmp(susehao,p->susehao)==0)
{
    n--;
}
    p=p->next;
}
system("cls");
//printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
p=head->next;
while(p)
{
if(strcmp(susehao,p->susehao)==0)
{
        /*p4=head4->next4;
        sscanf(p->id,"%*4d%6d%*2d",&c);
        printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
        b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
        while(p4)
        {

            if((strcmp(p4->id2,b))==0)
            printf("%-20s %-20s %-20s",p4->xueyuan,p4->zhuanye,p4->banji);
            p4=p4->next4;
        }*/
printf("%-20s%-20s%-20s\n","宿舍号","空闲床位","人数");
printf("%-20s%-20d%-20d\n",susehao,n,6-n);
break;
}
if(p->next==NULL)
{
   printf("该寝室不存在\n");
   break;
}
p=p->next;
}
}
void tjcw(linklist head,linklist3 head3)
{
    linklist p,r=head->next;
    linklist3 p3,rear=head3;
    int n;
    char susehao[30]={'q','\0'};
    while(r)
    {
    p=head->next;
    while(p)
    {
    n=6;
    if(strcmp(r->susehao,p->susehao)==0)
    {
    n--;
    }
    if(p->next==NULL)
    {
    p3=(linklist3)malloc(sizeof(lnode3));
    strcpy(p3->qs,p->susehao);
    p3->b=n;
    rear->next3=p3;
    rear=p3;
    }
    p=p->next;
    }
    r=r->next;
    }
    rear->next3=NULL;
    p3=head3->next3;
    system("cls");
    printf("%-40s %-40s %-40s\n","寝室","人数","空闲床位");
    while(p3)
    {
    if(p3->b!=6&&strcmp(p3->qs,susehao)!=0)
    {
    printf("%-40s %-40d %-40d\n",p3->qs,p3->b,6-(p3->b));//想了好久
    strcpy(susehao,p3->qs);
    }
    p3=p3->next3;
    }
}
void output2(linklist2 head2)
{
    linklist2 p = head2->next2;
    printf("%-80s%-80s\n","帐号","密码");
    while(p)
    {
        printf("%-80s%-80s\n",p->zh,p->mima);
        p=p->next2;
    }
}
void output(linklist head,linklist4 head4,linklist5 head5,linklist6 head6)
{
    linklist p=head->next;
    linklist4 p4=head4->next4;
    linklist5 p5;
    int a,c,n=0,f;
    char b[30],d[10];
    d[0]=' ',d[1]='\0';
    while(p)
    {
      n++;
      p=p->next;
    }
    printf("1.全部浏览,2.分页浏览,其他字符.退出\n");
    scanf("%d",&a);
    system("cls");
    getchar();
    if(a==1)
    {
    printf("当前系统中共有%d个信息\n",n);
    printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
    p=head->next;
    while(p)
    {
        p4=head4->next4;
        p5=head5->next5;
        sscanf(p->id,"%*4d%6d%*2d",&c);
        printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
        b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
        while(p4)
        {
            if((strcmp(p4->id2,b))==0)
            {
            printf("%-20s %-20s %-20s\n",p4->xueyuan,p4->zhuanye,p4->banji);
            break;
            }
            p4=p4->next4;
            }
        while(p5)
        {
            if((strcmp(p5->susehao2,p->susehao))==0)
            {
            printf("%-20s %-10s %-10s %-20s %-20s\n\n","寝室长",d,p5->name2,p5->id3,p5->dianhua2);
            break;
            }
            p5=p5->next5;
        }
        p=p->next;
    }

    }

    else if(a==2)
    {
        p=head->next;
loop:
    f=0;
    printf("当前系统中共有%d个信息\n",n);
    printf("%-20s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n","宿舍号","床号","姓名","学号","电话","是否正常毕业","是否为寝室长","学院","专业","班级");
    p=head->next;
    while(p)
    {
        p4=head4->next4;
        p5=head5->next5;
        sscanf(p->id,"%*4d%6d%*2d",&c);
        printf("%-20s %-10d %-10s %-20s %-20s %-20s %-20s",p->susehao,p->chuanghao,p->name,p->id,p->dianhua,p->bz1,p->bz2);
        b[6]='\0',b[5]=c%10+'0',b[4]=c/10%10+'0',b[3]=c/100%10+'0',b[2]=c/1000%10+'0',b[1]=c/10000%10+'0',b[0]=c/100000+'0';
        while(p4)
        {
            if((strcmp(p4->id2,b))==0)
            {
            printf("%-20s %-20s %-20s\n",p4->xueyuan,p4->zhuanye,p4->banji);
            break;
            }
            p4=p4->next4;
            }
        while(p5)
        {
            if((strcmp(p5->susehao2,p->susehao))==0)
            {
            printf("%-20s %-10s %-10s %-20s %-20s\n\n","寝室长",d,p5->name2,p5->id3,p5->dianhua2);
            break;
            }
            p5=p5->next5;
        }
        f++;
        if(f==12)
        {
            char s[30];
            printf("enter.下一页 2.其它字符.返回上一级\n");
            gets(s);
            if(s[0]=='\0')
            {
                system("cls");
                goto loop;
            }
            else
            {
                break;
            }
        }
        p=p->next;
    }
    }
    }
void load6(linklist6 head6)
{
linklist6 p,rear=head6;
char id4[20],xy[20];
FILE *fp;
if((fp=fopen("xy.txt","r"))==NULL)
{
     printf("open error\n");
     exit(0);
}
while((fscanf(fp,"%s %s\n",id4,xy))!=EOF)
{
        p = (linklist6)malloc(sizeof(lnode6));
        strcpy(p->id4,id4);
        strcpy(p->xy,xy);
        rear->next6 = p;
        rear = p;
}
rear->next6=NULL;
fclose(fp);
}



